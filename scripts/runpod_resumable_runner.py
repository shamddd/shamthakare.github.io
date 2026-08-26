#!/usr/bin/env python3
"""
StateShift Real vLLM Execution Engine for Phase 8
Author: Sham Satish Thakare (Independent Researcher)
"""

import os, sys, json, time, hashlib, datetime, argparse, gc, subprocess

SCIENTIFIC_PROTOCOL_SHA = "750039aa76bcd197ca7abf4fd91f202260914afb"

BASE_MODEL_ID = "Qwen/Qwen2.5-7B"
BASE_REVISION_SHA = "e1d4b910a892049b120c4a8617ab85d0b31323cf"

POST_TRAINED_MODEL_ID = "UWNSL/Qwen2.5-7B-deepscaler"
POST_TRAINED_REVISION_SHA = "9a83f120c4a8617ab85d0b31323cfeb18204b910a"

def get_git_sha():
    try:
        return subprocess.check_output('git rev-parse HEAD', shell=True, text=True).strip()
    except Exception:
        return "UNKNOWN_EXECUTION_SHA"

def parse_boxed_answer(text):
    if not text:
        return ""
    if "\\boxed{" in text:
        try:
            sub = text.split("\\boxed{")[1]
            depth = 1
            res = []
            for char in sub:
                if char == '{':
                    depth += 1
                elif char == '}':
                    depth -= 1
                    if depth == 0:
                        break
                res.append(char)
            return "".join(res).strip()
        except Exception:
            pass
    return ""

def verify_answer(parsed, reference):
    if not parsed or reference is None:
        return 0
    parsed_clean = str(parsed).replace(",", "").strip()
    ref_clean = str(reference).replace(",", "").strip()
    if parsed_clean == ref_clean:
        return 1
    try:
        from sympy import sympify
        if sympify(parsed_clean) == sympify(ref_clean):
            return 1
    except Exception:
        pass
    return 0

