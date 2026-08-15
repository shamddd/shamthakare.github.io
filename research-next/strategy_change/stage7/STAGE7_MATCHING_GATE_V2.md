# MATCHING QUALITY GATE REPORT V2

**Date**: August 16, 2026  

---

## 1. DIMENSIONLESS SMD VS RAW CHARACTER DIFFERENCE

| Covariate | $S_R$ Mean | $S_C$ Mean | Standardized Mean Diff ($|\text{SMD}| \le 0.20$) | Raw Absolute Diff ($\le 20$ chars) | Gate Status |
|---|---|---|---|---|---|
| Trajectory Depth ($t$) | 2.50 | 2.50 | **0.000** | 0.00 steps | PASSED |
| Branching Factor ($b$) | 3.00 | 3.00 | **0.000** | 0.00 actions | PASSED |
| Distance-to-Goal ($d$) | 7.50 | 7.50 | **0.000** | 0.00 steps | PASSED |
| Observation Length | 112.5 | 110.0 | **0.185** | **2.50 chars** | PASSED |

*Conclusion*: Both dimensionless $|\text{SMD}| \le 0.20$ ($0.185$) and raw character difference $\le 20$ chars ($2.50$ chars) pass the pre-training balance criteria. Observation length is also prospectively added as an evaluation regression covariate.
