"""
Gradient saliency, variance, and LayerNorm projection diagnostics for PRELUDE v1.
Computes gradient norm, Gradient Noise Scale (GNS), and layerwise gradient ratios on micro-batches.
"""

from typing import List, Dict, Any, Tuple
import torch
import numpy as np
from transformers import PreTrainedModel, PreTrainedTokenizer


def compute_gradient_saliency_and_gns(model: PreTrainedModel,
                                      tokenizer: PreTrainedTokenizer,
                                      dataset: List[Dict[str, str]],
                                      device: torch.device,
                                      microbatch_size: int = 4,
                                      num_microbatches: int = 5) -> Dict[str, float]:
    """
    Evaluates gradient norms across distinct microbatches to calculate:
    1. Average gradient norm ||g||
    2. Gradient Noise Scale proxy: Var(g) / ||E[g]||^2
    3. LayerNorm vs Output un-embedding gradient magnitude ratio
    """
    model.eval()
    samples = dataset[:microbatch_size * num_microbatches]
    if len(samples) < microbatch_size:
        return {
            "microbatch_gradient_norm": 0.0,
            "gradient_noise_scale": 0.0,
            "layernorm_to_output_grad_ratio": 0.0
        }
        
    collected_layer_norms: List[float] = []
    collected_output_norms: List[float] = []
    collected_total_norms: List[float] = []
    
    # Identify target parameter groups
    layernorm_params = []
    output_head_params = []
    
    for name, param in model.named_parameters():
        if not param.requires_grad:
            continue
        if "ln" in name.lower() or "norm" in name.lower():
            layernorm_params.append(param)
        elif "lm_head" in name.lower() or "embed_out" in name.lower() or "wte" in name.lower():
            output_head_params.append(param)
            
    for mb_idx in range(num_microbatches):
        batch = samples[mb_idx * microbatch_size : (mb_idx + 1) * microbatch_size]
        if not batch:
            break
            
        prompts = [f"Question: {ex['question']}\nAnswer: {ex['answer']}" for ex in batch]
        inputs = tokenizer(prompts, return_tensors="pt", padding=True, truncation=True, max_length=256).to(device)
        
        # Zero gradients
        model.zero_grad()
        outputs = model(**inputs, labels=inputs["input_ids"])
        loss = outputs.loss
        loss.backward()
        
        # Total gradient norm
        total_norm_sq = 0.0
        for p in model.parameters():
            if p.grad is not None:
                total_norm_sq += float(p.grad.data.norm(2).item() ** 2)
        total_norm = np.sqrt(total_norm_sq)
        collected_total_norms.append(total_norm)
        
        # LayerNorm gradient norm
        ln_norm_sq = 0.0
        for p in layernorm_params:
            if p.grad is not None:
                ln_norm_sq += float(p.grad.data.norm(2).item() ** 2)
        collected_layer_norms.append(np.sqrt(ln_norm_sq))
        
        # Output head gradient norm
        out_norm_sq = 0.0
        for p in output_head_params:
            if p.grad is not None:
                out_norm_sq += float(p.grad.data.norm(2).item() ** 2)
        collected_output_norms.append(np.sqrt(out_norm_sq))
        
    model.zero_grad()
    
    mean_total_norm = float(np.mean(collected_total_norms)) if collected_total_norms else 0.0
    var_total_norm = float(np.var(collected_total_norms)) if collected_total_norms else 0.0
    
    # GNS proxy = Var(||g||) / (||E[g]||^2 + eps)
    gns_proxy = float(var_total_norm / (mean_total_norm**2 + 1e-8))
    
    mean_ln_norm = float(np.mean(collected_layer_norms)) if collected_layer_norms else 0.0
    mean_out_norm = float(np.mean(collected_output_norms)) if collected_output_norms else 0.0
    ln_to_out_ratio = float(mean_ln_norm / (mean_out_norm + 1e-8))
    
    return {
        "microbatch_gradient_norm": mean_total_norm,
        "gradient_noise_scale": gns_proxy,
        "layernorm_to_output_grad_ratio": ln_to_out_ratio
    }
