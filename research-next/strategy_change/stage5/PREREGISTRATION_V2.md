# PREREGISTRATION SPECIFICATION V2: STATE-MATCHED RECOVERY STUDY

**Date**: August 16, 2026  
**Status**: `GO — PILOT IMPLEMENTATION AUTHORIZED`  
**Preregistration Protocol Version**: `v2.0-final`  

---

## 1. APPROVED NOVELTY STATEMENT

> *"No primary-source work identified in the audited literature was found to evaluate the same preregistered recovery-specific state-matched interaction estimand."*

---

## 2. STUDY SUMMARY & PRIMARY ESTIMAND

This study evaluates whether full RLVR post-training achieves a selective value advantage over PrefixRL on recovery-critical states ($S_R$) relative to matched control states ($S_C$), across 4 factored structural OOD environments (OOD-B, OOD-D, OOD-M, OOD-C).

* **Primary Flagship Estimand**:
  $$\Delta_{\text{late}} = \mathbb{E}_{s \in S_R}\left[V_{\text{FULL}}(s) - V_{\text{PREFIX}}(s)\right] - \mathbb{E}_{s \in S_C}\left[V_{\text{FULL}}(s) - V_{\text{PREFIX}}(s)\right]$$
* **Primary Directional Hypothesis**: $\Delta_{\text{late}} > 0$.
* **Sensitivity Reporting**: Preregistered reporting at threshold values $\delta \in \{0.02, 0.05, 0.10\}$.
