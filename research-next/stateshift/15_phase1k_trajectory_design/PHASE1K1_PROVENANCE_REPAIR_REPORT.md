# PHASE 1K.1 PROVENANCE REPAIR REPORT

**Milestone**: Phase 1K.1 Provenance Repair & Ledger V2 Finalization  
**Execution Timestamp**: `2026-08-20 01:17 UTC`  
**Auditor**: Scientific Integrity Auditor & ML Systems Engineer  

---

## 1. Summary of Provenance Repair

All placeholder SHA references in Stage 1 have been completely replaced with real, verified 40-character Git commit SHAs obtained via live API queries to Hugging Face.

* **Replaced Draft Ledger**: `PHASE1K_SECONDARY_LEDGER_DRAFT.jsonl`
* **Canonical Verified Ledger**: `PHASE1K_SECONDARY_LEDGER_V2.jsonl` ($12,712$ rows, SHA-256 `70c0cd88c6036c087f77c1a530388b1ef821d1f1d86dab69845a525bf3ab0ac8`)
* **Verification Status**: **`100% VERIFIED LIVE`**

---

## 2. Updated Cost & Financial Summary

| Candidate $K$ | Rollouts Count | Extrapolated GPU-Hours | Base Compute Cost | Total Budget (incl 20% reserve) | Fits in $3.74 Balance? | Remaining Balance Buffer | Claim Capability |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **$K = 2$** | **12,712** | **1.56 h** | **$2.49 USD** | **$2.98 USD** | **YES** | **+$0.76 USD** | **DESCRIPTIVE TRAJECTORY ONLY** |
| **$K = 3$** | 19,068 | 2.35 h | $3.73 USD | $4.48 USD | **NO** | -$0.74 USD | DESCRIPTIVE + EMERGENCE TIMING |
| **$K = 4$** | 25,424 | 3.13 h | $4.97 USD | $5.97 USD | **NO** | -$2.23 USD | MONOTONICITY & EMERGENCE (DEFENSIBLE) |

*Signed by Scientific Integrity Auditor & ML Systems Engineer*
