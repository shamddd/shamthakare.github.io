# STATESHIFT PROSPECTIVE STUDY PROTOCOL & HYPOTHESIS REGISTRATION (V3 SEALED)

**Protocol Version**: `Phase 1H Prospective Release 3.0`  
**Registration Date**: `2026-08-17`  
**Execution Status**: **`DRAFTED & FROZEN; SCIENTIFIC EXECUTION ON HOLD`**  
**Confirmatory Registry V3 Hash**: `d95c1d7b6f6132733f9e778ef7d67cd8001ac4b30652ac5b83fc96053a0b8941`  
**Strict Sensitivity Registry Hash**: `ff57926a32b84a4e975d4d38977333662ae5b6c39b04e5613ddb9b30ed4df7f8`  

---

## 1. EXECUTIVE SUMMARY & STUDY DESIGN

The **StateShift** experiment measures whether reinforcement learning fine-tuning increases a language model's ability to recover from controlled, locally invalid intermediate reasoning states ($S_R$) relative to valid reference states ($S_C$) during mathematical derivation.

### 1.1 Primary Study Invariants

1. **Primary Estimand ($\Gamma_t$)**:
   $$\Gamma_t = \left(\mu_{R,t} - \mu_{R,0}\right) - \left(\mu_{C,t} - \mu_{C,0}\right)$$
   where:
   - $\mu_{R,t}$ is the mean target transition success rate for Recovery Perturbed states ($S_R$) at RL checkpoint $t$.
   - $\mu_{C,t}$ is the mean target transition success rate for Control Valid reference states ($S_C$) at RL checkpoint $t$.
   - $\mu_{R,0}$ and $\mu_{C,0}$ are baseline success rates at base model initialization $t=0$.

2. **Primary Scalar Endpoint**:
   Scalar interaction $\Gamma_T$ at final RL checkpoint $T=256$.

3. **Confirmatory Sample Size**:
   Post-Human Certified Registry $N = 456$ decontaminated problem pairs (`FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V3.json`).

4. **Strict Sensitivity Subset**:
   Strict Registry $N = 398$ pairs excluding `POSSIBLE_RELATED` contamination items (`FINAL_PROSPECTIVE_STATE_REGISTRY_STRICT_CONTAMINATION_V4.json`).

5. **Rollout Allocation**:
   $K = 16$ independent stochastic rollouts per state per checkpoint ($T_s = 0.6$, top_p $= 0.95$, max_tokens $= 2048$).

6. **Inference Resampling Procedure**:
   $B = 10,000$ problem-blocked bootstrap replicates resampling problems with all states and rollouts intact.

---

## 2. CHECKPOINT TRAJECTORY SPECIFICATION

The study evaluates the public UWNSL Qwen2.5-7B DeepScaleR 4K Temporal Sampling trajectory across 9 discrete checkpoints:

| Step ($t$) | Model Name | Hugging Face Repository ID | Immutable Revision SHA |
| :---: | :---: | :--- | :--- |
| **0** | `pi_0` | `Qwen/Qwen2.5-7B` | `d149729398750b98c0af14eb82c78cfe92750796` |
| **32** | `pi_32` | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_32` | `f46f9eac9908013a502735b7e882821f492ca61e` |
| **64** | `pi_64` | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_64` | `d57afa929761825af618c6545ab7f7a5b28b3dc1` |
| **96** | `pi_96` | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_96` | `5164cb6d7dcace900aed6a961cea33de40f2b6dc` |
| **128** | `pi_128` | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_128` | `27d9d8455a50c0cb0af37e9676bac4e2a1ecddec` |
| **160** | `pi_160` | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_160` | `d8df8a5d6290bcc7b4b5fa108121cc5b9808bf58` |
| **192** | `pi_192` | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_192` | `cb3f9bda37c44699246d04b9af21df41879e0ac3` |
| **224** | `pi_224` | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_224` | `1833fa4e7beea19c2451e1f7a4dfe3068454edaf` |
| **256** | `pi_256` | `UWNSL/Qwen2.5-7B-deepscaler_4k_step_256` | `7667ad787966f5733fdca3d2b240452d7095ff95` |

---

## 3. STATISTICAL INFERENCE & HYPOTHESIS TESTING

### 3.1 Primary Hypothesis Test (Option A Descriptive Inference)
- **Primary Endpoint**: Scalar interaction point estimate $\hat{\Gamma}_T$ at $T=256$.
- **Interval Estimation**: 95% non-parametric BC_a / percentile confidence interval $[\hat{\Gamma}_{T,0.025}, \hat{\Gamma}_{T,0.975}]$ computed via $B=10,000$ problem-blocked bootstrap replicates.
- **Descriptive Trajectory**: Intermediate values $\hat{\Gamma}_t$ ($t=32 \dots 224$) are presented descriptively as interaction curves with 95% point-wise confidence bands.

### 3.2 Sensitivity Analyses
1. **Strict Decontamination Subset**: Re-evaluate $\Gamma_T$ on $N=398$ strict subset.
2. **Operator Stratification**: Compute $\Gamma_{T,\text{op}}$ across `OP_CONSTANT_PERTURB`, `OP_SIGN_FLIP`, and `OP_FRACTION_FLIP`.

---

## 4. PROTOCOL EXECUTION BOUNDARY & SCIENTIFIC HOLD DIRECTIVE

> [!CAUTION]
> **MANDATORY EXECUTION DIRECTIVE**:
> This protocol document formally freezes all StateShift study parameters. However, **scientific execution (checkpoint downloads, technical canary runs, and model inference) is strictly ON HOLD until human adjudication gate verification is complete.**

---
*Signed by StateShift Principal Investigators, Lead Auditor & Research Statistician*
