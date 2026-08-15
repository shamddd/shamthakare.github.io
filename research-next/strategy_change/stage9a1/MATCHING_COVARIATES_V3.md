# MATCHING COVARIATES V3 SPECIFICATION

**Date**: August 16, 2026  

---

## 1. EXPANDED MATCHING COVARIATES

Every recovery state ($S_R$) is paired with a control state ($S_C$) matched on 8 explicit covariates:

1. `source_problem_id`: Exact same problem ID.
2. `step_depth` ($t$): Identical step depth in reasoning chain.
3. `remaining_solution_length`: Identical number of steps to final answer.
4. `observation_token_length`: $|\text{SMD}| \le 0.10$.
5. `verifier_branch_factor`: Equal number of valid next-step transitions.
6. `error_type_category`: Matched difficulty category (arithmetic vs algebraic vs logic).
7. `state_entropy`: Matched action-space entropy.
8. `new_info_required`: Matched boolean indicator whether continuation requires introducing new problem constants.
