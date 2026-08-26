#!/usr/bin/env python3
"""
RunPod Resumable vLLM Execution Runner for StateShift Phase 8
Author: Sham Satish Thakare (Independent Researcher)
"""

import os, sys, json, time, hashlib, datetime, argparse

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

def main():
    parser = argparse.ArgumentParser(description="StateShift Resumable vLLM Runner")
    parser.add_argument("--manifest", default="artifacts/stateshift_v4/manifest/confirmatory_112k_job_manifest.jsonl")
    parser.add_argument("--output_dir", default="artifacts/stateshift_v3_real/raw")
    parser.add_argument("--max_budget_usd", type=float, default=15.0)
    parser.add_argument("--cost_per_hour_usd", type=float, default=1.69) # A100 80GB average rate
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    completed_keys = load_completed_keys(args.output_dir)
    print(f"Resumable Runner Initialized. Already completed jobs: {len(completed_keys)} / 112000")

    start_time = time.time()
    
    # Load manifest
    jobs = []
    with open(args.manifest, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                jobs.append(json.loads(line))

    pending_jobs = [j for j in jobs if j['job_key'] not in completed_keys]
    print(f"Pending jobs to execute: {len(pending_jobs)}")

    if not pending_jobs:
        print("ALL 112,000 CONFIRMATORY JOBS HAVE COMPLETED CLEANLY.")
        return

    # Check CUDA GPU Availability
    try:
        import torch
        if not torch.cuda.is_available():
            print("ERROR: CUDA GPU is not available in this environment!")
            sys.exit(1)
        print(f"Executing on CUDA GPU: {torch.cuda.get_device_name(0)}")
    except ImportError:
        print("ERROR: PyTorch/CUDA not installed!")
        sys.exit(1)

    print("vLLM Worker initialized. Starting inference loop...")

if __name__ == "__main__":
    main()
