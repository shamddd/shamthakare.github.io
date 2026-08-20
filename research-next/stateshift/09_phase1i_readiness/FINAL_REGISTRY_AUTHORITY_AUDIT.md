# FINAL CONFIRMATORY REGISTRY AUTHORITY AUDIT

**Milestone**: Phase 1I.1 Registry Provenance & Reconciliation Audit  
**Execution Timestamp**: `2026-08-19 22:56 UTC`  
**Auditor**: Reproducibility Engineer & Scientific Integrity Auditor  
**Primary Authoritative Registry File**: `FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4.json`  
**Strict Contamination Registry File**: `FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4_STRICT.json`  
**Registry Reconciliation Verdict**: **`RECONCILED & HASH-VERIFIED`**

---

## 1. Authoritative Registry Verification Table

| Registry Version | Target Count ($N$) | File Location | SHA-256 Hash | Status |
| :--- | :---: | :--- | :--- | :---: |
| **Authoritative Post-Human V4** | **`N = 454`** | [`FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4.json`](file://~/.gemini/antigravity/scratch/research-next/stateshift/06_data_registry/human_adjudication/FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4.json) | `76f1a8adead0f3ebe78ac0ef2b2b87f55767083b9988bbdee61a69af7b9d5478` | **`AUTHORITATIVE PRIMARY`** |
| **Strict Contamination V4** | **`N = 388`** | [`FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4_STRICT.json`](file://~/.gemini/antigravity/scratch/research-next/stateshift/06_data_registry/human_adjudication/FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4_STRICT.json) | `667660ca243c2d6df8af4cec7cd859ef2bd403ff1993abc033947409dd210227` | **`STRICT SECONDARY`** |

---

## 2. Forensic Audit of Prospective Pair Exclusions

A line-item audit confirms why $N=454$ supersedes initial drafts ($N=456$):

1. **`pair_math500_367`**: Prospectively excluded. Operator perturbation `OP_SIGN_FLIP` modified mathematical inverse-function notation $f^{-1}(x) \to f^{+1}(x)$. Notation alteration is an inadmissible perturbation under the preregistered arithmetic sign perturbation specification.
2. **`pair_math500_391`**: Prospectively excluded during human semantic adjudication repair due to ambiguous ground-truth target formatting.

Both exclusions were applied prospectively prior to model inference. SHA-256 hashes recomputed directly from disk confirm exact agreement.

*Signed by Reproducibility Engineer & Lead Statistical Methodologist*
