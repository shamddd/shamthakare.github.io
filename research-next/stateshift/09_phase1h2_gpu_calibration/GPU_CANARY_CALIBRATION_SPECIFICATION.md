# STATESHIFT PHASE 1H.2 — GPU FEASIBILITY CALIBRATION SPECIFICATION (V2 REVISED)

**Protocol Version**: `Phase 1H.2 Release 2.0`  
**Registration Date**: `2026-08-19`  
**Execution Status**: **`PREPARED & SPECIFIED; AWAITING TARGET GPU ACCELERATOR`**  
**Confirmatory Registry V3 Hash**: `d95c1d7b6f6132733f9e778ef7d67cd8001ac4b30652ac5b83fc96053a0b8941` ($N=456$)  
**Strict Sensitivity Registry Hash**: `d50f18f9391d63901fadf0b4b16069b74e108dc4ab31afeebb7a4a3ab1d541a1` ($N=389$)  

---

## 1. OBJECTIVE & SCIENTIFIC HOLD BOUNDARY

Phase 1H.1 established that serial CPU execution requires ~84,670.26 CPU-hours (~9.67 CPU-years), proving local CPU execution is unfeasible for the full 131,328-rollout experiment. All unvalidated CPU-to-GPU speedup conversion multipliers have been removed.

**Phase 1H.2** calibrates technical feasibility on the actual target GPU accelerator (e.g., NVIDIA A100/H100 or Cloud GPU cluster) before any full experiment launch decision.

> [!CAUTION]
> **FULL EXPERIMENT LAUNCH HOLD**:  
> The 131,328-rollout confirmatory experiment remains strictly on **HOLD**. Full launch is prohibited until empirical GPU calibration metrics (load time, tokens/sec per rollout, VRAM, latency) are measured on the target GPU platform.

---

## 2. FROZEN CALIBRATION BENCHMARK DESIGN ($N=16$ Rollouts)

To preserve prospective scientific separation, **ZERO items from the 456-pair confirmatory registry are accessed**. Calibration evaluates the synthetic item with $K=4$ rollouts per state per checkpoint to capture throughput variance:

- **Canary Item ID**: `synthetic_canary_001`
- **Question Text**: `"A box contains 12 red balls and 8 blue balls. How many balls are there?"`
- **Control Prefix ($S_C$)**: `"12 + 8 = 20."`
- **Recovery Prefix ($S_R$)**: `"12 - 8 = 20."`
- **Record Type Tag**: `record_type = "technical_canary"`
- **Allocation**: 2 Checkpoints ($t=0, t=256$) $\times$ 2 States ($S_C, S_R$) $\times K=4$ rollouts = **exactly 16 GPU calibration rollouts**.

---

## 3. CHECKPOINTS & COMPREHENSIVE HARDWARE METRICS REQUIREMENT

| Checkpoint Step ($t$) | Model Name | Hugging Face Repository | Immutable Revision SHA |
| :---: | :---: | :--- | :--- |
| **0** | `pi_0` | `Qwen/Qwen2.5-7B` | `d149729398750b98c0af14eb82c78cfe92750796` |
| **256** | `pi_256` | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_256` | `7667ad787966f5733fdca3d2b240452d7095ff95` |

### Required Forensic GPU & Environment Parameters to Record:
1. **GPU Hardware Identity**: GPU device name, device count, and Compute Capability.
2. **Software Toolchain Versions**: CUDA driver version, PyTorch version, `transformers` version.
3. **Execution Configuration**: `dtype` (`float16` / `bfloat16`), `device_map`, attention implementation (`sdpa` / `flash_attention_2`), model quantization state (none / 8-bit / 4-bit), KV cache status (`use_cache=True`).
4. **VRAM Memory Allocation**:
   - `torch.cuda.memory_allocated()`
   - `torch.cuda.max_memory_allocated()`
   - `torch.cuda.memory_reserved()`
5. **Rollout Latency & Per-Rollout Token Throughput**:
   - Model load duration per checkpoint.
   - Warmup rollout duration vs measured rollouts.
   - Individual tokens/sec and total generation duration for each rollout $k \in \{1 \dots 4\}$.
6. **Token Roundtrip Verification**: `tokenizer.decode(output_token_ids) == decoded_text` for 16/16 generations.

---

## 4. GPU FEASIBILITY EXTRAPOLATION FORMULA

From the 16 measured GPU rollout durations, calculate:

$$\text{Extrapolated GPU-Hours (Mean)} = \frac{\text{Mean GPU Generation Seconds} \times 131,328}{3600}$$

$$\text{Extrapolated GPU-Hours (Median)} = \frac{\text{Median GPU Generation Seconds} \times 131,328}{3600}$$

$$\text{Single Checkpoint GPU-Hours} = \frac{\text{Mean GPU Generation Seconds} \times 14,592}{3600}$$

$$\text{Extrapolated JSONL Storage} = \frac{\text{Mean Bytes / Record} \times 131,328}{1024^3} \text{ (GB)}$$

---

## 5. GO / REDESIGN / NO-GO FEASIBILITY THRESHOLDS

Upon executing GPU calibration on the target GPU hardware:

- **`GO`**: Measured total GPU-hours $\le 250$ GPU-hours and peak VRAM $\le 80$ GB per device.
- **`REDESIGN`**: Measured GPU-hours $> 250$ GPU-hours (requires adjusting $K$ or max_tokens via pre-execution protocol amendment).
- **`NO-GO`**: System OOM or model loading failure on GPU target platform.

---
*Signed by Lead ML Systems Engineer, Research Statistician & Scientific Integrity Auditor*
