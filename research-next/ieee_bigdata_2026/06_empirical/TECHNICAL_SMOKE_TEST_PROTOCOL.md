# TECHNICAL SMOKE TEST PROTOCOL

**Date**: August 16, 2026  

---

## 1. SMOKE TEST SPECIFICATION

* **Prompt**: Non-reserved trivial mathematical prompt ("Calculate 2 + 2.").
* **Execution Boundary**:
  - 1 prompt.
  - 1 generation per checkpoint.
  - `max_new_tokens <= 32`.
* **Output Classification**: `record_type = "technical_smoke_test"`.
* **Non-Interference**: Strictly excluded from paper dataset and statistical analysis.
* **Success Criteria**:
  - Model loads from exact locked revision.
  - MPS device active without OOM.
  - Tokenizer decodes text correctly.
  - `ModelInputAdapter` formats inputs.
  - Primitive JSONL record logged.
