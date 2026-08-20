# MATCHING COVARIATE IDENTIFICATION AUDIT REPORT

**Date**: August 16, 2026  

---

## 1. COVARIATE CLASSIFICATION AUDIT

We audit all candidate matching variables to prevent **group-definition contamination** (matching on variables that definitionally separate recovery states from controls).

| Candidate Covariate | Classification | Status | Rationale |
| :--- | :--- | :---: | :--- |
| `trajectory_depth` | **PRE-GROUP STRUCTURAL** | **RETAINED** | Pre-transition trajectory step index. |
| `remaining_solution_length` | **PRE-GROUP STRUCTURAL** | **RETAINED** | Reference steps remaining to complete problem. |
| `token_length` | **PRE-GROUP STRUCTURAL** | **RETAINED** | Exact token count of state prefix. |
| `branching_factor` | **PRE-GROUP STRUCTURAL** | **RETAINED** | Step graph node out-degree. |
| `reasoning_operation_type` | **PRE-GROUP STRUCTURAL** | **RETAINED** | Operational step category (e.g. `arithmetic_addition`, `algebraic_substitution`). |
| `problem_difficulty` | **PRE-GROUP STRUCTURAL** | **RETAINED** | Derived prospectively from reference solution step count. |
| `error_category` | **GROUP-DEFINING** | **REMOVED** | Definitionally `none` for controls and non-`none` for recovery states. Matching on it forces a collider artifact. |
| `verifier_state` | **GROUP-DEFINING** | **REMOVED** | Definitionally `VALID` for controls and `INVALID` for recovery states. |

$$\boxed{\textbf{FINAL MATCHING COVARIATE SET: 6 PRE-GROUP STRUCTURAL VARIABLES}}$$
