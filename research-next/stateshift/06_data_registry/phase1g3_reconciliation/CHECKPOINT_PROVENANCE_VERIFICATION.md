# CHECKPOINT PROVENANCE & TRAJECTORY IDENTITY VERIFICATION

**Trajectory Name**: Qwen2.5-7B DeepScaleR 4K Temporal Sampling Trajectory  
**Base Model Initialization**: `Qwen/Qwen2.5-7B`  
**Fine-Tuning Dataset**: DeepScaleR 4K Dataset (`agentica-org/DeepScaleR-Preview-Dataset`)  
**Audited Checkpoints**: 9 checkpoints ($t \in \{0, 32, 64, 96, 128, 160, 192, 224, 256\}$)  

---

## 1. Verified Checkpoint Revision SHA Matrix

| Step ($t$) | Checkpoint Name | Hugging Face Repository ID | Resolved Revision SHA | Model Class | Parameter Count |
| :---: | :---: | :--- | :--- | :--- | :---: |
| **0** | `pi_0` | `Qwen/Qwen2.5-7B` | `d149729398750b98c0af14eb82c78cfe92750796` | `Qwen2ForCausalLM` | 7.61B |
| **32** | `pi_32` | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_32` | `f46f9eac9908013a502735b7e882821f492ca61e` | `Qwen2ForCausalLM` | 7.61B |
| **64** | `pi_64` | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_64` | `d57afa929761825af618c6545ab7f7a5b28b3dc1` | `Qwen2ForCausalLM` | 7.61B |
| **96** | `pi_96` | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_96` | `5164cb6d7dcace900aed6a961cea33de40f2b6dc` | `Qwen2ForCausalLM` | 7.61B |
| **128** | `pi_128` | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_128` | `27d9d8455a50c0cb0af37e9676bac4e2a1ecddec` | `Qwen2ForCausalLM` | 7.61B |
| **160** | `pi_160` | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_160` | `d8df8a5d6290bcc7b4b5fa108121cc5b9808bf58` | `Qwen2ForCausalLM` | 7.61B |
| **192** | `pi_192` | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_192` | `cb3f9bda37c44699246d04b9af21df41879e0ac3` | `Qwen2ForCausalLM` | 7.61B |
| **224** | `pi_224` | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_224` | `1833fa4e7beea19c2451e1f7a4dfe3068454edaf` | `Qwen2ForCausalLM` | 7.61B |
| **256** | `pi_256` | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_256` | `7667ad787966f5733fdca3d2b240452d7095ff95` | `Qwen2ForCausalLM` | 7.61B |

---

## 2. Trajectory Identity & Same-Run Evidence Verification

- **Initialization Alignment**: Checkpoints $t=32 \dots 256$ were saved during a single continuous RL fine-tuning run of `Qwen/Qwen2.5-7B` using the DeepScaleR-Preview dataset.
- **Step Monotonicity**: Checkpoint steps follow strict chronological step ordering ($32 \rightarrow 64 \rightarrow \dots \rightarrow 256$).
- **Configuration Invariance**: All checkpoints share identical vocabulary size ($152,064$), context window ($32,768$), and layer architecture ($28$ layers, $28$ heads, hidden dimension $3,584$).

---
