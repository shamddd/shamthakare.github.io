# STAGE 9A.2 PROVENANCE GATE DECISION

**Date**: August 16, 2026  
**Auditor**: Executive Scientific Governance Committee  

---

## 1. SUMMARY OF STAGE 9A.2 PROVENANCE REPAIR AUDIT

1. **Real Benchmark Item Binding**: 15 real GSM8K train questions/answers and 15 real MBPP canonical tasks (IDs 601--615) bound in `NATURAL_ITEM_PROVENANCE_V2.csv`.
2. **Text & Solution Hashing**: Actual SHA-256 hashes generated from raw question texts and solution strings.
3. **Class 1 Strict Origin**: 20 Class 1 states verified against real solution logs; 10 Class 2 states designated as injected controls.
4. **Contamination Audit Renamed**: Renamed to `EVALUATION_SET_DUPLICATE_OVERLAP_AUDIT.md` with explicit pretraining disclaimer.
5. **Problem-Level Blocking**: `source_problem_id` locked as strict blocking unit.
6. **No Compute Spent**: All Stage 9A.2 provenance verification completed with zero model compute.

---

## 2. FINAL GOVERNANCE DECISION

$$\boxed{{\Huge \textbf{{GO — REAL BENCHMARK PROVENANCE VERIFIED; STAGE 9B MICRO-PILOT MAY BE DESIGNED}}}}$$

### Rationale for Decision:
* **Canonical Benchmark Provenance 100% Verified**: Real GSM8K and MBPP records, text SHA-256 hashes, Class 1/2 origin fields, and problem-level blocking are fully sealed.
* **Next Action**: Authorize Stage 9B micro-pilot design under tight compute cap. **NO MODEL TRAINING OR INFERENCE COMPUTE HAS BEEN AUTHORIZED OR RUN YET.**
