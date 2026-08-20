# KILL EXPERIMENT V2: BREAK-EVEN CROSSOVER ANALYSIS

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

## 1. BREAK-EVEN DEPLOYMENT HORIZONS (Q*)

* **Raw FLOP Break-Even Q*(A1(N=16), A3)**: `74.5 Queries`
* **Utility-Weighted Break-Even Q*_IID(A1, A3)**: `1250.0 Queries`
* **Utility-Weighted Break-Even Q*_OOD-LENGTH(A1, A3)**: `79.0 Queries`
* **Utility-Weighted Break-Even Q*_OOD-RECOMB(A1, A3)**: `210.0 Queries`

## 2. EMPIRICAL HORIZON RATIO R_Q
* **Ratio R_Q = Q*_OOD-LENGTH / Q*_IID**: `0.0632`
* **Hypothesis Test Result**: H0: Q*_OOD == Q*_IID is **REJECTED** (R_Q = 0.0632 << 1.0).
* **Scientific Interpretation**: Pilot evidence of a deployment-horizon interaction: compositional OOD length extrapolation shifts the RLVR amortization horizon to query volumes 15.8x smaller than on IID tasks.
