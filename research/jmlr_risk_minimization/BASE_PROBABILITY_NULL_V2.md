# BASE-PROBABILITY NULL MECHANISM ANALYSIS (V2)

**Date**: August 16, 2026  
**Auditor**: Lead Forensic Auditor  

---

## 1. REVISION OF CAUSAL ATTRIBUTION OVER-CLAIMS

> **Correction Notice**: The previous draft converted the residual shift percentage ($52.2\%$) directly into a causal attribution statement ("proving RLVR sample efficiency gains"). This is **NOT** mathematically justified.

### Corrected Framing:
*"The specified base-probability-only null predicts part, but not all, of the observed frontier shift; the remaining discrepancy may arise from trained-policy utility, generation length, verifier cost, dependence structure, finite Best-of-N truncation ($N \le 32$), or other factors."*

---

## 2. TEN-FACTOR CONTEXTUAL AUDIT OF THE BASE NULL

1. **Independent Bernoulli Assumption**: Best-of-$N$ assumes independent trials ($1 - (1-p)^N$). In practice, candidate generations from an LLM are correlated due to prefix sharing.
2. **Heterogeneous Per-Example $p(x)$**: Base probability $p$ is not constant across queries; Jensen's inequality implies $E[1 - (1-p(x))^N] 
eq 1 - (1 - E[p(x)])^N$.
3. **Finite $N \le 32$ Truncation**: Best-of-$N$ utility saturates at $N=32$ in our evaluation grid.
4. **Verifier Cost Scaling**: Verifier FLOPs scale linearly with candidate sequence length.
5. **Generation Length Inflation**: RLVR trained policies generate sequences ~15% longer than base greedy models.
6. **Policy Generation Cost**: LoRA-RLVR adds adapter forward overhead ($+0.2\%$).
7. **Stochasticity & Temperature**: Best-of-$N$ temperature ($T=0.7$) degrades precision relative to greedy decoding.
8. **Verifier Pass Rate Variance**: Verifier false positives increase on OOD length tasks.
9. **Target Utility Threshold $u$**: Shift sensitivity varies with $u \in [0.5, 0.9]$.
10. **Pass@$N$ vs Utility Mapping**: Utility requires exact correct solution, not merely partial credit.
