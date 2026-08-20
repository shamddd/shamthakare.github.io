# Program 1 Internal Decontamination Audit & Professor Gap Re-Classification

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Purpose**: Formally verify the internal three-paper firewall (`PUB-001`, `PUB-002`, `PUB-003`) and correct professor gap classifications to strictly separate verbatim explicit paper gaps from inferred scientific research alignment.

---

## 1. Internal Three-Paper Firewall Audit

| Submitted Manuscript | Primary Claim | Program 1 Research Question | Overlap Score | Decontamination Result |
|---|---|---|:---:|---|
| **`PUB-001`** (IEEE TAI) | Sample-level consensus GRPO gives 0.00% Pass@1 gain; token entropy is length-confounded ($r=+0.486$). | Does GRPO post-training alter the predictive reliability of self-consistency agreement ($S_{\text{ans}}$) and Area Under Risk-Coverage (AURC)? | **2 (Shared Infra)** | **DECONTAMINATED**. Program 1 tests trajectory agreement calibration failure (AURC & Brier score) under GRPO mode collapse, NOT sample-level credit weighting. |
| **`PUB-002`** (IEEE BigData) | Matched recovery contrast $D_{\text{recovery}} = -0.1100$; Instruct checkpoints show no recovery-specific advantage over Base. | Does self-consistency become less informative when post-training preserves or improves baseline accuracy? | **1 (Shared Area)** | **DECONTAMINATED**. Program 1 evaluates self-consistency trajectory agreement calibration, NOT single-step state-matched error recovery. |
| **`PUB-003`** (TMLR) | OOD length extrapolation reduces crossover query volume ($R_f \approx 0.0618$). | Does trajectory homogenization ($J_{\text{path}}$) mediate self-consistency agreement decoupling? | **1 (Shared Area)** | **DECONTAMINATED**. Program 1 evaluates uncertainty calibration reliability, NOT deployment compute amortization frontiers ($Q^*_{\text{frontier}}$). |

---

## 2. Professor Open Problem Gap Re-Classification

Every entry previously marked `EXPLICIT_GAP` has been audited against primary paper text. Unless verbatim text in the paper explicitly identifies the gap, the label is updated to **`INFERRED_ALIGNMENT`**:

1. **MIT — Jacob Andreas & Yoon Kim (LINGO Lab)**:
   - *Paper*: *Beyond Binary Rewards: Training LMs to Reason About Uncertainty* (ICLR 2026).
   - *Audited Passage*: The paper demonstrates that incorporating Brier rewards into PPO calibrates verbalized confidence. It does not explicitly state "evaluate trajectory agreement under GRPO".
   - *Re-Classification*: **`INFERRED_ALIGNMENT`** (Intellectual alignment on uncertainty-aware reward design).

2. **MIT — Armando Solar-Lezama & Nickolai Zeldovich (CSAIL)**:
   - *Paper*: *Verifiable Enclave Execution for AI Workloads* (USENIX Security 2025).
   - *Audited Passage*: Focuses on enclave OS kernel attestation. Does not explicitly mention "verifiable audit logging for dynamic agent tool execution streams".
   - *Re-Classification*: **`INFERRED_ALIGNMENT`** (Intellectual alignment on verifiable systems execution).

3. **Harvard — Sham Kakade & Finale Doshi-Velez**:
   - *Re-Classification*: **`INFERRED_ALIGNMENT`** (Theoretical bounds on model post-training).

4. **Princeton — Wyatt Lloyd & Michael Freedman**:
   - *Re-Classification*: **`INFERRED_ALIGNMENT`** (Consensus tail-latency optimization).

5. **Columbia — Elias Bareinboim**:
   - *Re-Classification*: **`INFERRED_ALIGNMENT`** (Causal sequential decision making).

6. **Penn — Eric Wong**:
   - *Re-Classification*: **`INFERRED_ALIGNMENT`** (Provable safety bounds for neural policies).
