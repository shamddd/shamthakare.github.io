# MATCHING PROTOCOL SPECIFICATION (V3)

**Date**: August 16, 2026  

---

## 1. COVARIATE SELECTION & JUSTIFICATION

We lock **7 prospective structural covariates** for matching recovery states $S_R$ to control states $S_C$:
1. `trajectory_depth` (continuous, caliper $\le 1.0$ step)
2. `remaining_solution_length` (continuous, caliper $\le 2.0$ steps)
3. `token_length` (continuous, caliper $\le 20$ tokens)
4. `branching_factor` (continuous, caliper $\le 1.0$)
5. `error_category` (categorical, exact match)
6. `problem_difficulty` (categorical, exact match)
7. `verifier_state` (categorical, exact match)

Matching occurs prospectively **BEFORE** model treatment rollouts are evaluated.
