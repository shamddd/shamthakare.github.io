# FIVE ARMS AND FULL-SFT BASELINE SPECIFICATION

**Date**: August 16, 2026  

---

## 1. FIVE PREREGISTERED TREATMENT ARMS

To isolate RL-specific policy behavior from complete-trajectory SFT and recovery exposure, 5 arms originate from the exact same initial checkpoint:

1. **Arm 0 ($T = \text{BASE}$)**: Base model checkpoint.
2. **Arm 1 ($T = \text{PREFIXRL}$)**: Prefix-conditioned RL baseline.
3. **Arm 2 ($T = \text{RECOVERY-SFT}$)**: SFT on recovery-only state demonstrations.
4. **Arm 3 ($T = \text{FULL-SFT}$)**: SFT on complete trajectories (matched for total training tokens/examples).
5. **Arm 4 ($T = \text{FULL-RLVR}$)**: Full-parameter on-policy RLVR.

---

## 2. KEY MECHANISTIC CONTRASTS

* $C_1 = \Delta_{\text{late}}(\text{FULL-RLVR} - \text{PREFIXRL})$ (Late-state behavior change vs prefix restriction)
* $C_2 = \Delta_{\text{late}}(\text{FULL-RLVR} - \text{RECOVERY-SFT})$ (RL policy flexibility vs SFT recovery exposure)
* $C_4 = \Delta_{\text{late}}(\text{FULL-RLVR} - \text{FULL-SFT})$ (RL optimization benefit vs Complete-Trajectory SFT)
