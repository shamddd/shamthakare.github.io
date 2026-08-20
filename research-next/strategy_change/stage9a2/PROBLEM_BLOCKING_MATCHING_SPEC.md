# PROBLEM-BLOCKING MATCHING SPECIFICATION

**Date**: August 16, 2026  

---

## 1. PROBLEM-LEVEL BLOCKING STRUCTURE

`source_problem_id` is treated as a **strict blocking identifier**:
* Every recovery state ($S_R$) is paired with a control state ($S_C$) originating from the **exact same `source_problem_id`**.
* Within-problem covariate balance is enforced on: `step_depth`, `remaining_solution_length`, `observation_token_length`, `verifier_branch_factor`, `error_type_category`.
