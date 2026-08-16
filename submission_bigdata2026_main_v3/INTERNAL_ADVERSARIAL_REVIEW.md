# INTERNAL ADVERSARIAL REVIEW REPORT

> **DISCLAIMER**: This document records an internal red-team self-audit executed during paper preparation. It is NOT an independent peer review and MUST NOT be represented as an official decision by any conference committee.

**Paper Title**: `recovery_eval`: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning  
**Target Venue**: IEEE BigData 2026 (Special Session on Machine Learning on Big Data)  

---

## Internal Risk Assessment Summary

| Reviewer Persona / Focus | Internal Risk Classification | Primary Item Evaluated | Status |
| :--- | :--- | :--- | :--- |
| **IEEE BigData Area Chair** | **`PASS`** | Scope alignment with MLBD Special Session & IEEE BigData | **RESOLVED** |
| **LLM Evaluation Researcher** | **`PASS`** | State perturbation, verifier logic, prompt template separation | **RESOLVED** |
| **Statistical Reviewer** | **`PASS`** | Matching metric nomenclature, 95% bootstrap CI interpretation | **RESOLVED** |
| **Reproducibility Reviewer** | **`PASS`** | Primitive evidence sealing (SHA-256), token round-trip decode | **RESOLVED** |

---

## Detailed Risk Item Log

### 1. Scope & Framing Audit
* **Item**: Ensure manuscript is framed as machine learning evaluation infrastructure, LLM reasoning diagnostics, and reproducible data-centric AI benchmarking rather than a novel training algorithm.
* **Risk Classification**: `MINOR`
* **Resolution**: Wording in `main.tex` explicitly presents `recovery_eval` as an evaluation and diagnostic framework.

### 2. Matching Metric Nomenclature
* **Item**: Do not confuse weighted-L1 distance with Standardized Mean Difference (SMD).
* **Risk Classification**: `MAJOR`
* **Resolution**: Metric is explicitly named **normalized weighted-L1 matched-pair distance**. Per-covariate SMDs are reported separately (Depth: $+0.0000$, Remaining Length: $+0.0000$, Token Length: $+0.1333$).

### 3. Empirical Claim Boundaries
* **Item**: Prevent over-interpretation of $D_{	ext{recovery}} = -0.1100$ ($95\%$ CI $[-0.240, +0.030]$).
* **Risk Classification**: `BLOCKER`
* **Resolution**: Wording locked to *"Under the evaluated state-matched protocol, we did not observe evidence of a recovery-specific advantage for the Instruct checkpoint over the Base checkpoint."* Zero causal claims or assertions of Base superiority.

### 4. Primitive Evidence Integrity
* **Item**: Verify raw JSONL evidence SHA-256 and token decode round-trip.
* **Risk Classification**: `BLOCKER`
* **Resolution**: `RAW_NEURAL_ROLLOUTS.jsonl` SHA-256 sealed (`51b5a157...`), 400/400 BPE decode round-trip match verified, independent verifier passed 100%.

---

**FINAL INTERNAL VERDICT**: **`PASS — ZERO ACTIVE UNRESOLVED BLOCKERS`**
