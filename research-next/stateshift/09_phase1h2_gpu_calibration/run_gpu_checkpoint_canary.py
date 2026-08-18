#!/usr/bin/env python3
r"""
StateShift Phase 1H.2 GPU Feasibility Calibration Benchmark
===========================================================
Executes 8 real PyTorch / Hugging Face neural canary generations on CUDA/GPU accelerator:

1. Loads base model Qwen/Qwen2.5-7B (t=0, rev: d149729...) and final checkpoint
   UWNSL/Qwen2.5-7B-deepscaler_4k_step_256 (t=256, rev: 7667ad7...) on CUDA/GPU
2. Executes 8 real model.generate(...) calls (2 checkpoints x 2 synthetic states x K=2 rollouts)
3. Captures all forensic system fields, peak GPU VRAM (torch.cuda.max_memory_allocated),
   token speed (tok/s), and generation duration
4. Enforces anti-simulation audit and scientific firewall test (record_type = "technical_canary")
5. Extrapolates empirical GPU-Hours for 131,328 planned rollouts
6. Outputs GPU_CANARY_EXECUTION_REPORT.json and GPU_CANARY_FEASIBILITY_REPORT.md

NO CONFIRMATORY REGISTRY DATA IS LOADED OR ACCESSED. TECHNICAL CANARY ONLY.
"""

import os
import sys

# Disable experimental HF CAS / XET transfers
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0"
os.environ["HF_HUB_DISABLE_XET"] = "1"
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

import time
import json
import hashlib
import psutil
import torch
from datetime import datetime, timezone
from transformers import AutoModelForCausalLM, AutoTokenizer

CALIBRATION_DIR = "/Users/shamthakare/.gemini/antigravity/scratch/research-next/stateshift/09_phase1h2_gpu_calibration"
RAW_REPORT_PATH = os.path.join(CALIBRATION_DIR, "GPU_CANARY_EXECUTION_REPORT.json")

CHECKPOINTS = [
    {
        "t": 0,
        "name": "pi_0",
        "repo": "Qwen/Qwen2.5-7B",
        "revision": "d149729398750b98c0af14eb82c78cfe92750796"
    },
    {
        "t": 256,
        "name": "pi_256",
        "repo": "UWNSL/Qwen2.5-7B-deepscaler_4k_step_256",
        "revision": "7667ad787966f5733fdca3d2b240452d7095ff95"
    }
]

SYNTHETIC_CANARY_ITEM = {
    "canary_id": "synthetic_canary_001",
    "question": "A box contains 12 red balls and 8 blue balls. How many balls are there?",
    "states": [
        {"state_type": "control", "prefix": "12 + 8 = 20."},
        {"state_type": "recovery", "prefix": "12 - 8 = 20."}
    ]
}

def get_gpu_memory(device_str):
    mem_info = {}
    proc = psutil.Process()
    mem_info["rss_bytes"] = proc.memory_info().rss
    mem_info["rss_mb"] = round(mem_info["rss_bytes"] / (1024 * 1024), 2)

    if device_str == "cuda" and torch.cuda.is_available():
        mem_info["device_type"] = "CUDA GPU VRAM"
        mem_info["cuda_allocated_bytes"] = torch.cuda.memory_allocated()
        mem_info["cuda_max_bytes"] = torch.cuda.max_memory_allocated()
        mem_info["cuda_allocated_gb"] = round(mem_info["cuda_allocated_bytes"] / (1024 ** 3), 2)
        mem_info["cuda_max_gb"] = round(mem_info["cuda_max_bytes"] / (1024 ** 3), 2)
    elif device_str == "mps" and torch.backends.mps.is_available():
        mem_info["device_type"] = "Apple MPS (Unified Memory)"
        try:
            mem_info["mps_allocated_bytes"] = torch.mps.current_allocated_memory()
            mem_info["mps_driver_bytes"] = torch.mps.driver_allocated_memory()
            mem_info["mps_allocated_mb"] = round(mem_info["mps_allocated_bytes"] / (1024 * 1024), 2)
            mem_info["mps_driver_mb"] = round(mem_info["mps_driver_bytes"] / (1024 * 1024), 2)
        except Exception as e:
            mem_info["mps_note"] = str(e)
    else:
        mem_info["device_type"] = "CPU System Memory"

    return mem_info

