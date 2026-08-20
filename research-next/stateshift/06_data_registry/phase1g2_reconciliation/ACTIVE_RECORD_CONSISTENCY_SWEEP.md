# ACTIVE RECORD CONSISTENCY SWEEP REPORT

**Audit Date**: `2026-08-17 06:18 UTC`  
**Status**: **ZERO UNRESOLVED LOAD-BEARING CONTRADICTIONS**  

---

## Verified Terms & Reconciled Values Matrix

| Parameter / Term | Reconciled Authoritative Value | Source Artifact | Consistency Status |
| :--- | :--- | :--- | :---: |
| **Primary Estimand** | $\Gamma_t = (\mu_{R,t} - \mu_{R,0}) - (\mu_{C,t} - \mu_{C,0})$ | `PRIMARY_ESTIMAND_FINAL.md` | **RECONCILED** |
| **Primary Scalar Endpoint** | $\Gamma_T$ at $T=256$ | `PRIMARY_ESTIMAND_FINAL.md` | **RECONCILED** |
| **Decontamination Exclusions** | $29$ unique problems ($3$ exact, $12$ struct, $14$ near) | `DECONTAMINATION_CATEGORY_RECONCILIATION.md` | **RECONCILED** |
| **Primary Conservative Pool** | $N = 471$ | `MATH500_PRIMARY_CONSERVATIVE_POOL.json` | **RECONCILED** |
| **Final Registered Pairs** | $N = 365$ Control/Recovery pairs | `FINAL_PROSPECTIVE_STATE_REGISTRY.json` | **RECONCILED** |
| **Lineage Overlap Count** | $3,501$ direct problem matches | `CORPUS_OVERLAP_FINAL_RECONCILIATION.md` | **RECONCILED** |
| **Unique Training Examples** | $41,242$ unique items searched | `CORPUS_OVERLAP_FINAL_RECONCILIATION.md` | **RECONCILED** |
| **Terminal Attrition Path** | $471 \rightarrow 366 \rightarrow 365$ ($105$ ineligible, $1$ pair fail) | `ATTRITION_STAGE_RECONCILIATION_REPORT.md` | **RECONCILED** |
| **MDES / Power Language** | Downgraded to generic design-sensitivity illustration | `STATISTICAL_INFERENCE_RECONCILIATION.md` | **RECONCILED** |
| **Segmentation Precision** | $94.0\%$ ($47/50$, Wilson CI $[83.5\%, 97.9\%]$) | `SEGMENTATION_CLAIM_REPAIR.md` | **RECONCILED** |
| **Bootstrap Algorithm** | $B=10,000$ Problem-Blocked Bootstrap | `BOOTSTRAP_ALGORITHM_LOCK.md` | **RECONCILED** |

---
