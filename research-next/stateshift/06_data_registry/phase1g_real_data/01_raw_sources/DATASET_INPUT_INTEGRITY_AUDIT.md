# DATASET INPUT INTEGRITY AUDIT

**Audit Date**: `2026-08-17T05:44:47.973615+00:00`  
**Verifier**: StateShift Reproducibility & Integrity Engine  

---

## 1. Input Integrity Verification Matrix

| Dataset Identifier | Repository / Source | Split | Record Count | File Size (Bytes) | SHA-256 Digest | Schema Verification | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **MATH-500** | `HuggingFaceH4/MATH-500` | `test` | `500` | `478,566` | `e51c56264004515c91c5b99714ef3d21e0373f87506e6b37110fbada033c9581` | `problem, solution, answer, subject, level, unique_id` | **PASSED** |
| **DeepScaleR** | `agentica-org/DeepScaleR-Preview-Dataset` | `train` | `40315` | `23,511,379` | `2f538b8caad164364428609ec13194628314e43096b46c2e939781ce82e2243c` | `problem, answer, solution` | **PASSED** |
| **Omni-MATH** | `KbsdJames/Omni-MATH` | `test` | `4428` | `7,827,085` | `a532162daf00e6940c0ab0bdecc13efcc981caaac08313371f45351476aa2b7c` | `domain, difficulty, problem, solution, answer, source` | **PASSED** |

---

## 2. Structural & Schema Integrity Verification

1. **MATH-500**:
   - Total records: `500` (Matches canonical MATH-500 benchmark spec).
   - Null value check: 0 null problems, 0 null solutions.
   - Unique problem statements: `500` (100% unique problem statements).

2. **DeepScaleR Training Data**:
   - Total records: `40315` (Matches official DeepScaleR-Preview train split).
   - Problem statement availability: 100% non-empty strings.

3. **Omni-MATH Dataset**:
   - Total records: `4428` (Matches official Omni-MATH test benchmark).
   - Domain coverage: Geometry, Algebra, Number Theory, Combinatorics, Calculus.

---
**Verdict**: All raw datasets verified against official checksums and schemas. Proceeding to normalization lock.
