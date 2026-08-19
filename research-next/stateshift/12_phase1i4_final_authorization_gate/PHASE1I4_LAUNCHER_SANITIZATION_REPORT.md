# PHASE 1I.4 LAUNCHER SANITIZATION REPORT

**Milestone**: Phase 1I.4 Launcher Cleanup & Constant Unification  
**Execution Timestamp**: `2026-08-19 23:35 UTC`  
**Target File**: `research-next/stateshift/09_phase1i_readiness/run_confirmatory_experiment.py`  

---

## 1. Superseded Constants Removal Audit

All historical/superseded constants have been completely removed from executable code:

* **Removed Superseded Assignments**:
  - `EXPECTED_TOTAL_ROLLOUTS = 130752` (Removed)
  - `HARD_BUDGET_CAP_USD = 35.00` (Removed)
  - `MIN_REQUIRED_BALANCE_USD = 30.70` (Removed)
* **Canonical Assignments Frozen**:
  - `EXPECTED_N = 454`
  - `EXPECTED_TOTAL_ROLLOUTS = 29056`
  - `EXPECTED_CHECKPOINTS = [0, 256]`
  - `EXPECTED_K = 16`
  - `EXPECTED_REGISTRY_SHA256 = "76f1a8adead0f3ebe78ac0ef2b2b87f55767083b9988bbdee61a69af7b9d5478"`
  - `EXPECTED_STRICT_SHA256 = "667660ca243c2d6df8af4cec7cd859ef2bd403ff1993abc033947409dd210227"`
  - `HARD_SPEND_CEILING_USD = 8.00`
  - `MIN_REQUIRED_BALANCE_USD = 6.82`
  - `MAX_HOURLY_GPU_RATE_USD = 1.65`

---

## 2. Print Path & Banner Unification Audit

* **Stale Banners Removed**: Duplicate print messages and superseded "Full 9-Checkpoint" banners eliminated.
* **Canonical Execution Banner**: `STATESHIFT PHASE 1I.3 ENDPOINT-K16 CONFIRMATORY EXECUTION`.
* **Configuration Loader**: Launcher dynamically loads configuration from `PHASE1I4_FINAL_EXECUTION_CONFIG.json`.

*Signed by Principal ML Systems Engineer & Reproducibility Auditor*
