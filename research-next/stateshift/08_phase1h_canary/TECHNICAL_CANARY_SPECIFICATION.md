# STATESHIFT TECHNICAL CHECKPOINT CANARY PHASE SPECIFICATION (V2 REVISED)

**Protocol Version**: `Phase 1H Canary Release 2.0`  
**Date**: `2026-08-17`  
**Execution Status**: **`READY FOR BENCHMARKING`**  
**Confirmatory Registry Hash**: `d95c1d7b6f6132733f9e778ef7d67cd8001ac4b30652ac5b83fc96053a0b8941`  

---

## 1. CANARY SEPARATION & SYNTHETIC DATASET SPECIFICATION

To preserve scientific prospective separation, **ZERO items from the 456-pair confirmatory registry are used**. The canary evaluates a non-study synthetic item:

- **Canary Item ID**: `synthetic_canary_001`
- **Question Text**: `"A box contains 12 red balls and 8 blue balls. How many balls are there?"`
- **Control Prefix ($S_C$)**: `"12 + 8 = 20."`
- **Recovery Prefix ($S_R$)**: `"12 - 8 = 20."`
- **Record Type Tag**: `record_type = "technical_canary"`

---

## 2. CANARY DESIGN & CHECKPOINT SELECTION

The canary evaluates **exactly 8 neural generations**:

- **Checkpoints**:
  1. $t=0$: `Qwen/Qwen2.5-7B` (Revision: `d149729398750b98c0af14eb82c78cfe92750796`)
  2. $t=256$: `UWNSL/Qwen2.5-7B-deepscaler_4k_step_256` (Revision: `7667ad787966f5733fdca3d2b240452d7095ff95`)
- **States**: 2 synthetic states ($S_C, S_R$)
- **Rollouts**: $K = 2$ stochastic rollouts per state per checkpoint ($2 \times 2 \times 2 = 8$ total neural rollouts)

---

## 3. FORENSIC RECORD FIELDS & MPS MEMORY SPECIFICATION

Every record must be produced by genuine PyTorch/Hugging Face `AutoModelForCausalLM.from_pretrained` and `model.generate(...)` calls, capturing:

- **Forensic System Metadata**: `record_type`, `canary_id`, `checkpoint_t`, `model_repository`, `resolved_model_revision`, `model_class`, `parameter_count`, `tokenizer_repository`, `tokenizer_revision`, `device`, `dtype`
- **Inputs & Parameters**: `input_text`, `input_token_ids`, `input_token_count`, `input_sha256`, `generation_seed`, `temperature`, `top_p`, `max_new_tokens`
- **Outputs & Latency**: `output_token_ids`, `generated_token_count`, `decoded_generated_text`, `token_roundtrip_verified`, `generation_start_ns`, `generation_end_ns`, `generation_duration_sec`, `tokens_per_sec`, `model_load_duration_sec`
- **Device/Unified Memory (Apple MPS / GPU)**:
  - `torch.mps.current_allocated_memory()` (if available)
  - `torch.mps.driver_allocated_memory()` (if available)
  - Process RSS memory (`psutil.Process().memory_info().rss`)
  - Labeled explicitly as **`device/unified memory`** (NOT VRAM on MPS).

---

## 4. ANTI-SIMULATION AUDIT & SCIENTIFIC FIREWALL

1. **Anti-Simulation Test**: The canary fails if `AutoModelForCausalLM.from_pretrained` or `model.generate` are skipped, if generated token IDs are mocked/template-reconstructed, or if token roundtrip `decode(output_token_ids) != decoded_generated_text`.
2. **Scientific Firewall**: The confirmatory analysis pipeline enforces `record_type == "empirical_confirmatory"` and raises an explicit rejection if `record_type == "technical_canary"` is passed.

---

## 5. COMPUTE & STORAGE EXTRAPOLATION FOR FULL STUDY (131,328 ROLLOUTS)

From the 8 canary rollouts, the feasibility script extrapolates:
- **Device GPU-hours**: $(\text{mean generation sec} \times 131,328) / 3600$
- **Expected Total Generated Tokens**: $\text{mean generated tokens} \times 131,328$
- **Extrapolated Disk Storage**: Serialized JSONL file size $\times 131,328$
- **Single Checkpoint Estimate**: Extrapolation for $14,592$ rollouts ($456 \text{ pairs} \times 2 \text{ states} \times 16 \text{ rollouts}$).

---
*Signed by StateShift Lead Technical Engineer & Research Statistician*
