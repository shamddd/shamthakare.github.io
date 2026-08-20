# PROBLEM-BLOCKED BOOTSTRAP ALGORITHM LOCK

**Resampling Protocol**: Problem-Level Hierarchical Block Bootstrap  
**Bootstrap Replicates**: $B = 10,000$  
**Unit of Resampling**: Independent Problem ID $i \in \{1, \dots, N\}$ ($N=365$)  

---

## 1. Algorithm Pseudocode

```python
def problem_blocked_bootstrap(pair_registry, B=10000, alpha=0.05, seed=42):
    np.random.seed(seed)
    N = len(pair_registry)
    problem_ids = [p["problem_id"] for p in pair_registry]
    
    bootstrap_gamma_T = []
    
    for b in range(B):
        # Sample problem IDs WITH REPLACEMENT
        sampled_indices = np.random.choice(N, size=N, replace=True)
        
        gamma_sample = []
        for idx in sampled_indices:
            # Carry together ALL states, rollouts, and checkpoints for problem idx
            gamma_i_T = compute_problem_interaction(pair_registry[idx], T=256)
            gamma_sample.append(gamma_i_T)
            
        Gamma_T_b = np.mean(gamma_sample)
        bootstrap_gamma_T.append(Gamma_T_b)
        
    ci_lower = np.percentile(bootstrap_gamma_T, 100 * (alpha / 2))
    ci_upper = np.percentile(bootstrap_gamma_T, 100 * (1 - alpha / 2))
    
    return np.mean(bootstrap_gamma_T), (ci_lower, ci_upper)
```

---

## 2. Invariance Rules

1. **Do NOT independently resample rollouts**: All $K=16$ rollouts for state $S_C$ and $S_R$ across all checkpoints $t$ are linked to problem $i$ and resampled together.
2. **Preserve Within-Problem Covariance**: Blocked sampling preserves baseline-to-checkpoint covariance structures.

---
