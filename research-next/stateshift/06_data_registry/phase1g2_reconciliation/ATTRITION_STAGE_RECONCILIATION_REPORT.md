# ATTRITION STAGE RECONCILIATION REPORT (V2)

**Initial Benchmark**: MATH-500 ($N=500$)  
**Primary Decontaminated Pool**: $N=471$ (excluding 29 decontaminated collisions)  

---

## 1. Terminal Stage Partitioning Matrix ($N=471$)

| Terminal Stage | Definition | Problem Count ($N$) | Percentage of Primary Pool (%) |
| :--- | :--- | :---: | :---: |
| **`FINAL_REGISTERED`** | Successfully constructed Control ($S_C$) and Recovery ($S_R$) state pairs | **`365`** | **`77.5%`** |
| **`PERTURBATION_INELIGIBLE`** | Solution contains conceptual prose without verifiable numeric equations | `10` | `2.1%` |
| **`PAIR_CONSTRUCTION_FAILURE`** | Solution target step lacks modifiable integer/sign parameter (`math500_214`) | **`96`** | **`20.4%`** |
| **TOTAL PRIMARY POOL** | Full decontaminated evaluation benchmark | **471** | **100.0%** |

---

## 2. Reconciled Cascade Summary

1. **Primary Pool**: $N = 471$
2. **Perturbation-Eligible Stage**: $471 - 105 \text{ ineligible} = \mathbf{366 \text{ eligible problems}}$.
3. **Pair Construction Stage**: $366 - 1 \text{ pair failure (math500\_214)} = \mathbf{365 \text{ final registered pairs}}$.
4. **Total Excluded Primary Problems**: $105 + 1 = \mathbf{106 \text{ problems}}$.

---
