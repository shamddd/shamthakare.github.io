# PHASE 2B.4 — EXECUTION PROTOCOL FREEZE

**Milestone**: Nine-Checkpoint Empirical Trajectory Execution Freeze  
**Execution Timestamp**: `2026-08-20 04:26 UTC`  

---

## 1. Frozen Execution Parameters

| Parameter | Value | Standard / Invariant |
| :--- | :---: | :--- |
| **Checkpoints Evaluated** | $t \in \{32, 96, 160, 224\}$ | Reusing frozen $t \in \{0, 64, 128, 192, 256\}$ |
| **Population ($N$)** | $454$ | Identical problem registry |
| **Repetitions ($K$)** | $2$ rollouts / cell | Minimum-cost completion design |
| **Total New Rollouts** | $7,264$ | $4 \text{ checkpoints} \times 454 \text{ problems} \times 2 \text{ conditions} \times 2$ |
| **Temperature ($T$)** | $0.6$ | Frozen sampling parameter |
| **Top-$p$** | $0.95$ | Frozen sampling parameter |
| **Max Tokens** | $512$ | `max_new_tokens = 512` |
| **Hard Cost Ceiling** | $\$2.50 \text{ USD}$ | Estimated cost: $\$2.28 \text{ USD}$ |

*Signed by Reproducibility Engineer & Scientific Integrity Auditor*
