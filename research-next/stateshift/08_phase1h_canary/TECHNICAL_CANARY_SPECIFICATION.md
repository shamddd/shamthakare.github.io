# STATESHIFT TECHNICAL CHECKPOINT CANARY PHASE SPECIFICATION

**Protocol Version**: `Phase 1H Canary Release 1.0`  
**Date**: `2026-08-17`  
**Execution Status**: **`READY FOR BENCHMARKING`**  
**Confirmatory Registry Hash**: `d95c1d7b6f6132733f9e778ef7d67cd8001ac4b30652ac5b83fc96053a0b8941`  

---

## 1. CANARY PHASE GOALS & BENCHMARK PARAMETERS

Before launching full inference across all 131,328 rollouts, the **Technical Checkpoint Canary Phase** benchmarks technical feasibility and system resource consumption on a minimal 1-problem canary slice:

1. **Canary Slice Size**: 1 Problem Pair (`math500_001`, Pair ID `pair_math500_001`)
2. **State Subsets**: 2 States ($S_C$ Control Valid, $S_R$ Recovery Perturbed)
3. **Checkpoint Subsets**: 2 Checkpoints ($t=0$ Base `Qwen/Qwen2.5-7B`, $t=256$ Final `UWNSL/Qwen2.5-7B-deepscaler_4k_step_256`)
4. **Canary Rollouts**: $K = 2$ rollouts per state per checkpoint ($2 \times 2 \times 2 = 8$ canary rollouts)

---

## 2. BENCHMARK METRICS TO MEASURE

The canary benchmark script records:
- **Model Load Time**: Time required to download/load weights into VRAM per 7B checkpoint.
- **Inference Latency**: Average time per generation token and total time per rollout.
- **Memory Consumption**: Peak GPU VRAM allocated during 7B forward pass & generation.
- **Storage Extrapolation**: Disk space required per JSON rollout file.
- **Full Run Extrapolation**: Extrapolated total GPU-hours and disk storage required for all **131,328** neural rollouts ($456 \text{ pairs} \times 2 \text{ states} \times 9 \text{ checkpoints} \times 16 \text{ rollouts}$).

---

## 3. CANARY HARDWARE & ENVIRONMENT REQUIREMENTS

- **Device**: Metal / MPS / CUDA GPU or CPU fallback
- **Dependencies**: `transformers`, `torch`, `huggingface_hub`
- **Output Storage**: Log files recorded under `research-next/stateshift/08_phase1h_canary/canary_benchmark_results.json`

---
*Signed by StateShift Lead Technical Engineer & Research Statistician*
