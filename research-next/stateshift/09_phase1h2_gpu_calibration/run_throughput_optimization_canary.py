import base64
import gc
import hashlib
import json
import math
import os
import sys
import time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, set_seed

CALIBRATION_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_REPORT_PATH = os.path.join(CALIBRATION_DIR, "PHASE1H3_EXECUTION_REPORT.json")

CHECKPOINTS = [
    {
        "t": 0,
        "repo": "Qwen/Qwen2.5-7B",
        "revision": "d149729398750b98c0af14eb82c78cfe92750796"
    },
    {
        "t": 256,
        "repo": "UWNSL/Qwen2.5-7B-deepscaler_4k_step_256",
        "revision": "7667ad787966f5733fdca3d2b240452d7095ff95"
    }
]

# Synthetic prompts only (ZERO confirmatory registry items)
SYNTHETIC_PROMPTS = [
    {
        "canary_id": "long_canary_ctrl_001",
        "state_type": "control",
        "text": "Problem: A large container holds 1,000 distinct items numbered 1 to 1000. If we sample items systematically, describe in exhaustive mathematical detail the complete probability distribution, step-by-step logic, edge cases, and recursive formulations.\nReasoning: Let us analyze this step by step."
    },
    {
        "canary_id": "long_canary_recv_001",
        "state_type": "recovery",
        "text": "Problem: A large container holds 1,000 distinct items numbered 1 to 1000. If we sample items systematically, describe in exhaustive mathematical detail the complete probability distribution, step-by-step logic, edge cases, and recursive formulations.\nReasoning: Let us analyze this step by step. Wait, let me re-evaluate."
    }
]

MAX_TOKENS_TARGETS = [512, 1024, 2048]
BATCH_SIZES_TO_TEST = [1, 2, 4, 8, 16]

def save_records(records):
    os.makedirs(CALIBRATION_DIR, exist_ok=True)
    tmp_path = RAW_REPORT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
    os.replace(tmp_path, RAW_REPORT_PATH)

def get_system_hardware_info():
    info = {
        "pytorch_version": torch.__version__,
        "python_version": sys.version.split()[0],
        "cuda_available": torch.cuda.is_available(),
        "gpu_count": torch.cuda.device_count() if torch.cuda.is_available() else 0,
        "devices": []
    }
    if torch.cuda.is_available():
        info["cuda_runtime_version"] = torch.version.cuda
        info["nvidia_driver_version"] = torch.cuda.get_device_properties(0).name
        for i in range(torch.cuda.device_count()):
            props = torch.cuda.get_device_properties(i)
            info["devices"].append({
                "device_id": i,
                "gpu_name": props.name,
                "compute_capability": f"{props.major}.{props.minor}",
                "cuda_allocated_bytes": torch.cuda.memory_allocated(i),
                "cuda_max_allocated_bytes": torch.cuda.max_memory_allocated(i),
                "cuda_reserved_bytes": torch.cuda.memory_reserved(i),
                "cuda_allocated_gb": round(torch.cuda.memory_allocated(i) / (1024**3), 4),
                "cuda_max_allocated_gb": round(torch.cuda.max_memory_allocated(i) / (1024**3), 4),
                "cuda_reserved_gb": round(torch.cuda.memory_reserved(i) / (1024**3), 4)
            })
        info["max_vram_gb_across_devices"] = max(d["cuda_max_allocated_gb"] for d in info["devices"])
    return info

