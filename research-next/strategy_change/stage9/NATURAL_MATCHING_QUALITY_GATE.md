# NATURAL STATE MATCHING QUALITY GATE REPORT

**Date**: August 16, 2026  
**State Registry SHA-256**: `6c8f64032fce4db1807a4f3d147c571fed7f39ddd6ad9b22cc63dd451d665183`  

---

## 1. PRE-TRAINING NATURAL COVARIATE BALANCE AUDIT

Matched across 20 natural recovery states ($S_R$) and 20 matched natural control states ($S_C$):

| Domain | Covariate | $S_R$ Mean | $S_C$ Mean | Standardized Mean Diff ($|\text{SMD}| \le 0.20$) | Gate Status |
|---|---|---|---|---|---|
| Math | Step Depth ($t$) | 3.00 | 3.00 | **0.000** | PASSED |
| Math | Observation Tokens | 162.5 | 164.5 | **0.082** | PASSED |
| Code | Step Depth ($t$) | 4.00 | 4.00 | **0.000** | PASSED |
| Code | Observation Tokens | 202.5 | 204.5 | **0.076** | PASSED |

*Conclusion*: Both Math and Code domain state pairs pass the pre-training balance criteria ($|\text{SMD}| < 0.10$).
