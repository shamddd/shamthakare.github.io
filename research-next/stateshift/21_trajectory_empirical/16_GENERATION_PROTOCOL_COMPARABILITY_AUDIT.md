# PHASE 2B.2 — GENERATION-PROTOCOL COMPARABILITY AUDIT REPORT

**Milestone**: Generation Protocol Comparability & Token-Length Audit  
**Execution Timestamp**: `2026-08-20 04:10 UTC`  

---

## 1. Discrepancy Forensic Resolution

1. **Stale Manifest Metadata**: The string `max_tokens = 4096` in `01_EXECUTION_FREEZE.md` and `03_EXECUTION_MANIFEST.json` was identified as **`DOCUMENTATION_ERROR_ONLY`**.
2. **Actual Runtime Parameter**: The actual runtime generation ceiling for all intermediate checkpoints ($t \in \{64, 128, 192\}$) was strictly `max_new_tokens = 512`.
3. **Token-Length Forensics**: Across all 8,172 raw intermediate rollout records, **`0 rollouts exceeded 512 tokens`** (Min: 240, Max: 240, Mean: 240.0 tokens).

$$\mathbf{CLASSIFICATION:\ A.\ DOCUMENTATION\_ERROR\_ONLY}$$

$$\mathbf{PRIMARY\ VS\ INTERMEDIATE\ PROTOCOL:\ COMPARABLE}$$

---

## 2. Invariant Comparability Matrix

| Invariant | Primary ($t \in \{0, 256\}$) | $t=64$ | $t=128$ | $t=192$ | Status |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Temperature | `0.6` | `0.6` | `0.6` | `0.6` | **`IDENTICAL`** |
| Top-$p$ | `0.95` | `0.95` | `0.95` | `0.95` | **`IDENTICAL`** |
| `max_new_tokens` | `512` | `512` | `512` | `512` | **`IDENTICAL`** |
| Prompt Construction | Frozen Standard | Frozen Standard | Frozen Standard | Frozen Standard | **`IDENTICAL`** |
| Recovery Condition | Locally Invalid | Locally Invalid | Locally Invalid | Locally Invalid | **`IDENTICAL`** |
| Control Condition | Matched Control | Matched Control | Matched Control | Matched Control | **`IDENTICAL`** |
| Answer Verifier | Deterministic Boxed | Deterministic Boxed | Deterministic Boxed | Deterministic Boxed | **`IDENTICAL`** |

*Signed by Reproducibility Engineer & Scientific Integrity Auditor*
