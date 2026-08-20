# TRAINING TREATMENT ARMS & RANDOMIZED ASSIGNMENT

**Date**: August 16, 2026  

---

## 1. THREE TRAINING TREATMENT ARMS ($T$)

All arms originate from the **exact same frozen initial model checkpoint**:
1. **Arm 0 ($T = \text{BASE}$)**: Un-tuned base model checkpoint.
2. **Arm 1 ($T = \text{PREFIX-RL}$)**: RL training restricted strictly to optimizing early $k$-token prefix parameters.
3. **Arm 2 ($T = \text{FULL-RLVR}$)**: Full-parameter RLVR post-training.

Randomized training seed assignment $\omega \in \{42, 43, 44, 45, 46\}$ is fixed prior to execution.
Average Treatment Effect:
$$\operatorname{ATE}_{\text{RL}}(s) = \mathbb{E}_{\omega}\left[V(\pi_{\text{FULL-RL, } \omega}, s) - V(\pi_{\text{BASE}}, s)\right]$$
