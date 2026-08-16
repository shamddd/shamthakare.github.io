"""
Base evaluation diagnostics module for PRELUDE v1.
Calculates base pass@1, prompt NLL, mean token entropy, and parameter scale.
"""

from typing import List, Dict, Any, Tuple
import torch
import numpy as np
from transformers import PreTrainedModel, PreTrainedTokenizer
from ..verifiers.math_verifier import verify_reasoning_rollout


def compute_prompt_nll_and_entropy(model: PreTrainedModel, 
                                   tokenizer: PreTrainedTokenizer, 
                                   prompts: List[str], 
                                   device: torch.device) -> Tuple[float, float]:
    """
    Computes average prompt negative log-likelihood (NLL) and mean token entropy across prompts.
    """
    model.eval()
    total_nll = 0.0
    total_entropy = 0.0
    total_tokens = 0
    
    with torch.no_grad():
        for prompt in prompts:
            inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512).to(device)
            input_ids = inputs["input_ids"]
            
            outputs = model(**inputs)
            logits = outputs.logits[:, :-1, :]  # Shift for autoregressive loss
            labels = input_ids[:, 1:]
            
            # Cross-entropy NLL
            loss_fn = torch.nn.CrossEntropyLoss(reduction="sum")
            nll = loss_fn(logits.view(-1, logits.size(-1)), labels.view(-1)).item()
            
            # Entropy: H = - sum p log p
            probs = torch.softmax(logits, dim=-1)
            log_probs = torch.log_softmax(logits, dim=-1)
            entropy = -(probs * log_probs).sum(dim=-1).sum().item()
            
            num_toks = labels.size(1)
            total_nll += nll
            total_entropy += entropy
            total_tokens += num_toks
            
    mean_nll = (total_nll / total_tokens) if total_tokens > 0 else 0.0
    mean_entropy = (total_entropy / total_tokens) if total_tokens > 0 else 0.0
    return float(mean_nll), float(mean_entropy)


def evaluate_base_pass_rates(model: PreTrainedModel, 
                             tokenizer: PreTrainedTokenizer, 
                             dataset: List[Dict[str, str]], 
                             device: torch.device, 
                             max_samples: int = 100, 
                             k_rollouts: int = 8,
                             max_new_tokens: int = 256) -> Dict[str, float]:
    """
    Evaluates greedy pass@1 and sampled pass@k on target dataset.
    """
    model.eval()
    samples = dataset[:max_samples]
    correct_greedy = 0
    correct_at_k = 0
    
    for item in samples:
        prompt = f"Question: {item['question']}\nLet's solve this step-by-step:\n"
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        
        # 1. Greedy Pass@1
        with torch.no_grad():
            out_greedy = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=False, pad_token_id=tokenizer.eos_token_id)
            text_greedy = tokenizer.decode(out_greedy[0][inputs["input_ids"].size(1):], skip_special_tokens=True)
            r_greedy, _, _ = verify_reasoning_rollout(text_greedy, item["answer"])
            correct_greedy += r_greedy
            
        # 2. Sampled Pass@k
        with torch.no_grad():
            out_sampled = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=True, temperature=0.7, top_p=0.95, num_return_sequences=k_rollouts, pad_token_id=tokenizer.eos_token_id)
            k_correct = 0
            for seq in out_sampled:
                text_samp = tokenizer.decode(seq[inputs["input_ids"].size(1):], skip_special_tokens=True)
                r_samp, _, _ = verify_reasoning_rollout(text_samp, item["answer"])
                if r_samp == 1:
                    k_correct += 1
            if k_correct > 0:
                correct_at_k += 1
                
    num = len(samples)
    return {
        "pass_at_1": (correct_greedy / num) if num > 0 else 0.0,
        "pass_at_k": (correct_at_k / num) if num > 0 else 0.0,
        "num_evaluated": num
    }
