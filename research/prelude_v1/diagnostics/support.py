"""
Sampled solution coverage and support diagnostics module for PRELUDE v1.
Calculates empirical success coverage p_hat_K and group-wise advantage variance.
"""

from typing import List, Dict, Any, Tuple
import torch
import numpy as np
from transformers import PreTrainedModel, PreTrainedTokenizer
from ..verifiers.math_verifier import verify_reasoning_rollout


def compute_sampled_solution_coverage(model: PreTrainedModel,
                                      tokenizer: PreTrainedTokenizer,
                                      dataset: List[Dict[str, str]],
                                      device: torch.device,
                                      num_prompts: int = 50,
                                      k_rollouts: int = 8,
                                      max_new_tokens: int = 256) -> Dict[str, float]:
    """
    Computes empirical success coverage:
        p_hat_K = (1 / nK) sum_{i=1}^n sum_{j=1}^K I[r(x_i, y_ij) == 1]
    Also measures the fraction of prompts with non-zero reward variance (where GRPO advantage is non-vanishing).
    """
    model.eval()
    prompts_data = dataset[:num_prompts]
    total_rollouts = 0
    total_successes = 0
    prompts_with_at_least_one_success = 0
    group_variances: List[float] = []
    
    for item in prompts_data:
        prompt = f"Question: {item['question']}\nLet's solve this step-by-step:\n"
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=True,
                temperature=0.7,
                top_p=0.95,
                num_return_sequences=k_rollouts,
                pad_token_id=tokenizer.eos_token_id
            )
            
        rewards = []
        for seq in outputs:
            gen_text = tokenizer.decode(seq[inputs["input_ids"].size(1):], skip_special_tokens=True)
            r, _, _ = verify_reasoning_rollout(gen_text, item["answer"])
            rewards.append(r)
            total_successes += r
            total_rollouts += 1
            
        if any(r == 1 for r in rewards):
            prompts_with_at_least_one_success += 1
            
        # Group reward variance: if var == 0, GRPO relative advantage vanishes
        var_r = float(np.var(rewards))
        group_variances.append(var_r)
        
    p_hat_K = (total_successes / total_rollouts) if total_rollouts > 0 else 0.0
    support_coverage = (prompts_with_at_least_one_success / len(prompts_data)) if prompts_data else 0.0
    mean_group_variance = float(np.mean(group_variances)) if group_variances else 0.0
    vanishing_gradient_ratio = float(np.mean([1.0 if v == 0.0 else 0.0 for v in group_variances])) if group_variances else 1.0
    
    return {
        "sampled_success_rate_p_hat": p_hat_K,
        "prompt_support_coverage": support_coverage,
        "mean_group_reward_variance": mean_group_variance,
        "vanishing_advantage_prompt_ratio": vanishing_gradient_ratio,
        "total_rollouts_evaluated": total_rollouts
    }
