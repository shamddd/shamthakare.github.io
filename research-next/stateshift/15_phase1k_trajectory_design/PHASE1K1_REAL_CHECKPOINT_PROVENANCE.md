# PHASE 1K.1 REAL CHECKPOINT PROVENANCE REPORT

**Milestone**: Live Hugging Face Checkpoint Verification  
**Execution Timestamp**: `2026-08-20 01:17 UTC`  
**Auditor**: ML Systems Engineer & Reproducibility Auditor  
**Lineage**: `UWNSL/Qwen2.5-7B-deepscaler_4k_step_*`  

---

## 1. Verified Live Hugging Face Commit SHAs

All 7 intermediate fine-tuning checkpoints were queried and verified live against the Hugging Face API:

| Checkpoint $t$ | Repository Path | Resolved Immutable Commit SHA | Tokenizer Repo | Architecture | Shards | Size (GB) | Status |
| :---: | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **$t = 32$** | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_32` | `f46f9eac9908013a502735b7e882821f492ca61e` | `Qwen/Qwen2.5-7B` | `Qwen2ForCausalLM` | 4 | 14.2 GB | **`VERIFIED_LIVE`** |
| **$t = 64$** | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_64` | `d57afa929761825af618c6545ab7f7a5b28b3dc1` | `Qwen/Qwen2.5-7B` | `Qwen2ForCausalLM` | 4 | 14.2 GB | **`VERIFIED_LIVE`** |
| **$t = 96$** | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_96` | `5164cb6d7dcace900aed6a961cea33de40f2b6dc` | `Qwen/Qwen2.5-7B` | `Qwen2ForCausalLM` | 4 | 14.2 GB | **`VERIFIED_LIVE`** |
| **$t = 128$** | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_128` | `27d9d8455a50c0cb0af37e9676bac4e2a1ecddec` | `Qwen/Qwen2.5-7B` | `Qwen2ForCausalLM` | 4 | 14.2 GB | **`VERIFIED_LIVE`** |
| **$t = 160$** | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_160` | `d8df8a5d6290bcc7b4b5fa108121cc5b9808bf58` | `Qwen/Qwen2.5-7B` | `Qwen2ForCausalLM` | 4 | 14.2 GB | **`VERIFIED_LIVE`** |
| **$t = 192$** | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_192` | `cb3f9bda37c44699246d04b9af21df41879e0ac3` | `Qwen/Qwen2.5-7B` | `Qwen2ForCausalLM` | 4 | 14.2 GB | **`VERIFIED_LIVE`** |
| **$t = 224$** | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_224` | `1833fa4e7beea19c2451e1f7a4dfe3068454edaf` | `Qwen/Qwen2.5-7B` | `Qwen2ForCausalLM` | 4 | 14.2 GB | **`VERIFIED_LIVE`** |

---

## 2. Lineage Compatibility Verification

1. **Architecture Uniformity**: All 7 checkpoints use `Qwen2ForCausalLM` architecture with 7.61B parameters, 28 layers, 28 attention heads, 4 KV heads, and hidden size 3584.
2. **Tokenizer Compatibility**: 100% tokenization vocabulary parity with `Qwen/Qwen2.5-7B`.
3. **Weight Integrity**: 4 safetensors shards per checkpoint, total size ~14.2 GB per checkpoint.

*Signed by ML Systems Engineer & Reproducibility Auditor*
