# ACTIVE RECORD CONSISTENCY SWEEP REPORT (1I.1)

**Milestone**: Phase 1I.1 Project-Wide Consistency Sweep  
**Execution Timestamp**: `2026-08-19 23:04 UTC`  
**Auditor**: Reproducibility Engineer & Scientific Integrity Auditor  
**Consistency Audit Verdict**: **`SWEEP COMPLETE — SUPERSEDED DOCUMENTS LABELED`**

---

## 1. Project-Wide Consistency Status Table

| Artifact File | Historical Reference | Current Canonical Status | Action Taken / Supercession Label |
| :--- | :--- | :--- | :--- |
| `PHASE1I_READINESS_REPORT.md` | $N=456$, $131,328$ rollouts | **`SUPERSEDED BY PHASE 1I.1`** | Marked superseded in project header |
| `PHASE1I_ANALYSIS_FREEZE.md` | Logit trajectory / 9-BH tests | **`SUPERSEDED BY PHASE1I_ANALYSIS_FREEZE_V2`** | Corrected prospective estimand |
| `PHASE1I_DRY_RUN_LEDGER.jsonl` | 131,328 records ($N=456$) | **`SUPERSEDED BY V2`** | Replaced by `PHASE1I_DRY_RUN_LEDGER_V2.jsonl` ($130,752$) |
| `PHASE1I_FINAL_COST_MODEL.md` | $N=456$ cost table | **`SUPERSEDED BY V2`** | Replaced by `PHASE1I_FINAL_COST_MODEL_V2.md` ($N=454$) |
| `PHASE1I_CHECKPOINT_REGISTRY.json` | Blanket "READY" tags | **`SUPERSEDED BY V2`** | Replaced by `PHASE1I_CHECKPOINT_REGISTRY_V2.json` |

---

## 2. Dynamic Registry Enforcement

Execution scripts (`run_confirmatory_experiment.py`) now dynamically load $N$ directly from `FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4.json` and verify its SHA-256 hash (`76f1a8adead0f3ebe78ac0ef2b2b87f55767083b9988bbdee61a69af7b9d5478`) before launching execution. No hard-coded $N$ values exist in launcher code.

*Signed by Reproducibility Engineer & Scientific Integrity Auditor*
