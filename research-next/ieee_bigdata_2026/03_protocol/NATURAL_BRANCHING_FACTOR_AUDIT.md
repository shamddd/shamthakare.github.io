# NATURAL BRANCHING FACTOR AUDIT REPORT

**Date**: August 16, 2026  

---

## 1. AUDIT FINDINGS

For linear mathematical reasoning benchmarks (GSM8K reference CoT traces), every reference step has exactly 1 valid forward continuation path ($b_i = 1.0$).
* **Classification**: `CONSTRUCTOR_DERIVED` (constant $1.0$ across linear reference chains).
* **Sample Standard Deviation**: $s_{\text{branching}} = 0.0$.
* **Zero-Variance Rule Action**: Under our strict matching distance specification ($s_k = 0$), `branching_factor` is automatically excluded from the distance metric for linear CoT benchmarks, and remaining active continuous weights are renormalized to $1/3 \approx 0.3333$.
