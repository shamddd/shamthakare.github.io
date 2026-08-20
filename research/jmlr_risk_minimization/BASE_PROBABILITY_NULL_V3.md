# BASE-PROBABILITY NULL MECHANISM ANALYSIS (V3) — MATHEMATICAL CORRECTION

**Date**: August 16, 2026  
**Auditor**: Lead Mathematical & Statistical Auditor  

---

## 1. OFFICIAL RETRACTION OF THE INVALID 47.8% / 52.2% RATIO DECOMPOSITION

> **MATHEMATICAL RETRACTION NOTICE**: The previous calculation R_obs / R_null = 0.0618 / 0.1292 = 0.478 was **INCORRECTLY INTERPRETED** as *"47.8% explained, 52.2% residual"*. Dividing two ratios does **NOT** measure fraction of shift explained. All claims attributing 52.2% of the shift to RLVR generalization are **OFFICIALLY RETRACTED**.

---

## 2. FORMAL DECOMPOSITION ESTIMANDS

We evaluate the fraction of break-even horizon shift predicted by the base-probability null across two mathematically defensible estimands:

### Estimand A: Linear Contraction from Null Horizon ($R=1.0$)
* **Observed Horizon Contraction**: $\Delta_{\text{obs}} = 1.0 - R_{\text{obs}} = 1.0 - 0.0618 = 0.9382$
* **Null-Predicted Horizon Contraction**: $\Delta_{\text{null}} = 1.0 - R_{\text{null}} = 1.0 - 0.1292 = 0.8708$
* **Fraction Explained ($E_{\text{linear}}$)**: **`92.82%`** (Residual = `7.18%`)

### Estimand B: Log-Ratio Contraction
* **Observed Log Contraction**: $|\ln R_{\text{obs}}| = |\ln 0.0618| = 2.7838$
* **Null-Predicted Log Contraction**: $|\ln R_{\text{null}}| = |\ln 0.1292| = 2.0464$
* **Fraction Explained ($E_{\text{log}}$)**: **`73.51%`** (Residual = `26.49%`)

---

## 3. CORE SCIENTIFIC RE-INTERPRETATION

> **KEY FINDING**: Base-policy competence deterioration ($p(d_{\text{IID}}) = 0.21 \to p(d_{\text{OOD}}) = 0.03$) predicts **73.5% to 92.8%** of the observed deployment-frontier shift. 

The primary driver of the break-even horizon contraction is the rapid explosion of Best-of-$N$ search costs as base accuracy collapses under distribution shift, rather than an extraordinary RLVR generalization dynamic.