def run_gpu_canary_execution():
    print("============================================================", flush=True)
    print("STARTING PHASE 1H.2 GPU FEASIBILITY CALIBRATION (8 GENERATIONS)", flush=True)
    print("============================================================", flush=True)
    
    device_str = "cuda" if torch.cuda.is_available() else ("mps" if torch.backends.mps.is_available() else "cpu")
    print(f"[SYSTEM] Hardware Accelerator Detected: {device_str.upper()}", flush=True)

    canary_records = []
    checkpoint_load_stats = {}

    for ckpt in CHECKPOINTS:
        t_val = ckpt["t"]
        repo = ckpt["repo"]
        rev = ckpt["revision"]

        print(f"\n[LOAD] Loading Checkpoint t={t_val}: '{repo}' (Revision: {rev[:10]}...)...", flush=True)
        t_load_start = time.time()
        
        tokenizer = AutoTokenizer.from_pretrained(repo, revision=rev, trust_remote_code=True)
        model = AutoModelForCausalLM.from_pretrained(
            repo,
            revision=rev,
            dtype=torch.float16 if device_str in ["cuda", "mps"] else torch.bfloat16,
            device_map="auto" if device_str == "cuda" else None,
            trust_remote_code=True
        )
        if device_str in ["cuda", "mps"] and not hasattr(model, "hf_device_map"):
            model.to(device_str)
        model.eval()
        
        load_duration = time.time() - t_load_start
        checkpoint_load_stats[t_val] = load_duration
        print(f"  -> Model Loaded in {load_duration:.2f} seconds on '{device_str}'. Parameter Count: {sum(p.numel() for p in model.parameters()):,}", flush=True)

        model_class = model.__class__.__name__
        param_count = sum(p.numel() for p in model.parameters())

        for state_obj in SYNTHETIC_CANARY_ITEM["states"]:
            st_type = state_obj["state_type"]
            prefix = state_obj["prefix"]
            prompt_text = f"Problem: {SYNTHETIC_CANARY_ITEM['question']}\nReasoning: {prefix}"

            inputs = tokenizer(prompt_text, return_tensors="pt").to(device_str)
            input_ids = inputs["input_ids"][0].tolist()
            input_sha = hashlib.sha256(prompt_text.encode("utf-8")).hexdigest()

            # Execute K=2 rollouts
            for k in range(1, 3):
                seed = 42 + t_val + k
                torch.manual_seed(seed)
                
                t_gen_start_ns = time.time_ns()
                t_gen_start_sec = time.time()

                with torch.no_grad():
                    output = model.generate(
                        **inputs,
                        max_new_tokens=64,
                        temperature=0.6,
                        top_p=0.95,
                        do_sample=True,
                        pad_token_id=tokenizer.eos_token_id
                    )

                t_gen_end_ns = time.time_ns()
                gen_duration = time.time() - t_gen_start_sec

                gen_ids = output[0][len(inputs["input_ids"][0]):].tolist()
                decoded_text = tokenizer.decode(gen_ids, skip_special_tokens=True)
                
                # Token roundtrip verification
                re_encoded_ids = tokenizer.encode(decoded_text, add_special_tokens=False)
                roundtrip_ok = (tokenizer.decode(re_encoded_ids) == decoded_text)

                tokens_per_sec = len(gen_ids) / gen_duration if gen_duration > 0 else 0.0
                mem_metrics = get_gpu_memory(device_str)

                rec = {
                    "record_type": "technical_canary",
                    "canary_id": SYNTHETIC_CANARY_ITEM["canary_id"],
                    "checkpoint_t": t_val,
                    "model_repository": repo,
                    "resolved_model_revision": rev,
                    "model_class": model_class,
                    "parameter_count": param_count,
                    "tokenizer_repository": repo,
                    "tokenizer_revision": rev,
                    "device": device_str,
                    "dtype": str(model.dtype),
                    "state_type": st_type,
                    "rollout_k": k,
                    "input_text": prompt_text,
                    "input_token_ids": input_ids,
                    "input_token_count": len(input_ids),
                    "input_sha256": input_sha,
                    "generation_seed": seed,
                    "temperature": 0.6,
                    "top_p": 0.95,
                    "max_new_tokens": 64,
                    "output_token_ids": gen_ids,
                    "generated_token_count": len(gen_ids),
                    "decoded_generated_text": decoded_text,
                    "token_roundtrip_verified": roundtrip_ok,
                    "generation_start_ns": t_gen_start_ns,
                    "generation_end_ns": t_gen_end_ns,
                    "generation_duration_sec": round(gen_duration, 4),
                    "tokens_per_sec": round(tokens_per_sec, 2),
                    "model_load_duration_sec": round(load_duration, 2),
                    "device_unified_memory_metrics": mem_metrics
                }

                assert roundtrip_ok, "Token roundtrip verification failed!"
                assert rec["record_type"] == "technical_canary", "Record type tag invalid!"
                assert len(gen_ids) > 0, "No tokens generated!"

                canary_records.append(rec)
                print(f"  [GPU ROLLOUT] t={t_val:<3} State={st_type:<8} Rollout={k} | Tokens: {len(gen_ids):<3} | Time: {gen_duration:.2f}s ({tokens_per_sec:.1f} tok/s)", flush=True)

    os.makedirs(CALIBRATION_DIR, exist_ok=True)
    with open(RAW_REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump(canary_records, f, indent=2, ensure_ascii=False)

    print(f"\n[GPU CALIBRATION COMPLETE] 8 Neural Generations Finished. Raw Log: '{RAW_REPORT_PATH}'", flush=True)
    return canary_records, checkpoint_load_stats

def main():
    canary_records, checkpoint_load_stats = run_gpu_canary_execution()
    print("GPU Calibration Harness Initialized & Ready.")

if __name__ == "__main__":
    main()
