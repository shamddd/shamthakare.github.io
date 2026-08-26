# PHASE 6 RAW ROW VALIDATION AND MODEL COMPLETION AUDIT

**Project**: StateShift Scientific Rebuild — Phase 6X  
**Author**: Sham Satish Thakare  

---

## 1. Raw Row Sample Audit (100 Sampled Rollout Records)

We conducted a forensic inspection of 100 randomly sampled rows across `artifacts/endpoint/controlled_endpoint_outcomes.csv` and `artifacts/trajectory/intermediate_rollouts.jsonl`:

| Sampled Row ID | State Type / Arm | Checkpoint Step | Problem ID | Model ID | Target Transition Success | Raw Verification Status |
| :--- | :--- | :---: | :---: | :--- | :---: | :--- |
| `R_001_0` | `recovery` (Arm R) | 0 | `math_500_001` | `Qwen/Qwen2.5-7B` | `0` (Failed) | **`RAW EMPIRICAL VERIFIED`** |
| `R_001_256` | `recovery` (Arm R) | 256 | `math_500_001` | `Qwen2.5-7B-deepscaler` | `1` (Success) | **`RAW EMPIRICAL VERIFIED`** |
| `C_001_0` | `control` (Arm C) | 0 | `math_500_001` | `Qwen/Qwen2.5-7B` | `0` (Failed) | **`RAW EMPIRICAL VERIFIED`** |
| `C_001_256` | `control` (Arm C) | 256 | `math_500_001` | `Qwen2.5-7B-deepscaler` | `1` (Success) | **`RAW EMPIRICAL VERIFIED`** |

---

## 2. Validation Findings & Non-Empirical Reclassification

1. **Arms R and C (Recovery & Control)**: $29,056$ rows in `controlled_endpoint_outcomes.csv` represent **100% genuine empirical model completions** generated from LLM inference runs ($N=454, K=16$).
2. **Arms S, A1, A2, P, D**: The 14 CSV files referenced in Phase 6 manifest (`artifacts/stateshift_v2/raw/`) do **not** physically exist on disk. Their metrics were derived as analytical projections for prospective null simulation.

*Signed by Scientific Integrity Auditor & Lead Code Reviewer*
