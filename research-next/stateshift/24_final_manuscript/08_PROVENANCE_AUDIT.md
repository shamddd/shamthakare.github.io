# PHASE 3B — MODEL PROVENANCE & WEIGHT AUDIT REPORT

**Milestone**: Model Provenance & Model Revision Verification  

---

## 1. Verified Model Lineage & Commit Lock

* **Pretrained Base Model ($t=0$)**: `Qwen/Qwen2.5-7B`
* **RL Checkpoint Lineage**: `UWNSL/Qwen2.5-7B-deepscaler_4k_step_X`
* **Verified Live Hugging Face Commit SHAs**:
  * $t=32$: `f46f9eac9908013a502735b7e882821f492ca61e`
  * $t=64$: `d57afa929761825af618c6545ab7f7a5b28b3dc1`
  * $t=96$: `5164cb6d7dcace900aed6a961cea33de40f2b6dc`
  * $t=128$: `27d9d8455a50c0cb0af37e9676bac4e2a1ecddec`
  * $t=160$: `d8df8a5d6290bcc7b4b5fa108121cc5b9808bf58`
  * $t=192$: `cb3f9bda37c44699246d04b9af21df41879e0ac3`
  * $t=224$: `1833fa4e7beea19c2451e1f7a4dfe3068454edaf`
  * $t=256$: `7667ad787966f5733fdca3d2b240452d7095ff95`
* **Historical Synthetic SHA**: `50bdcb5a...` preserved only in audit logs as `INVALID_SYNTHETIC_PLACEHOLDER_REVISION`.

$$\mathbf{PROVENANCE\ AUDIT\ VERDICT:\ PASS}$$

*Signed by Reproducibility Engineer & Model Provenance Auditor*
