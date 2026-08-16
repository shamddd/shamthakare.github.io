"""
Representation geometry and linear reward probe diagnostics for PRELUDE v1.
Computes residual stream effective rank, stable rank, singular value spectra, and probe AUROC.
"""

from typing import List, Dict, Any, Tuple, Optional
import torch
import numpy as np
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.metrics import roc_auc_score, r2_score
from transformers import PreTrainedModel, PreTrainedTokenizer
from ..verifiers.math_verifier import verify_reasoning_rollout


def compute_matrix_spectral_metrics(activations: np.ndarray) -> Dict[str, float]:
    """
    Computes effective rank, stable rank, and spectral properties of activation matrix H in R^{N x d}.
    """
    N, d = activations.shape
    if N < 2 or d < 2:
        return {
            "effective_rank": 1.0,
            "stable_rank": 1.0,
            "top_singular_value_ratio": 1.0,
            "subspace_condition_number": 1.0
        }
        
    # Center activations
    H_centered = activations - np.mean(activations, axis=0, keepdims=True)
    
    # Singular values of centered activations
    # SVD on min(N, d)
    try:
        _, S, _ = np.linalg.svd(H_centered, full_matrices=False)
    except np.linalg.LinAlgError:
        # Fallback to eigenvalue decomposition of covariance
        cov = (H_centered.T @ H_centered) / max(1, N - 1)
        eigvals = np.maximum(0.0, np.linalg.eigvalsh(cov))
        S = np.sqrt(np.sort(eigvals)[::-1])
        
    # Filter tiny singular values
    S_pos = S[S > 1e-7]
    if len(S_pos) == 0:
        return {
            "effective_rank": 1.0,
            "stable_rank": 1.0,
            "top_singular_value_ratio": 1.0,
            "subspace_condition_number": 1.0
        }
        
    # Normalized spectral distribution p_i = sigma_i / sum(sigma)
    p = S_pos / np.sum(S_pos)
    
    # Effective Rank: erank = exp(-sum p_i ln p_i)
    entropy = -np.sum(p * np.log(p + 1e-12))
    erank = float(np.exp(entropy))
    
    # Stable Rank: srank = sum(sigma_i^2) / sigma_1^2
    srank = float(np.sum(S_pos**2) / (S_pos[0]**2 + 1e-12))
    
    top_ratio = float(S_pos[0] / np.sum(S_pos))
    k = min(len(S_pos), 10)
    cond_k = float(S_pos[0] / (S_pos[k - 1] + 1e-12))
    
    return {
        "effective_rank": erank,
        "stable_rank": srank,
        "top_singular_value_ratio": top_ratio,
        "subspace_condition_number": cond_k
    }


def extract_rollout_activations_and_probe(model: PreTrainedModel,
                                         tokenizer: PreTrainedTokenizer,
                                         dataset: List[Dict[str, str]],
                                         device: torch.device,
                                         num_prompts: int = 30,
                                         k_rollouts: int = 6,
                                         max_new_tokens: int = 192) -> Dict[str, float]:
    """
    Extracts residual stream representations from generated rollouts, computes spectral geometry,
    and trains a linear reward probe to measure AUROC and separability.
    """
    model.eval()
    prompts_data = dataset[:num_prompts]
    
    collected_vectors: List[np.ndarray] = []
    collected_rewards: List[int] = []
    
    for item in prompts_data:
        prompt = f"Question: {item['question']}\nLet's solve this step-by-step:\n"
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        
        with torch.no_grad():
            gen_out = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=True,
                temperature=0.7,
                top_p=0.95,
                num_return_sequences=k_rollouts,
                output_hidden_states=True,
                return_dict_in_generate=True,
                pad_token_id=tokenizer.eos_token_id
            )
            
        sequences = gen_out.sequences
        prompt_len = inputs["input_ids"].size(1)
        
        # Extract hidden states from forward pass of generated sequences
        with torch.no_grad():
            fwd_out = model(sequences, output_hidden_states=True)
            # Use last hidden state of final token in sequence
            hidden_states = fwd_out.hidden_states[-1]  # shape: (B, SeqLen, d_model)
            final_token_vecs = hidden_states[:, -1, :].cpu().to(torch.float32).numpy()
            
        for idx, seq in enumerate(sequences):
            gen_text = tokenizer.decode(seq[prompt_len:], skip_special_tokens=True)
            r, _, _ = verify_reasoning_rollout(gen_text, item["answer"])
            collected_vectors.append(final_token_vecs[idx])
            collected_rewards.append(r)
            
    X = np.array(collected_vectors)  # (N_total, d_model)
    y = np.array(collected_rewards)  # (N_total,)
    
    # 1. Compute spectral metrics on representation manifold
    spectral_metrics = compute_matrix_spectral_metrics(X)
    
    # 2. Compute Linear Probe Separability
    num_pos = np.sum(y == 1)
    num_neg = np.sum(y == 0)
    
    if num_pos >= 2 and num_neg >= 2:
        # Both classes exist -> train linear probe
        clf = LogisticRegression(C=1.0, max_iter=200, penalty="l2")
        try:
            clf.fit(X, y)
            probs = clf.predict_proba(X)[:, 1]
            probe_auroc = float(roc_auc_score(y, probs))
            probe_r2 = float(r2_score(y, probs))
        except Exception:
            probe_auroc = 0.50
            probe_r2 = 0.0
    else:
        # Trivial support (all 0 or all 1)
        probe_auroc = 0.50
        probe_r2 = 0.0
        
    return {
        "residual_effective_rank": spectral_metrics["effective_rank"],
        "residual_stable_rank": spectral_metrics["stable_rank"],
        "top_singular_value_ratio": spectral_metrics["top_singular_value_ratio"],
        "subspace_condition_number": spectral_metrics["subspace_condition_number"],
        "reward_probe_auroc": probe_auroc,
        "reward_probe_r2": probe_r2,
        "total_probe_samples": len(y)
    }
