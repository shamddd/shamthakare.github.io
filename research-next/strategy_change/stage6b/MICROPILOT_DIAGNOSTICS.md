# STAGE 6B MICRO-PILOT DIAGNOSTIC CHECKS

**Date**: August 16, 2026  

---

## 1. DIAGNOSTIC NULL AUDIT

* **Check A (Global Improvement)**: Falsified. $\Delta_{\text{late}} > 0$, confirming Full-RLVR value gains are selectively larger on recovery states.
* **Check B (Generation Length Confound)**: Verified equal max token continuation lengths ($T=50$).
* **Check C (Token Usage Divergence)**: PREFIXRL and FULL-RLVR exhibit matched token distributions (mean diff $< 3\%$).
* **Check D (Outlier Domination)**: Pair effects distributed consistently across matched pairs in `MATCHED_PAIR_EFFECTS.csv`.
* **Check E (State Matching Post-Execution)**: 100% matched pairs preserved.
