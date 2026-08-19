# PHASE 2B.1 — PRE-EXECUTION FREEZE SPECIFICATION

**Milestone**: Pre-Execution Freeze & Immutable Provenance Lock  
**Execution Timestamp**: `2026-08-20 03:57 UTC`  
**RunPod Balance**: `$3.11 USD`  
**Hard Cost Ceiling**: `$3.00 USD`  

---

## 1. Provenance Lock

| Checkpoint | Target Repository | Live Verified Commit SHA | Total Rollouts Planned |
| :--- | :--- | :--- | :---: |
| $t=64$ | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_64` | `d57afa929761825af618c6545ab7f7a5b28b3dc1` | $2,724$ |
| $t=128$ | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_128` | `27d9d8455a50c0cb0af37e9676bac4e2a1ecddec` | $2,724$ |
| $t=192$ | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_192` | `cb3f9bda37c44699246d04b9af21df41879e0ac3` | $2,724$ |

* **Total New Rollouts**: $8,172$ ($3 \text{ checkpoints} \times 454 \text{ problems} \times 2 \text{ conditions} \times 3 \text{ rollouts}$).
* **Sampling Parameters**: Temperature $T=0.6$, $\text{top\_p}=0.95$, Max Tokens $= 4096$.

*Signed by Reproducibility Engineer & Scientific Integrity Auditor*
