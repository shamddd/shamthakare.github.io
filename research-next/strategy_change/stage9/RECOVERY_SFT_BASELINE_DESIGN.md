# RECOVERY-SFT SECONDARY BASELINE DESIGN

**Date**: August 16, 2026  

---

## 1. FOUR TREATMENT ARMS

All arms originate from the exact same frozen base checkpoint:
1. **Arm 0 ($T = \text{BASE}$)**: Base model checkpoint.
2. **Arm 1 ($T = \text{PREFIXRL}$)**: Prefix-conditioned RL baseline.
3. **Arm 2 ($T = \text{RECOVERY-SFT}$)**: Supervised Fine-Tuning on recovery demonstrations (isolates SFT demonstration from RL policy flexibility).
4. **Arm 3 ($T = \text{FULL-RLVR}$)**: Full-parameter on-policy RLVR.
