# COMPUTE PLAN — PROJECT A (FLAGSHIP)

**Canonical Project Title**: *C3A: Causal Counterfactual Credit Assignment for Multi-Turn Tool-Using Foundation Agents*  
**Author**: Sham Thakare  
**Date**: August 2026  

---

## 1. Computational Budget & Hardware Constraints

This project is explicitly engineered for **compute realism**, eliminating any requirement for 100+ H100 GPU clusters. All primary empirical claims can be validated on modest, accessible hardware.

### Target Hardware Setup
- **GPU**: 1 $\times$ NVIDIA RTX 4090 (24 GB VRAM) or 1 $\times$ NVIDIA A100 (40/80 GB VRAM).
- **RAM**: 32 GB system memory.
- **Storage**: 100 GB SSD space (for cached trajectories and checkpoints).

---

## 2. Parameter Efficiency & Memory Optimizations

1. **Model Architecture**:
   - `Qwen2.5-1.5B-Instruct` (BF16 base weights: $\approx 3.0$ GB VRAM).
2. **Fine-Tuning Efficiency**:
   - LoRA ($r=16, \alpha=32$): Trainable parameters $\approx 18.4\text{M}$ ($<1.2\%$ of total parameters).
   - Optimizer state (AdamW FP32 for LoRA parameters): $< 150$ MB VRAM.
3. **Activation Caching & FlashAttention**:
   - `FlashAttention-2` enabled with gradient checkpointing.
   - Max context length: 2,048 tokens.
   - Total peak memory during backward pass: $\approx 14.2$ GB VRAM (well within 24 GB budget).

---

## 3. Total GPU-Hour Allocation Budget

| Phase | Description | Model Scale | Runs $\times$ Seeds | GPU-Hours |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 1: Pilot** | Single-seed sanity check & ablation verification | 1.5B | 1 run $\times$ 1 seed | 3.5 hrs |
| **Phase 2: Full Sweep** | C3A vs Standard GRPO vs TCPO vs PPO | 1.5B | 4 methods $\times$ 3 seeds | 32.0 hrs |
| **Phase 3: Controls** | Permuted + Random + Compute-Matched ($G=8$) | 1.5B | 3 controls $\times$ 3 seeds | 24.0 hrs |
| **Phase 4: Stress Tests** | Noise injection & OOD tool evaluation | 1.5B | 2 stress suites | 6.5 hrs |
| **Phase 5: Cross-Arch** | SmolLM-1.7B / Qwen-0.5B validation | 0.5B / 1.7B | 2 models $\times$ 1 seed | 8.0 hrs |
| **TOTAL** | **Full Publication Experiment Suite** | -- | -- | **74.0 GPU-Hours** |

> **Feasibility Assessment**: The entire empirical experimental matrix executes in under **4 days on a single RTX 4090 GPU**, or under **24 hours on a cloud A100 instance** ($\approx \$75\text{--}\$120$ total compute cost).
