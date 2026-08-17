# ATTRITION STAGE RECONCILIATION REPORT (V3 REBUILT)

**Primary Pool Problems**: $N=471$  
**Audit Pipeline**: Phase 1G.3 Final Semantic Validity & Mutation Engine  

---

## 1. Authoritative Terminal Stage Partitioning Matrix ($N=471$)

| Terminal Stage | Definition | Item Count ($N$) | Percentage (%) |
| :--- | :--- | :---: | :---: |
| **`FINAL_REGISTERED`** | Successfully constructed Control ($S_C$) and Recovery ($S_R$) state pairs | **`459`** | **`97.5%`** |
| **`NO_VERIFIABLE_TRANSITION`** | Solution contains conceptual prose or diagram code without verifiable math equations | `8` | `1.7%` |
| **`NO_EFFECT_MUTATION`** | Target equation step contains no parameter that mutates under deterministic operators | `4` | `0.8%` |
| **TOTAL PRIMARY POOL** | Full decontaminated evaluation benchmark | **471** | **100.0%** |

---

## 2. Partitioning Integrity Check

- Total Primary Benchmark: `471`
- Registered Pairs: `459`
- Excluded Non-Registered Problems: `12` (`8` no-transition + `4` no-mutation)
- Sum Check: `459 + 8 + 4 = 471` (**EXACT MATCH**).

---
