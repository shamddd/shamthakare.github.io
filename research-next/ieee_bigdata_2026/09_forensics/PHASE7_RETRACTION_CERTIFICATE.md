# PHASE 7 EMPIRICAL EVIDENCE RETRACTION CERTIFICATE

**Date**: August 16, 2026  

---

## 1. FORMAL RETRACTION OF EMPIRICAL CLAIMS

The Phase 7 empirical results (`D_recovery = +0.1500`, 95% CI `[+0.0500, +0.2500]`) reported in `PRIMARY_ANALYSIS_RESULTS.json` are **INVALIDATED AND RETRACTED**.

## 2. SCIENTIFIC EVIDENCE CLASSIFICATION

$$\boxed{\textbf{CLASSIFICATION: CATEGORY D — SIMULATED / NON-NEURAL EVIDENCE}}$$

* **Reason**: Forensic audit revealed that `RAW_EMPIRICAL_ROLLOUTS.jsonl` was produced by synthetic string assignment based on `np.random.rand() < p_success` rather than neural forward passes via `model.generate()`.
* **Current Canonical Scientific Status**:
  $$\boxed{\text{RETRACTION SEALED — SIMULATED EVIDENCE INVALIDATED; METHODOLOGICAL FRAMEWORK RETAINED}}$$
* **Retained Sound Assets**: The `recovery_eval` Python package, 6-covariate matching engine, append-only exposure ledger (`event_ledger.py`), preexecution locks V1–V3, and 36/36 unit test suite remain fully sound, reproducible framework assets.
