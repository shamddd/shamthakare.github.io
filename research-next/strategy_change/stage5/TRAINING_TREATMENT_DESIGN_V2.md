# TRAINING TREATMENT DESIGN V2

**Date**: August 16, 2026  

---

## 1. REPAIRED PREFIXRL TREATMENT SPECIFICATION

All training arms originate from the **exact same frozen initial checkpoint revision**:

1. **Arm 0 ($T = \text{BASE}$)**: Un-tuned base model checkpoint.
2. **Arm 1 ($T = \text{PREFIXRL}$)**:
   - Implements the exact PrefixRL principle (Setlur et al. 2026 / Rocha Filho et al. 2026).
   - Obtains fixed off-policy strategy prefixes $h_k$.
   - Conditions training episodes on those fixed prefixes.
   - Performs on-policy RL on the continuation trajectory.
   - Preserves identical base checkpoint and matched RL token budget.
3. **Arm 2 ($T = \text{FULL-RLVR}$)**: Full-parameter on-policy RLVR post-training across full trajectories.

---

## 2. REPAIRED ESTIMAND TERMINOLOGY

> **Terminology Correction**: We do not use the term "Average Treatment Effect (ATE)". We define:
> *"Average randomized-training contrast conditional on the fixed starting checkpoint across randomized training seeds $\omega \in \{42, 43, 44, 45, 46\}$."*
