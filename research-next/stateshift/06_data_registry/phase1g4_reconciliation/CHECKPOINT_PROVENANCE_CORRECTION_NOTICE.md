# CHECKPOINT PROVENANCE METADATA CORRECTION NOTICE

**Target Checkpoint Series**: UWNSL Temporal Sampling Trajectory ($t \in \{0, 32, \dots, 256\}$)  

---

## Technical Metadata Reconciliation

- **Context Window / Max Position Embeddings**:
  - Checkpoints $t=32 \dots 256$ in the official `UWNSL/Qwen2.5-7B-deepscaler_4k_step_*` Hugging Face repositories expose **`max_position_embeddings = 131072`** (131k tokens) in their `config.json`.
  - Base checkpoint `Qwen/Qwen2.5-7B` exposes standard $32,768$ (32k) position embeddings.
- **Architectural Parameter Invariance**:
  - Model class: `Qwen2ForCausalLM`
  - Parameter count: `7.61B`
  - Layers: `28`
  - Attention heads: `28`
  - Hidden dimension: `3584`
  - Vocabulary size: `152064`

> [!IMPORTANT]
> **Manuscript Configuration Note**:
> All manuscript and preregistration configuration statements shall report `131,072` position embeddings for the UWNSL step-32 through step-256 checkpoints, correcting any previous general 32k context assumption.

---
