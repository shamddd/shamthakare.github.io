# Program 2 Internal Decontamination Audit

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Purpose**: Formally establish the scientific decontamination boundary separating Program 2 from `PUB-001`, `PUB-002`, `PUB-003`, and `PAPER CANDIDATE #4`.

---

## 1. Immutable Four-Paper Firewall Audit

| Prior Publication | Primary Claim | Program 2 Proposed Research Question | Overlap Score | Decontamination Result |
|---|---|---|:---:|---|
| **`PUB-001`** (IEEE TAI) | Sample-level consensus GRPO gives 0.00% Pass@1 gain; token entropy is length-confounded. | Do transient tool-execution failures create persistent belief-state errors that alter downstream actions after tool recovery? | **0 (Unrelated)** | **PASS**. Program 2 focuses on multi-turn agent environment tool errors, NOT RL policy credit assignment. |
| **`PUB-002`** (IEEE BigData `BigD497`) | Matched recovery contrast $D_{\text{recovery}} = -0.1100$; Instruct checkpoints show no recovery-specific advantage over Base. | Do transient tool-execution failures create persistent belief-state errors that alter downstream actions after tool recovery? | **1 (Shared Area)** | **PASS**. `PUB-002` evaluated single-step arithmetic prefix errors. Program 2 evaluates **external tool failures, persistent belief-state corruption, multi-turn decision depth ($d \ge 1$), and downstream machine-verifiable safety violations**. |
| **`PUB-003`** (TMLR) | OOD length extrapolation reduces crossover query volume ($R_f \approx 0.0618$). | Do transient tool-execution failures create persistent belief-state errors that alter downstream actions after tool recovery? | **0 (Unrelated)** | **PASS**. Program 2 evaluates multi-turn agent belief persistence, NOT compute amortization frontiers ($Q^*$). |
| **`PAPER CANDIDATE #4`** (Program 1) | Model capability is a boundary condition for GRPO self-consistency calibration. | Do transient tool-execution failures create persistent belief-state errors that alter downstream actions after tool recovery? | **0 (Unrelated)** | **PASS**. Program 2 evaluates agent tool error propagation, NOT RLVR uncertainty calibration. |

---

## 2. Distinction from `PUB-002`

`PUB-002` established that aggregate accuracy gains do not translate into a specialized single-step error-recovery advantage on mathematical prefixes. To strictly preserve `PUB-002`, Program 2:
1. **Does NOT claim** "LLMs fail to recover from arithmetic missteps".
2. **Targets External Tool Failures**: Evaluates API timeouts ($F_1$), permission denials ($F_2$), malformed payloads ($F_3$), and stale observations ($F_4$).
3. **Measures Temporal Error Persistence ($d \ge 1$)**: Evaluates whether agent behavior remains divergent *after the external tool is fully restored to health*.
