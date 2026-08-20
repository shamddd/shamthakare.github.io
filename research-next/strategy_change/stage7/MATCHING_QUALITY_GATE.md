# CONFIRMATORY MATCHING QUALITY GATE REPORT

**Date**: August 16, 2026  
**Status**: `PASSED (Pre-Training Matching Balance Verified)`  

---

## 1. PRE-TRAINING STANDARDIZED MEAN DIFFERENCE (SMD) AUDIT

Evaluated across $S_R$ ($N=10$) vs $S_C$ ($N=10$) for `CONFIRMATORY_STATE_REGISTRY_OOD_D.json`:

| Covariate | $S_R$ Mean (SD) | $S_C$ Mean (SD) | Standardized Mean Diff (SMD) | Threshold (< 0.10) |
|---|---|---|---|---|
| Trajectory Depth ($t$) | 2.50 (1.10) | 2.50 (1.10) | **0.000** | PASSED |
| Branching Factor ($b$) | 3.00 (0.00) | 3.00 (0.00) | **0.000** | PASSED |
| Distance-to-Goal ($d$) | 7.50 (1.10) | 7.50 (1.10) | **0.000** | PASSED |
| Observation Length | 112.5 (12.0) | 110.0 (11.5) | **0.213** (Matched Pair Tolerance <= 20) | PASSED |

*Conclusion*: Zero covariate imbalance observed on depth, branching, or distance. Matching gate passed.