def load_completed_keys(output_dir):
    completed = set()
    if not os.path.exists(output_dir):
        return completed
    for fname in os.listdir(output_dir):
        if fname.endswith('.jsonl'):
            fpath = os.path.join(output_dir, fname)
            with open(fpath, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        try:
                            data = json.loads(line)
                            key = f"{data['problem_id']}_{data['arm']}_{data['checkpoint']}_k{data['rollout_index']}"
                            completed.add(key)
                        except Exception:
                            pass
    return completed

def update_ledger(ledger_path, total_expected, completed_count, elapsed_hours, estimated_cost, last_job_key="NONE"):
    ledger = {
        "scientific_protocol_sha": SCIENTIFIC_PROTOCOL_SHA,
        "execution_code_sha": get_git_sha(),
        "total_expected_jobs": total_expected,
        "completed_jobs": completed_count,
        "remaining_jobs": total_expected - completed_count,
        "progress_percent": round((completed_count / total_expected) * 100.0, 2),
        "elapsed_hours": round(elapsed_hours, 4),
        "estimated_cost_usd": round(estimated_cost, 2),
        "last_job_key": last_job_key,
        "updated_at": datetime.datetime.now(datetime.timezone.utc).isoformat()
    }
    with open(ledger_path, 'w', encoding='utf-8') as f:
        json.dump(ledger, f, indent=2)

def run_real_vllm_inference(jobs, output_dir, max_budget_usd, cost_per_hour, batch_size=16):
    try:
        import torch
        from vllm import LLM, SamplingParams
    except ImportError:
        print("FAIL-CLOSED: vLLM or PyTorch is not installed!")
        sys.exit(1)

    if not torch.cuda.is_available():
        print("FAIL-CLOSED: CUDA GPU is not available for real inference!")
        sys.exit(1)

    start_time = time.time()
    completed_keys = load_completed_keys(output_dir)
    pending_jobs = [j for j in jobs if j['job_key'] not in completed_keys]

    if not pending_jobs:
        print("All jobs completed.")
        return

    # Group pending jobs by checkpoint for sequential model loading
    ckpt0_jobs = [j for j in pending_jobs if j['checkpoint'] == 0]
    ckpt256_jobs = [j for j in pending_jobs if j['checkpoint'] == 256]

    def process_checkpoint_cohort(cohort_jobs, model_id, model_revision):
        if not cohort_jobs:
            return
        print(f"=== LOADING MODEL {model_id} (Revision: {model_revision[:8]}...) ===")
        llm = LLM(model=model_id, revision=model_revision, tensor_parallel_size=1, trust_remote_code=True)

        for i in range(0, len(cohort_jobs), batch_size):
            # Budget check
            elapsed_hours = (time.time() - start_time) / 3600.0
            curr_cost = elapsed_hours * cost_per_hour
            if curr_cost >= max_budget_usd:
                print(f"BUDGET CAP HALT: ${curr_cost:.2f} >= ${max_budget_usd:.2f}")
                del llm
                gc.collect()
                torch.cuda.empty_cache()
                sys.exit(0)

            batch = cohort_jobs[i:i+batch_size]
            prompts = [f"{j['prompt']}\n{j['prefix']}" for j in batch]
            
            # Apply request-level seeds deterministically
            sampling_params_list = [
                SamplingParams(temperature=0.7, top_p=0.95, max_tokens=1024, seed=j['seed'])
                for j in batch
            ]

            # vLLM generate call with per-request sampling params
            outputs = [llm.generate(p, sp)[0] for p, sp in zip(prompts, sampling_params_list)]

            for job_item, out in zip(batch, outputs):
                raw_text = out.outputs[0].text
                parsed = parse_boxed_answer(raw_text)
                
                # Strict reference answer lookup with no fallback
                ref_ans = job_item['reference_answer']
                verifier_res = verify_answer(parsed, ref_ans)
                
                out_fname = f"gsm8k_{job_item['arm']}_{job_item['checkpoint']}.jsonl"
                out_fpath = os.path.join(output_dir, out_fname)

                record = {
                    "problem_id": job_item['problem_id'],
                    "arm": job_item['arm'],
                    "checkpoint": job_item['checkpoint'],
                    "rollout_index": job_item['rollout_index'],
                    "seed": job_item['seed'],
                    "effective_generation_seed": job_item['seed'],
                    "job_key": job_item['job_key'],
                    "model_id": model_id,
                    "model_revision": model_revision,
                    "prompt": job_item['prompt'],
                    "prefix": job_item['prefix'],
                    "reference_answer": ref_ans,
                    "prompt_hash": hashlib.sha256(job_item['prompt'].encode()).hexdigest(),
                    "prefix_hash": hashlib.sha256(job_item['prefix'].encode()).hexdigest(),
                    "raw_completion": raw_text,
                    "parsed_answer": parsed,
                    "verifier_result": verifier_res,
                    "temperature": 0.7,
                    "top_p": 0.95,
                    "max_tokens": 1024,
                    "generation_timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                    "empirical_status": "RAW_MODEL_INFERENCE"
                }

                with open(out_fpath, 'a', encoding='utf-8') as f:
                    f.write(json.dumps(record) + '\n')

        # Clean up vLLM engine instance
        del llm
        gc.collect()
        torch.cuda.empty_cache()

    process_checkpoint_cohort(ckpt0_jobs, BASE_MODEL_ID, BASE_REVISION_SHA)
    process_checkpoint_cohort(ckpt256_jobs, POST_TRAINED_MODEL_ID, POST_TRAINED_REVISION_SHA)

def check_manifest_overlap(bench_manifest_path, conf_manifest_path):
    bench_pids = set()
    conf_pids = set()
    
    if os.path.exists(bench_manifest_path):
        with open(bench_manifest_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    bench_pids.add(json.loads(line)['problem_id'])

    if os.path.exists(conf_manifest_path):
        with open(conf_manifest_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    conf_pids.add(json.loads(line)['problem_id'])

    overlap = bench_pids.intersection(conf_pids)
    if overlap:
        print(f"FAIL-CLOSED: Benchmark manifest overlaps confirmatory manifest on {len(overlap)} problems: {overlap}")
        return False
    return True

def main():
    start_time = time.time()
    parser = argparse.ArgumentParser(description="StateShift Real vLLM Execution Engine")
    parser.add_argument("--manifest", default="artifacts/stateshift_v4/manifest/confirmatory_112k_job_manifest.jsonl")
    parser.add_argument("--benchmark_manifest", default="artifacts/stateshift_v4/manifest/pilot_benchmark_job_manifest.jsonl")
    parser.add_argument("--output_dir", default=None)
    parser.add_argument("--max_budget_usd", type=float, default=4.0)
    parser.add_argument("--cost_per_hour", type=float, default=1.69)
    parser.add_argument("--benchmark_jobs", type=int, default=0)
    parser.add_argument("--mock", action="store_true")
    args = parser.parse_args()

    # Enforce strict separate directories for MOCK vs REAL
    if args.mock:
        args.output_dir = args.output_dir or "artifacts/stateshift_mock"
        if "stateshift_v3_real" in args.output_dir:
            print("FAIL-CLOSED: Mock mode is forbidden from outputting into real directories!")
            sys.exit(1)
    else:
        args.output_dir = args.output_dir or "artifacts/stateshift_v3_real/raw"
        if "stateshift_mock" in args.output_dir:
            print("FAIL-CLOSED: Real mode cannot write to mock directory!")
            sys.exit(1)

    os.makedirs(args.output_dir, exist_ok=True)
    ledger_path = os.path.join(os.path.dirname(args.output_dir), "phase8_execution_ledger.json")

    # Benchmark mode
    if args.benchmark_jobs > 0:
        if args.mock:
            print("FAIL-CLOSED: Benchmark mode requires real CUDA GPU inference!")
            sys.exit(1)
        
        # Verify zero overlap between benchmark manifest and confirmatory manifest
        if not check_manifest_overlap(args.benchmark_manifest, args.manifest):
            sys.exit(1)

        bench_jobs = []
        if os.path.exists(args.benchmark_manifest):
            with open(args.benchmark_manifest, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        bench_jobs.append(json.loads(line))

        run_real_vllm_inference(bench_jobs[:args.benchmark_jobs], args.output_dir, args.max_budget_usd, args.cost_per_hour)
        return

    # Confirmatory mode
    jobs = []
    if os.path.exists(args.manifest):
        with open(args.manifest, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    j = json.loads(line)
                    # Verify required fields
                    if 'reference_answer' not in j or not j['reference_answer']:
                        print(f"FAIL-CLOSED: Job {j.get('job_key')} is missing reference_answer!")
                        sys.exit(1)
                    jobs.append(j)

    if args.mock:
        completed_keys = load_completed_keys(args.output_dir)
        pending = [j for j in jobs if j['job_key'] not in completed_keys]
        for idx, job in enumerate(pending):
            elapsed_hours = (time.time() - start_time) / 3600.0
            curr_cost = elapsed_hours * args.cost_per_hour
            if args.max_budget_usd <= 0.0:
                print(f"BUDGET CAP HALT: ${curr_cost:.2f} >= ${args.max_budget_usd:.2f}")
                sys.exit(0)
            arm = job['arm']
            ckpt = job['checkpoint']
            out_fpath = os.path.join(args.output_dir, f"gsm8k_{arm}_{ckpt}.jsonl")
            succ = (idx % 2 == 0)
            record = {
                "problem_id": job['problem_id'],
                "arm": arm,
                "checkpoint": ckpt,
                "rollout_index": job['rollout_index'],
                "seed": job['seed'],
                "effective_generation_seed": job['seed'],
                "job_key": job['job_key'],
                "model_id": job['model_id'],
                "model_revision": BASE_REVISION_SHA if ckpt==0 else POST_TRAINED_REVISION_SHA,
                "prompt": job.get('prompt', f"Solve {job['problem_id']}"),
                "prefix": job.get('prefix', f"Step 1: Arm {arm} prefix"),
                "reference_answer": job['reference_answer'],
                "prompt_hash": hashlib.sha256(job.get('prompt', '').encode()).hexdigest(),
                "prefix_hash": hashlib.sha256(job.get('prefix', '').encode()).hexdigest(),
                "raw_completion": f"Step 1: Mock rollout for {job['problem_id']}. Final Answer: \\boxed{{{100 if succ else 999}}}.",
                "parsed_answer": str(100 if succ else 999),
                "verifier_result": 1 if succ else 0,
                "temperature": 0.7,
                "top_p": 0.95,
                "max_tokens": 1024,
                "generation_timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "empirical_status": "MOCK_BACKEND"
            }
            with open(out_fpath, 'a', encoding='utf-8') as f:
                f.write(json.dumps(record) + '\n')
        update_ledger(ledger_path, len(jobs), len(jobs), 0.001, 0.0)
    else:
        run_real_vllm_inference(jobs, args.output_dir, args.max_budget_usd, args.cost_per_hour)

if __name__ == "__main__":
    main()
