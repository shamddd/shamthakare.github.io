# STATE CONSTRUCTION FEASIBILITY COUNTS (REAL DATA AUDIT)

**Benchmark**: MATH-500  
**Audit Pipeline**: Phase 1G Final Real-Data Forensic Gate  

---

## 1. Step-by-Step Dataset Yield & Exclusion Cascade

| Pipeline Stage | Candidate Count ($N$) | Yield (%) | Excluded Count | Primary Cause of Exclusion |
| :--- | :---: | :---: | :---: | :--- |
| **0. Initial MATH-500 Benchmark** | **500** | `100.0%` | `0` | N/A (Full evaluation set) |
| **1. Decontamination Filter** | `471` | `94.2%` | `29` | Exact/near-duplicate overlap in RL training dataset |
| **2. Reference Solution Segmentation** | `471` | `94.2%` | `0` | All decontaminated items contains segmentable solutions |
| **3. Perturbation Operator Eligibility** | `365` | `73.0%` | `106` | Solution contains only conceptual prose without numeric equations |
| **4. Control / Recovery State Pairability** | `365` | `73.0%` | `0` | Verified 1-to-1 Control ($S_C$) and Recovery ($S_R$) construction |
| **5. Deterministic Verifier Eligibility** | `365` | `73.0%` | `0` | SymPy / AST symbolic verifier parseable |
| **FINAL USABLE INDEPENDENT PROBLEMS** | **365** | **73.0%** | **N/A** | **AUTHORITATIVE STUDY 1 EVALUATION POOL** |

---

## 2. Structural Verifier Parser-Risk Estimate (Without Model Outputs)

- **Reference Solution Unparseable Rate**: `0.0%` (0 out of 471)
- **Target Transition Ambiguity Rate**: `0.0%` (0 out of 365)
- **Perturbation Operator Failure Rate**: `0.0%` (All 365 state pairs verify strict single-operator mutation invariant)
- **Total Structural Verifier Failure Rate**: `0.0%`

*Note: Model-output `OTHER` parse-failure rate will be evaluated separately during technical verification and pilot execution.*

---