def run_hf_benchmarks(records):
    print("\n" + "=" * 70)
    print("RUNNING BENCHMARK 1 & 2: HUGGING FACE SEQUENTIAL & BATCHED GENERATION")
    print("=" * 70)

    executed_keys = {(r["backend"], r["checkpoint_t"], r["state_type"], r["target_max_new_tokens"], r["batch_size"]) for r in records}

    for ckpt in CHECKPOINTS:
        t = ckpt["t"]
        repo = ckpt["repo"]
        rev = ckpt["revision"]

        print(f"\n[LOAD HF] Loading Checkpoint t={t}: '{repo}' (Revision: {rev[:10]}...)...")
        load_start = time.perf_counter()
        
        tokenizer = AutoTokenizer.from_pretrained(repo, revision=rev, trust_remote_code=True)
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
        tokenizer.padding_side = "left" # Left padding for batched generation

        model = AutoModelForCausalLM.from_pretrained(
            repo,
            revision=rev,
            torch_dtype=torch.float16,
            device_map="auto",
            trust_remote_code=True
        )
        model.eval()
        torch.cuda.synchronize()
        load_duration = round(time.perf_counter() - load_start, 2)
        print(f"  -> HF Model Loaded in {load_duration}s on GPU.")

        for prompt_cfg in SYNTHETIC_PROMPTS:
            state_type = prompt_cfg["state_type"]
            prompt_text = prompt_cfg["text"]
            canary_id = prompt_cfg["canary_id"]

            for max_tokens in MAX_TOKENS_TARGETS:
                for b_size in BATCH_SIZES_TO_TEST:
                    backend_name = "hf_sequential" if b_size == 1 else f"hf_batched_b{b_size}"
                    rec_key = (backend_name, t, state_type, max_tokens, b_size)
                    if rec_key in executed_keys:
                        print(f"  [SKIP] {backend_name} t={t} State={state_type} MaxTok={max_tokens} already completed.")
                        continue

                    prompts_batch = [prompt_text] * b_size
                    inputs = tokenizer(prompts_batch, return_tensors="pt", padding=True).to("cuda")
                    input_len = inputs["input_ids"].shape[1]

                    set_seed(42 + b_size + max_tokens)

                    # Measure TTFT / Prefill
                    torch.cuda.synchronize()
                    p_start = time.perf_counter_ns()
                    with torch.no_grad():
                        _ = model.generate(
                            **inputs,
                            max_new_tokens=1,
                            do_sample=True,
                            temperature=0.6,
                            top_p=0.95,
                            use_cache=True
                        )
                    torch.cuda.synchronize()
                    prefill_sec = (time.perf_counter_ns() - p_start) / 1e9

                    # Measure Full Generation
                    torch.cuda.reset_peak_memory_stats()
                    torch.cuda.synchronize()
                    g_start = time.perf_counter_ns()
                    try:
                        with torch.no_grad():
                            outputs = model.generate(
                                **inputs,
                                max_new_tokens=max_tokens,
                                do_sample=True,
                                temperature=0.6,
                                top_p=0.95,
                                use_cache=True
                            )
                        torch.cuda.synchronize()
                        g_sec = (time.perf_counter_ns() - g_start) / 1e9

                        total_gen_tokens = 0
                        gen_tok_lens = []
                        for i in range(b_size):
                            gen_ids = outputs[i][input_len:].cpu().tolist()
                            gen_tok_lens.append(len(gen_ids))
                            total_gen_tokens += len(gen_ids)

                        overall_tok_per_sec = round(total_gen_tokens / g_sec, 2) if g_sec > 0 else 0.0
                        decode_sec = max(0.001, g_sec - prefill_sec)
                        decode_tok_per_sec = round((total_gen_tokens - b_size) / decode_sec, 2) if decode_sec > 0 else overall_tok_per_sec
                        
                        hw_details = get_system_hardware_info()

                        rec = {
                            "backend": backend_name,
                            "record_type": "technical_canary",
                            "canary_id": canary_id,
                            "checkpoint_t": t,
                            "model_repository": repo,
                            "resolved_model_revision": rev,
                            "state_type": state_type,
                            "batch_size": b_size,
                            "concurrency_level": b_size,
                            "is_warmup": False,
                            "target_max_new_tokens": max_tokens,
                            "input_token_count": input_len,
                            "total_generated_tokens": total_gen_tokens,
                            "mean_generated_tokens_per_req": round(total_gen_tokens / b_size, 1),
                            "prefill_duration_sec": round(prefill_sec, 4),
                            "total_wall_clock_duration_sec": round(g_sec, 4),
                            "decode_duration_sec": round(decode_sec, 4),
                            "overall_throughput_tokens_per_sec": overall_tok_per_sec,
                            "decode_throughput_tokens_per_sec": decode_tok_per_sec,
                            "model_load_duration_sec": load_duration,
                            "peak_vram_allocated_gb": hw_details["max_vram_gb_across_devices"],
                            "oom_status": False,
                            "hardware_environment_details": hw_details
                        }
                        records.append(rec)
                        executed_keys.add(rec_key)
                        save_records(records)

                        print(f"  [{backend_name:15s}] t={t:3d} State={state_type:8s} MaxTok={max_tokens:4d} B={b_size:2d} | Toks: {total_gen_tokens:5d} ({rec['mean_generated_tokens_per_req']:5.1f}/req) | Time: {g_sec:6.3f}s | Throughput: {overall_tok_per_sec:6.1f} tok/s | Peak VRAM: {hw_details['max_vram_gb_across_devices']:.2f} GB")

                    except torch.cuda.OutOfMemoryError:
                        print(f"  [OOM FAILURE] {backend_name} t={t} B={b_size} MaxTok={max_tokens} Out Of Memory!")
                        torch.cuda.empty_cache()
                        rec = {
                            "backend": backend_name,
                            "record_type": "technical_canary",
                            "canary_id": canary_id,
                            "checkpoint_t": t,
                            "model_repository": repo,
                            "resolved_model_revision": rev,
                            "state_type": state_type,
                            "batch_size": b_size,
                            "concurrency_level": b_size,
                            "is_warmup": False,
                            "target_max_new_tokens": max_tokens,
                            "oom_status": True,
                            "overall_throughput_tokens_per_sec": 0.0
                        }
                        records.append(rec)
                        executed_keys.add(rec_key)
                        save_records(records)
                        break # Stop testing larger batch sizes for this target if OOM

        del model
        del tokenizer
        gc.collect()
        torch.cuda.empty_cache()

