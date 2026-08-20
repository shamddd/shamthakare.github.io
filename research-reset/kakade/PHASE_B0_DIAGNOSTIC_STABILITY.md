# PHASE B0 DIAGNOSTIC STABILITY & COLLINEARITY REPORT

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

## 1. NUMERICAL STABILITY & CONFOUNDING ANALYSIS (AMENDMENT 10)
* Internal feature extractions succeeded on 100% of pilot checkpoints without NaN/Inf failures (K3 Passed).
* Max Collinearity $R^2$ of internal feature $I_j$ onto $(B, H)$:
  - `erank` vs $(B, H)$: $R^2 = 0.62$ (Collinearity < 0.90, K4 Passed)
  - `probe_auroc` vs $(B, H)$: $R^2 = 0.58$ (Collinearity < 0.90, K4 Passed)
  - `gns_proxy` vs $(B, H)$: $R^2 = 0.44$ (Collinearity < 0.90, K4 Passed)
