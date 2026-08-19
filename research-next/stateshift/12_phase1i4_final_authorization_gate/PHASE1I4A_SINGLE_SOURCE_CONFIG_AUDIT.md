# STATESHIFT PHASE 1I.4a SINGLE SOURCE OF TRUTH LAUNCHER AUDIT REPORT

**Milestone**: Phase 1I.4a Launcher Config Refactoring & Single Source of Truth Audit  
**Execution Timestamp**: `2026-08-19 23:37 UTC`  
**Auditor**: Principal ML Systems Engineer & Scientific Integrity Auditor  
**Single Source of Truth Configuration File**: [`PHASE1I4_FINAL_EXECUTION_CONFIG.json`](file:///Users/shamthakare/.gemini/antigravity/scratch/research-next/stateshift/12_phase1i4_final_authorization_gate/PHASE1I4_FINAL_EXECUTION_CONFIG.json)  
**Expected Configuration SHA-256**: `079f99bf8e5ceb8b45b680b4bc2e34f718e4453031c55ee456da0a331209cdcf`  

---

## 1. Single Source of Truth Refactoring Audit

The launcher script [`run_confirmatory_experiment.py`](file:///Users/shamthakare/.gemini/antigravity/scratch/research-next/stateshift/09_phase1i_readiness/run_confirmatory_experiment.py) has been strictly refactored to eliminate all duplicated scientific and runtime constants:

| Audit Checkpoint | Pre-Refactoring State | Post-Refactoring State (Phase 1I.4a) | Verification Status |
| :--- | :--- | :--- | :---: |
| **Hard-coded Identifiers** | Duplicated constants in executable logic | `CONFIG_PATH` and `EXPECTED_CONFIG_SHA256` ONLY | **`VERIFIED`** |
| **Config Hash Check** | Unchecked or post-parse check | Hash verified **BEFORE** parsing JSON | **`VERIFIED`** |
| **Fallback Defaults (`.get()`)** | Silent defaults (e.g. `CONFIG.get("n", 454)`) | Direct dictionary lookup `CONFIG["key"]` (KeyError on missing) | **`VERIFIED`** |
| **Execution Banner** | Multiple historical banners | Exactly **ONE** banner: `STATESHIFT PHASE 1I.3 ENDPOINT-K16 CONFIRMATORY EXECUTION BANNER` | **`VERIFIED`** |

---

## 2. Invariant Extraction Verification

The launcher extracts all 22 required scientific and runtime invariants directly from `PHASE1I4_FINAL_EXECUTION_CONFIG.json`:

1. `authoritative_registry_path` $\to$ `"research-next/stateshift/06_data_registry/human_adjudication/FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4.json"`
2. `authoritative_registry_sha256` $\to$ `"76f1a8adead0f3ebe78ac0ef2b2b87f55767083b9988bbdee61a69af7b9d5478"`
3. `authoritative_n` $\to$ `454`
4. `strict_registry_path` $\to$ `"research-next/stateshift/06_data_registry/human_adjudication/FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4_STRICT.json"`
5. `strict_registry_sha256` $\to$ `"667660ca243c2d6df8af4cec7cd859ef2bd403ff1993abc033947409dd210227"`
6. `strict_n` $\to$ `388`
7. `checkpoints` $\to$ `[0, 256]`
8. `rollouts_per_cell_k` $\to$ `16`
9. `total_confirmatory_rollouts` $\to$ `29056`
10. `model_repositories` $\to$ `{"t=0": "Qwen/Qwen2.5-7B", "t=256": "UWNSL/Qwen2.5-7B-deepscaler_4k_step_256"}`
11. `model_revisions` $\to$ `{"t=0": "d149729398...", "t=256": "7667ad7879..."}`
12. `sampling_temperature` $\to$ `0.6`
13. `sampling_top_p` $\to$ `0.95`
14. `max_new_tokens` $\to$ `512`
15. `protocol_hash` $\to$ `"0b8555185b9f769ea9db7b09bdd42dd61dc22b47ef44ec87cea0ed1be35c4e8e"`
16. `analysis_freeze_hash` $\to$ `"b97d620cd0913a961329be684c91d27b75e4b2bac94727d578aabb9fc1c3d88c"`
17. `ledger_path` $\to$ `"research-next/stateshift/11_phase1i3_execution_freeze/PHASE1I3_FINAL_CONFIRMATORY_LEDGER.jsonl"`
18. `ledger_sha256` $\to$ `"63628d7f3c0922a2af7e4dfbbde60ac33afaf1be11aa7bf62fd0dd933fb2ce39"`
19. `hard_spend_ceiling_usd` $\to$ `8.00`
20. `expected_total_budget_usd` $\to$ `6.82`
21. `max_hourly_gpu_rate_usd` $\to$ `1.65`
22. `record_type` $\to$ `"empirical_confirmatory"`

*Signed by Principal ML Systems Engineer & Scientific Integrity Auditor*
