# PHASE 2 STAGE C0.2 — HARD MODEL-PROVENANCE REALITY CHECK REPORT

**Milestone**: Natural-Recovery Pilot Model Provenance Reality Check  
**Target Repository**: `UWNSL/Qwen2.5-7B-deepscaler_4k_step_256`  
**Execution Timestamp**: `2026-08-20 03:19 UTC`  

---

## 1. Provenance Audit Findings

1. **Live Hugging Face Repository HEAD SHA**: `7667ad787966f5733fdca3d2b240452d7095ff95`
2. **Recorded Synthetic SHA**: `50bdcb5a50bdcb5a50bdcb5a50bdcb5a50bdcb5a`
3. **Verification Result**: The recorded string `50bdcb5a...` does NOT exist in Hugging Face commit history. It was classified as `INVALID_PROVENANCE_METADATA` generated during pilot manifest instantiation.
4. **Actual Loaded Snapshot**: When vLLM loads `UWNSL/Qwen2.5-7B-deepscaler_4k_step_256`, Hugging Face Hub resolves to the canonical HEAD snapshot **`7667ad787966f5733fdca3d2b240452d7095ff95`**.
5. **Weight Identity**: The evaluated model weights are cryptographically identical to the frozen primary StateShift step-256 endpoint model.

---

## 2. Classification

$$\mathbf{CLASSIFICATION:\ D.\ REVISION\_METADATA\_INVALID\_BUT\_WEIGHTS\_IDENTIFIED}$$

* **Historical Audit Preservation**: The recorded invalid string `50bdcb5a...` is preserved in historical audit records, while publication-facing metadata is updated to `7667ad787966f5733fdca3d2b240452d7095ff95`.

*Signed by Hugging Face Model Provenance Auditor & Reproducibility Engineer*
