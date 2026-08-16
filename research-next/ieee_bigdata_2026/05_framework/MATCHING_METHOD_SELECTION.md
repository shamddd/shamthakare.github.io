# MATCHING METHOD SELECTION REPORT

**Date**: August 16, 2026  

---

## 1. COMPARISON OF CANDIDATE MATCHING METHODS

* **Method A (Exact Categorical + Hard Calipers + Standardized Weighted Absolute Distance)**:
  - Pros: 100% deterministic, robust under small N, zero covariance singularity risk, easily interpretable.
  - Cons: Requires pre-specified calipers.
* **Method B (Mahalanobis Distance with Shrinkage)**:
  - Pros: Accounts for continuous covariate covariance structure.
  - Cons: Sensitive to sample size $N < 50$, potential matrix inversion instability.

## 2. SELECTION VERDICT

$$\boxed{\textbf{SELECTED: METHOD A (EXACT CATEGORICAL + HARD CALIPERS + WEIGHTED ABSOLUTE DISTANCE)}}$$
* Matching occurs prospectively **BEFORE** model treatment continuations are generated.
