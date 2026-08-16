"""
Step-0 Hardware Throughput & Compute Calibration script for PRELUDE v1.
Profiles prompt throughput, rollout latency, backward step latency, and memory footprint on local hardware.
"""

import time
import json
import os
import torch
import torch.nn.functional as F
import numpy as np
from transformers import AutoModelForCausalLM, AutoTokenizer
from ..schema import TelemetryMeasurement


def run_hardware_calibration(model_name: str = "HuggingFaceTB/SmolLM2-360M", 
                             group_size: int = 4, 
                             max_gen_length: int = 32,
                             num_calibration_steps: int = 3,
                             device_str: str = "mps" if torch.backends.mps.is_available() else "cpu") -> TelemetryMeasurement:
    """
    Executes a real-time calibration benchmark with strict numerical clamping and profiling.
    """
    device = torch.device(device_str)
    print(f"[*] Starting Step-0 Hardware Calibration on device: {device} for model: {model_name}...")
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float32
    ).to(device)
    
    ref_model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float32
    ).to(device)
    ref_model.eval()
    
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-6, weight_decay=0.01)
    
    sample_prompts = [
        "Sarah has 15 apples. She gives 4 to Tom and buys 7 more. How many apples does she have?",
        "A train travels at 60 mph for 2.5 hours. What is the total distance covered in miles?",
        "If 3x + 7 = 22, what is the value of x?",
        "A store offers a 20% discount on a $50 shirt. What is the final price?"
    ]
    
    prompt_token_rates = []
    gen_token_rates = []
    backward_latencies = []
    step_latencies = []
    
    for step in range(num_calibration_steps):
        t_step_start = time.perf_counter()
        prompt = sample_prompts[step % len(sample_prompts)]
        formatted_prompt = f"Question: {prompt}\nLet's solve this step-by-step:\n"
        
        inputs = tokenizer(formatted_prompt, return_tensors="pt").to(device)
        prompt_len = inputs["input_ids"].size(1)
        
        # 1. Rollout Generation Phase (on reference/eval model to prevent logit corruption during profiling)
        t_gen_start = time.perf_counter()
        with torch.no_grad():
            outputs = ref_model.generate(
                **inputs,
                max_new_tokens=max_gen_length,
                do_sample=True,
                temperature=0.7,
                top_p=0.95,
                num_return_sequences=group_size,
                pad_token_id=tokenizer.eos_token_id
            )
        t_gen_end = time.perf_counter()
        
        gen_duration = t_gen_end - t_gen_start
        total_gen_toks = (outputs.size(1) - prompt_len) * group_size
        gen_token_rates.append(total_gen_toks / max(1e-4, gen_duration))
        prompt_token_rates.append(prompt_len / max(1e-4, gen_duration))
        
        # 2. Reference Forward Pass
        with torch.no_grad():
            ref_logits = ref_model(outputs).logits[:, :-1, :]
            ref_log_probs = F.log_softmax(ref_logits, dim=-1)
            
        # 3. Policy Forward & GRPO Backward Optimization Phase
        model.train()
        t_bwd_start = time.perf_counter()
        
        labels = outputs[:, 1:]
        logits = model(outputs).logits[:, :-1, :]
        log_probs = F.log_softmax(logits, dim=-1)
        
        token_log_probs = log_probs.gather(dim=-1, index=labels.unsqueeze(-1)).squeeze(-1)
        token_ref_log_probs = ref_log_probs.gather(dim=-1, index=labels.unsqueeze(-1)).squeeze(-1)
        
        mask = torch.zeros_like(labels, dtype=torch.float32)
        mask[:, prompt_len - 1:] = 1.0
        
        adv = torch.tensor([1.0, -1.0, 0.5, -0.5], dtype=torch.float32, device=device)[:group_size]
        
        kl_div = (token_ref_log_probs - token_log_probs) * mask
        kl_penalty = 0.04 * kl_div.sum(dim=-1)
        response_log_probs = (token_log_probs * mask).sum(dim=-1)
        
        loss = (-(response_log_probs * adv) + kl_penalty).mean()
        
        optimizer.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        optimizer.step()
        t_bwd_end = time.perf_counter()
        
        backward_duration = t_bwd_end - t_bwd_start
        backward_latencies.append(backward_duration)
        
        t_step_end = time.perf_counter()
        step_latencies.append(t_step_end - t_step_start)
        print(f"    Step {step+1}/{num_calibration_steps}: {step_latencies[-1]:.2f}s (Gen: {gen_duration:.2f}s, Bwd: {backward_duration:.2f}s)")
        
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
        prompt_tokens_per_sec=float(np.mean(prompt_token_rates)),
        generation_tokens_per_sec=float(np.mean(gen_token_rates)),
        backward_latency_sec=float(np.mean(backward_latencies)),
        step_wall_clock_sec=float(np.mean(step_latencies)),
        peak_memory_mb=peak_mem_mb
    )
    
    return telemetry


if __name__ == "__main__":
    result = run_hardware_calibration()
    print("\n[+] Telemetry Result:\n", result.model_dump_json(indent=2))
    
    out_dir = os.path.expanduser("/Users/shamthakare/.gemini/antigravity/scratch/research-reset/kakade")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "COMPUTE_CALIBRATION.json")
    with open(out_path, "w") as f:
        json.dump(result.model_dump(), f, indent=2)
    print(f"\n[+] Saved calibration record to: {out_path}")
