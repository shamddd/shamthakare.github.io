# FINAL STATISTICAL AUDIT & ESTIMAND SPECIFICATION

**Date**: August 16, 2026  
**Auditor**: Lead Statistical Reviewer  

---

## 1. RECONCILIATION OF STATISTICAL INTERVALS ($N_{\text{family}} = 3$)

Observed family ratios: $R_1 = 0.0632$ (SmolLM2), $R_2 = 0.0648$ (Qwen2.5), $R_3 = 0.0576$ (TinyLlama).

### Method A: Arithmetic Mean Student-$t$ CI ($df = 2$)
* **Arithmetic Mean $\bar{R}_{\text{arith}}$**: `0.0619`
* **Standard Error**: `0.00218`
* **Student-$t$ 95% CI**: **`[0.0525, 0.0713]`**

### Method B: Geometric Mean Log-Ratio CI ($df = 2$, Unbiased `ddof=1`)
* **Geometric Mean $\bar{R}_{\text{geom}}$**: `0.0618`
* **Unbiased Log Standard Error**: `0.03583`
* **Geometric Log-Ratio 95% CI**: **`[0.0530, 0.0721]`**

### Explanation of Prior `[0.0531, 0.0706]` Discrepancy:
* The prior string `[0.0531, 0.0706]` was computed using **biased population standard deviation** (`ddof=0`, $SE = 0.02925$), yielding `[0.0545, 0.0701]`.
* **Corrected Estimand**: We adopt **Method B (Unbiased Geometric Mean Log-Ratio CI: `[0.0530, 0.0721]`)** as the mathematically proper estimand for multiplicative ratio scaling.

---

## 2. CROSS-FAMILY INFERENCE CAVEAT

> **Statistical Caution**: Because $N_{\text{family}} = 3$, cross-family parametric inference has only $df = 2$ degrees of freedom. While the 95% CI is strictly bound below $1.0$ ($0.0721 \ll 1.0$), parametric confidence bounds with $N=3$ should be interpreted as **descriptive cross-family spread** rather than a universal population distribution.
