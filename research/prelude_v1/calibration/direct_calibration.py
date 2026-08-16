"""
Direct Step-0 Calibration Runner with immediate output flushing.
"""

import time
import json
import os
import torch
import torch.nn.functional as F
import numpy as np
from transformers import AutoModelForCausalLM, AutoTokenizer
from research.prelude_v1.schema import TelemetryMeasurement


def run_calibration():
    device_str = "mps" if torch.backends.mps.is_available() else "cpu"
    device = torch.device(device_str)
    model_name = "HuggingFaceTB/SmolLM2-360M"
    
    print(f"[*] Initializing calibration for {model_name} on {device}...", flush=True)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        
    model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float32).to(device)
    ref_model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float32).to(device)
    ref_model.eval()
    
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-5)
    
    prompt = "Question: Sarah has 15 apples. She gives 4 to Tom and buys 7 more. How many apples does she have?\nLet's solve this step-by-step:\n"
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    prompt_len = inputs["input_ids"].size(1)
    
    group_size = 4
    max_gen_length = 32
    
    print("[*] Running rollout generation benchmark...", flush=True)
    t0 = time.perf_counter()
    with torch.no_grad():
        outputs = ref_model.generate(
            **inputs,
            max_new_tokens=max_gen_length,
            do_sample=True,
            temperature=0.7,
            num_return_sequences=group_size,
            pad_token_id=tokenizer.eos_token_id
        )
    t1 = time.perf_counter()
    gen_time = t1 - t0
    gen_tokens = (outputs.size(1) - prompt_len) * group_size
    gen_rate = gen_tokens / max(1e-4, gen_time)
    print(f"    Generation: {gen_tokens} tokens in {gen_time:.2f}s ({gen_rate:.1f} tok/s)", flush=True)
    
    print("[*] Running reference forward pass benchmark...", flush=True)
    t0 = time.perf_counter()
    with torch.no_grad():
        ref_logits = ref_model(outputs).logits[:, :-1, :]
        ref_log_probs = F.log_softmax(ref_logits, dim=-1)
    t1 = time.perf_counter()
    ref_time = t1 - t0
    print(f"    Reference Fwd: {ref_time:.2f}s", flush=True)
    
    print("[*] Running policy backward optimization benchmark...", flush=True)
    t0 = time.perf_counter()
    model.train()
    logits = model(outputs).logits[:, :-1, :]
    log_probs = F.log_softmax(logits, dim=-1)
    
    labels = outputs[:, 1:]
    token_log_probs = log_probs.gather(dim=-1, index=labels.unsqueeze(-1)).squeeze(-1)
    token_ref_log_probs = ref_log_probs.gather(dim=-1, index=labels.unsqueeze(-1)).squeeze(-1)
    
    mask = torch.zeros_like(labels, dtype=torch.float32)
    mask[:, prompt_len - 1:] = 1.0
    adv = torch.tensor([1.0, -1.0, 0.5, -0.5], dtype=torch.float32, device=device)
    
    loss = (-(token_log_probs.sum(dim=-1) * adv) + 0.04 * (token_ref_log_probs - token_log_probs).sum(dim=-1)).mean()
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    t1 = time.perf_counter()
    bwd_time = t1 - t0
    print(f"    Policy Bwd: {bwd_time:.2f}s", flush=True)
    
    total_step_time = gen_time + ref_time + bwd_time
    print(f"[+] Total GRPO step wall-clock: {total_step_time:.2f}s", flush=True)
    
    num_params = sum(p.numel() for p in model.parameters())
    peak_mem_mb = float(num_params * 4 * 2 / (1024 * 1024))
    
    telemetry = TelemetryMeasurement(
        device_name=f"Apple M-Series Silicon ({device_str.upper()})",
        device_type=device_str,
        model_name=model_name,
        model_scale_params=num_params,
        group_size=group_size,
        max_gen_length=max_gen_length,
        batch_size=1,
        prompt_tokens_per_sec=float(prompt_len / max(1e-4, ref_time)),
        generation_tokens_per_sec=float(gen_rate),
        backward_latency_sec=float(bwd_time),
        step_wall_clock_sec=float(total_step_time),
        peak_memory_mb=peak_mem_mb
    )
    
    out_dir = "/Users/shamthakare/.gemini/antigravity/scratch/research-reset/kakade"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "COMPUTE_CALIBRATION.json")
    with open(out_path, "w") as f:
        json.dump(telemetry.model_dump(), f, indent=2)
    print(f"[+] Written telemetry JSON to {out_path}", flush=True)


if __name__ == "__main__":
    run_calibration()
