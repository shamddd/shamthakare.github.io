# INVALIDITY CLASSIFICATION FINAL REPORT

**Source of Truth**: `INVALIDITY_CLASSIFICATION_FINAL.csv` ($N=468$)  
**Audit Milestone**: Phase 1G.4d Final Classification Consistency Seal  

---

## 1. Dynamically Computed Invalidity Level Breakdown ($N=468$)

| Verification Level Category | Context Eval Performed | Human Review Required | Pair Count ($N$) | Percentage (%) | Operational Definition |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **`SEMANTICALLY_EVALUATED_INVALID`** | **YES** | **NO** | **`218`** | **`46.6%`** | Numerical parameter offsets & numeric fraction inversions evaluated false under context |
| **`OPERATOR_NON_EQUIVALENT`** | **NO** | **YES** | **`250`** | **`53.4%`** | Sign flips & symbolic fraction flips provably changing expression value, requiring human review |
| **TOTAL REGISTRY V4** | — | — | **468** | **100.0%** | All confirmatory prospective state pairs |

---

## 2. Operator $\times$ Verification Level Cross-Tabulation

| Operator Name | Registered Pairs ($N$) | `SEMANTICALLY_EVALUATED_INVALID` | `OPERATOR_NON_EQUIVALENT` | Human Review Required (`YES`) |
| :--- | :---: | :---: | :---: | :---: |
| **`OP_CONSTANT_PERTURB`** | `183` | `183` | `0` | `0` |
| **`OP_SIGN_FLIP`** | `191` | `0` | `191` | `191` |
| **`OP_FRACTION_FLIP`** | `94` | `35` | `59` | `59` |
| **TOTAL** | **468** | **218** | **250** | **250** |

---
