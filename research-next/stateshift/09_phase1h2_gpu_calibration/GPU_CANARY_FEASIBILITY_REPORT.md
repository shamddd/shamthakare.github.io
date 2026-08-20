# PHASE 1H.2 GPU FEASIBILITY CALIBRATION REPORT (V3 RECONCILED)

**Milestone**: Phase 1H.2 Empirical GPU Feasibility Calibration  
**Execution Timestamp**: `2026-08-18 21:24 UTC`  
**Hardware Accelerator**: `NVIDIA A100-SXM4-80GB` (Count: `1`, Compute Capability: `8.0`)  
**Driver & CUDA Version**: Driver `570.172.08` | CUDA Toolkit `12.4`  
**Software Stack**: PyTorch `2.4.1+cu124` | Transformers `4.46.3`  
**Measured Generations Completed**: **`16 / 16`** (+ 2 Warmup Generations, 100% Real CUDA PyTorch `model.generate()`)  
**Scientific Firewall Status**: **`PASSED & VERIFIED`**  

---

## 1. Measured Empirical GPU Benchmark Performance ($N=16$ Measured Rollouts)

| Benchmark Metric | Checkpoint $t=0$ (`Qwen2.5-7B`) | Checkpoint $t=256$ (`DeepScaleR-7B`) | Combined GPU Benchmark |
| :--- | :---: | :---: | :---: |
| **Model Load Duration** | `9.33s` | `65.25s` | `74.57s` |
| **Mean Generation Duration** | `0.8666s` | `0.9477s` | **`0.9072s`** |
| **Median Generation Duration** | — | — | **`0.7625s`** |
| **Mean Generated Tokens** | `42.9` | `42.5` | **`42.7` tokens** |
| **Mean Token Speed** | `49.4 tok/s` | `44.6 tok/s` | **`47.0 tok/s`** |
| **Peak VRAM Allocated Across Devices** | — | — | **`14.25 GB`** |

---

## 2. Empirical Full Experiment Feasibility Extrapolations ($N=131,328$ Rollouts)

Extrapolated metrics for the full confirmatory design (456 pairs x 2 states x 9 checkpoints x 16 rollouts = 131,328 generations):

- **Estimated Total GPU-Hours (Mean)**: **`33.09 GPU-Hours`**
- **Estimated Total GPU-Hours (Median)**: **`27.81 GPU-Hours`**
- **Estimated Total Generated Tokens**: **`5,606,064 tokens`**
- **Estimated Raw JSONL Storage Size**: **`0.33 GB`**

### Single Checkpoint Extrapolation ($N=14,592$ Rollouts)
- **Single Checkpoint Generation Duration**: **`3.68 GPU-Hours`**
- **Single Checkpoint Disk Storage**: **`0.04 GB`**

---

## 3. Anti-Simulation & Invariant Audit Results

1. **CUDA Accelerator Test**: `PASSED` (`torch.cuda.is_available() == True`).
2. **Model Instantiation Test**: `PASSED` (`AutoModelForCausalLM` instantiated `Qwen2ForCausalLM` with `7.615B` parameters).
3. **Warmup Allocation Test**: `PASSED` (Exactly 1 warmup generation per checkpoint executed prior to state loops and excluded from statistics).
4. **Independent Post-Persistence Token Provenance Audit**: `PASSED` (All 16 measured records reloaded from disk and verified via token ID SHA-256 match and fresh tokenizer decoding).
5. **Scientific Firewall Test**: `PASSED` (`record_type == "technical_canary"` firewalled from scientific pipeline).

---

## 4. PREREGISTERED FEASIBILITY THRESHOLD VERDICT

**Official Automated Verdict**: **`GO — GPU FEASIBILITY VERIFIED; CONFIRMATORY LAUNCH ELIGIBLE FOR SEPARATE AUTHORIZATION`** (Verdict Code: `GO`)

- **Empirical GPU-Hours Evaluation**: `33.09 GPU-Hours` vs Threshold <= 250.0 GPU-Hours.
- **Peak VRAM Evaluation**: `14.25 GB` vs Threshold <= 80.0 GB per device.

> [!IMPORTANT]
> **GOVERNANCE DIRECTIVE**:  
> The automated verdict evaluates technical compute feasibility. Confirmatory experiment launch remains strictly on **HOLD** pending explicit human principal authorization.

---
*Signed by Lead ML Systems Engineer, Research Statistician & Scientific Integrity Auditor*