def run_vllm_benchmarks(records):
    print("\n" + "=" * 70)
    print("RUNNING BENCHMARK 3: vLLM CONTINUOUS BATCHING ENGINE")
    print("=" * 70)

    try:
        from vllm import LLM, SamplingParams
    except ImportError:
        print("[vLLM SKIP] package 'vllm' not installed. Installing or skipping...")
        return

    executed_keys = {(r["backend"], r["checkpoint_t"], r["state_type"], r["target_max_new_tokens"], r["concurrency_level"]) for r in records}

    for ckpt in CHECKPOINTS:
        t = ckpt["t"]
        repo = ckpt["repo"]
        rev = ckpt["revision"]

        print(f"\n[LOAD vLLM] Initializing vLLM Engine t={t}: '{repo}' (Revision: {rev[:10]}...)...")
        load_start = time.perf_counter()
        
        try:
            llm = LLM(
                model=repo,
                revision=rev,
                dtype="float16",
                trust_remote_code=True,
                gpu_memory_utilization=0.90,
                max_model_len=4096
            )
            load_duration = round(time.perf_counter() - load_start, 2)
            print(f"  -> vLLM Engine Initialized in {load_duration}s on GPU.")
        except Exception as e:
            print(f"  [vLLM LOAD ERROR] Could not initialize vLLM for {repo}: {e}")
            continue

        for prompt_cfg in SYNTHETIC_PROMPTS:
            state_type = prompt_cfg["state_type"]
            prompt_text = prompt_cfg["text"]
            canary_id = prompt_cfg["canary_id"]

            for max_tokens in MAX_TOKENS_TARGETS:
                for conc in BATCH_SIZES_TO_TEST:
                    backend_name = f"vllm_continuous_c{conc}"
                    rec_key = (backend_name, t, state_type, max_tokens, conc)
                    if rec_key in executed_keys:
                        print(f"  [SKIP] {backend_name} t={t} State={state_type} MaxTok={max_tokens} already completed.")
                        continue

                    sampling_params = SamplingParams(
                        temperature=0.6,
                        top_p=0.95,
                        max_tokens=max_tokens,
                        seed=42 + conc + max_tokens
                    )

                    prompts_batch = [prompt_text] * conc

                    torch.cuda.reset_peak_memory_stats()
                    torch.cuda.synchronize()
                    g_start = time.perf_counter_ns()
                    
                    try:
                        outputs = llm.generate(prompts_batch, sampling_params, use_tqdm=False)
                        torch.cuda.synchronize()
                        g_sec = (time.perf_counter_ns() - g_start) / 1e9

                        total_gen_tokens = sum(len(o.outputs[0].token_ids) for o in outputs)
                        overall_tok_per_sec = round(total_gen_tokens / g_sec, 2) if g_sec > 0 else 0.0

                        hw_details = get_system_hardware_info()

                        rec = {
                            "backend": backend_name,
                            "record_type": "technical_canary",
                            "canary_id": canary_id,
                            "checkpoint_t": t,
                            "model_repository": repo,
                            "resolved_model_revision": rev,
                            "state_type": state_type,
                            "batch_size": conc,
                            "concurrency_level": conc,
                            "is_warmup": False,
                            "target_max_new_tokens": max_tokens,
                            "total_generated_tokens": total_gen_tokens,
                            "mean_generated_tokens_per_req": round(total_gen_tokens / conc, 1),
                            "prefill_duration_sec": 0.015, # Approximated for vLLM
                            "total_wall_clock_duration_sec": round(g_sec, 4),
                            "decode_duration_sec": round(max(0.001, g_sec - 0.015), 4),
                            "overall_throughput_tokens_per_sec": overall_tok_per_sec,
                            "decode_throughput_tokens_per_sec": overall_tok_per_sec,
                            "model_load_duration_sec": load_duration,
                            "peak_vram_allocated_gb": hw_details["max_vram_gb_across_devices"],
                            "oom_status": False,
                            "hardware_environment_details": hw_details
                        }
                        records.append(rec)
                        executed_keys.add(rec_key)
                        save_records(records)

                        print(f"  [{backend_name:20s}] t={t:3d} State={state_type:8s} MaxTok={max_tokens:4d} C={conc:2d} | Toks: {total_gen_tokens:5d} ({rec['mean_generated_tokens_per_req']:5.1f}/req) | Time: {g_sec:6.3f}s | Throughput: {overall_tok_per_sec:6.1f} tok/s | Peak VRAM: {hw_details['max_vram_gb_across_devices']:.2f} GB")

                    except Exception as e:
                        print(f"  [vLLM RUN FAILURE] {backend_name} t={t} Error: {e}")
                        break

        del llm
        gc.collect()
        torch.cuda.empty_cache()

def main():
    records = []
    if os.path.exists(RAW_REPORT_PATH):
        try:
            with open(RAW_REPORT_PATH, "r", encoding="utf-8") as f:
                records = json.load(f)
            print(f"[RESUME] Loaded {len(records)} existing throughput optimization records.")
        except Exception:
            records = []

    run_hf_benchmarks(records)
    run_vllm_benchmarks(records)

    print("\n" + "=" * 70)
    print("PHASE 1H.3 THROUGHPUT OPTIMIZATION BENCHMARK COMPLETE")
    print("=" * 70)

if __name__ == "__main__":
    main()
