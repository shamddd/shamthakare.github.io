# FRONTIER SHIFT DECOMPOSITION & HYPOTHESIS FRAMEWORK

**Date**: August 16, 2026  

---

## THREE COMPETING HYPOTHESES FOR FRONTIER SHIFT

1. **H1 — COMPETENCE-DRIVEN FRONTIER (PRIMARY DRIVER)**: Declining base-policy success rates under distribution shift cause Best-of-$N$ search costs to explode linearly/exponentially, moving the train-vs-search frontier toward up-front training. (Explains **73.5% -- 92.8%** of shift).
2. **H2 — ADDITIONAL TRAINED-POLICY EFFECT (SECONDARY)**: RLVR post-training maintains policy accuracy on OOD tasks better than un-tuned base models, contributing a modest residual shift.
3. **H3 — COST-STRUCTURE & ACCOUNTING EFFECT**: Generation sequence length inflation, verifier cost per candidate, and finite $N \le 32$ truncation account for remaining accounting variance.
