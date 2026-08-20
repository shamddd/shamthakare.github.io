# NATURAL RECOVERY ORIGIN AUDIT V2

**Date**: August 16, 2026  

---

## 1. STRICT CLASS 1 ORIGIN REQUIREMENT

Every recovery state record ($S_R$) requires explicit immutable provenance:
`source_dataset`, `source_revision`, `source_split`, `source_item_id`, `source_problem_sha256`, `source_trajectory_origin`, `source_trajectory_sha256`, `error_step_index`, `verifier_evidence`, `corrective_step`, `human_or_model_generated`.

* **Class 1 (Naturally Occurring Verifier-Identifiable Failure States)**:
  - Must originate from an immutable real recorded trajectory (e.g. human error step in GSM8K solution log or model error log) with verifiable SHA-256 hash.
  - **Count**: 20 items (10 Math, 10 Code).
* **Class 2 (Controlled Injected Failure States)**:
  - Any state lacking an immutable real trajectory is strictly downgraded to Class 2.
  - **Count**: 10 items (5 Math, 5 Code).

> **GOVERNANCE RULE**: Primary external validity claims are driven exclusively by Class 1. Class 2 serves as a positive control.
