# MATCHING DISTANCE & SENSITIVITY SPECIFICATION

**Date**: August 16, 2026  

---

## 1. STANDARDIZED ABSOLUTE DISTANCE FORMULA

After hard categorical constraints (`reasoning_operation_type`, `problem_difficulty`) and hard continuous calipers pass:

$$d(i,j) = \sum_{k=1}^4 w_k \cdot \frac{|z_{ik} - z_{jk}|}{\sigma_k}$$

where:
* $z_{\cdot k}$ are continuous covariates (`trajectory_depth`, `remaining_solution_length`, `token_length`, `branching_factor`).
* $\sigma_k$ is the sample standard deviation across candidate states in the evaluation pool.
* Weights $w_k = 0.25$ for all $k \in \{1,2,3,4\}$.

## 2. PRESPECIFIED SENSITIVITY THRESHOLDS (E6)

* **Standard Matching Threshold**: $d(i,j) \le 1.0$ standardized unit.
* **Tight Matching Threshold (E6 Sensitivity)**: $d(i,j) \le 0.5$ standardized unit.
