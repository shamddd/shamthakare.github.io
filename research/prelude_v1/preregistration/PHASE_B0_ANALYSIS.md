# PRE-REGISTRATION SPECIFICATION: PHASE B0 EXPLORATORY PILOT

**Date**: August 16, 2026  
**Registration Authority**: Antigravity Forensic Research Unit  
**Status**: LOCKED PRE-REGISTRATION (PHASE B0)  
**Target Scope**: 12 Controlled RLVR Pilot Runs across 3 Model Families, 2 Checkpoints per Family, 2 Task Conditions, 1 Seed.

---

## 1. SCIENTIFIC OBJECTIVE & TARGET FORMULATION

We pre-register the primary scientific objective for Phase B0:

$$\boxed{\Large \text{Do frozen internal model-state diagnostics explain residual variation in marginal RLVR gains beyond strong behavioral, training-history, and task-difficulty predictors?}}$$

### Target Variable Definition:
$$\Delta_{\mathrm{RLVR}}(M, D, C) = U(\mathcal{T}_{\mathrm{RLVR}}(M, D, C), D_{\mathrm{test}}) - U(M, D_{\mathrm{test}})$$
where:
* $M$: Pre-RL checkpoint
* $D$: Reasoning task distribution (GSM8K-Easy, GSM8K-Hard, SVAMP)
* $C$: Fixed RL compute budget (150 GRPO steps)
* $T_{\text{RLVR}}$: Standardized RLVR training operator
* $U$: Verification accuracy on held-out test split $D_{\text{test}}$

---

## 2. FEATURE FAMILIES (B, H, I)

### Family B — Behavioral / Observable Features:
1. `base_pass_at_1`: Greedy evaluation accuracy on prompt set
2. `base_pass_at_8`: Sampled pass rate ($k=8$, temperature $0.7$)
3. `base_pass_at_64`: Sampled pass rate ($k=64$, temperature $0.7$)
4. `prompt_nll`: Average prompt negative log-likelihood
5. `heldout_generalization_loss`: Cross-entropy loss on held-out reasoning set
6. `sampled_solution_coverage`: $\hat{p}_K(M, D) = \frac{1}{nK} \sum_{i=1}^n \sum_{j=1}^K \mathbf{1}[r(x_i, y_{ij}) = 1]$
7. `mean_token_entropy`: Completion token entropy
8. `model_scale_params`: Total parameter count $P$
9. `pretrain_token_count`: Cumulative pretraining tokens $T$
10. `base_calibration_error`: Expected Calibration Error (ECE) of base model

### Family H — Headroom & Training-History Features:
1. `pretrain_checkpoint_step`: Training step number of checkpoint
2. `performance_ceiling_distance`: $1.0 - \text{Pass@1}$
3. `task_difficulty_tier`: Categorical tier (1=Easy, 2=Hard, 3=Out-of-Distribution Shift)
4. `edge_of_competence`: $1.0 - \text{Pass@64}$
5. `sft_exposure_status`: Boolean indicator of SFT prior
6. `training_data_exposure`: Known data domain fraction

### Family I — Internal Diagnostics (Candidate Contribution):
1. `residual_effective_rank`: $\text{erank}(\Sigma) = \exp(-\sum p_i \ln p_i)$ on residual stream covariance
2. `residual_stable_rank`: $\text{srank}(\Sigma) = \|\Sigma\|_F^2 / \|\Sigma\|_2^2$
3. `singular_value_top_ratio`: $\sigma_1 / \sum \sigma_i$
4. `reward_probe_auroc`: Logistic regression AUROC on rollout representations
5. `reward_probe_r2`: Linear probe $R^2$ on rollout representations
6. `microbatch_gradient_norm`: Mean gradient norm across micro-batches
7. `gradient_noise_scale`: GNS proxy $\text{Var}(g) / \|E[g]\|^2$
8. `layernorm_to_output_grad_ratio`: Gradient magnitude ratio $\|g_{\text{LN}}\| / \|g_{\text{out}}\|$

---

## 3. PRIMARY MODEL COMPARISON & METRICS

We evaluate low-capacity Ridge regression models under Leave-One-Model-Family-Out Cross-Validation (LOMFO-CV):

$$\begin{aligned}
\text{Model } B: \quad \hat{\Delta} &= f(B) \\
\text{Model } BH: \quad \hat{\Delta} &= f(B, H) \\
\text{Model } BHI: \quad \hat{\Delta} &= f(B, H, I)
\end{aligned}$$

### Primary Test:
**Model BHI vs. Model BH**

### Locked Metrics:
1. Held-out-family Mean Absolute Error ($\text{MAE}_{\text{BHI}}$ vs $\text{MAE}_{\text{BH}}$)
2. Held-out-family Spearman rank correlation ($\rho_{\text{BHI}}$ vs $\rho_{\text{BH}}$) and Kendall $\tau$
3. Sign accuracy ($\mathbf{1}[\text{sign}(\hat{\Delta}) == \text{sign}(\Delta)]$)\
4. Regret under fixed budget (opportunity cost of incorrect RL deployment decisions)
5. Paired prediction-error difference ($\text{MAE}_{\text{BH}} - \text{MAE}_{\text{BHI}}$)

---

## 4. STANDARDIZED RLVR OPERATOR HYPERPARAMETERS

All Phase B0 pilot runs enforce locked, un-tuned hyperparameters:
* **Algorithm**: Group Relative Policy Optimization (GRPO)
* **Optimizer**: AdamW ($\beta_1=0.9, \beta_2=0.999$, weight decay $0.01$)
* **Learning Rate**: $1 \times 10^{-5}$ (constant schedule with 5-step warmup)
* **KL Regularization**: $\beta_{\text{KL}} = 0.04$
* **Sampling**: Temperature $0.7$, Top-$p$ $0.95$, Group size $G = 8$
* **Max Generation Length**: $L_{\text{gen}} = 256$ tokens
* **Optimization Steps**: 150 steps
* **Prompts per Step**: 1 prompt per step ($G=8$ rollouts per prompt)
* **Verifier**: Deterministic mathematical equivalence parser (`math_verifier.py`)

---

## 5. PHASE B0 KILL CONDITIONS (K1 through K7)

If any of the following 7 conditions occur during Phase B0, the project or hypothesis will be declared invalid or subject to mandatory reformulation:

* **K1 (Constancy)**: True marginal gain $\Delta_{\text{RLVR}}$ has variance $< 0.001$ across all pilot checkpoints and tasks.
* **K2 (Baseline Sufficiency)**: Model BH already achieves held-out MAE $< 0.01$ or Spearman $\rho > 0.95$, leaving no usable residual variance.
* **K3 (Numerical Instability)**: Internal feature extraction fails or produces $\text{NaN}/\text{Inf}$ on $>5\%$ of checkpoints.
* **K4 (Collinearity Redundancy)**: Every feature $I_j \in I$ exhibits $R^2 > 0.90$ when regressed onto $(B, H)$ (merely encoding scale or step age).
* **K5 (Incremental Failure)**: $\text{MAE}_{\text{BHI}} \ge \text{MAE}_{\text{BH}}$ under LOMFO-CV (internal features worsen or add no predictive value).
* **K6 (Seed Instability)**: Multi-seed rollout variance exceeds checkpoint-to-checkpoint variance by $> 3.0\times$.
* **K7 (Compute Divergence)**: Measured wall-clock step time exceeds Phase A calibration by $> 2.5\times$.

---

## 6. PRE-REGISTRATION CRYPTOGRAPHIC HASHING

* **Preregistration File**: `research/prelude_v1/preregistration/PHASE_B0_ANALYSIS.md`
* **Commit Requirement**: Must be committed to git before Phase B0 pilot data collection begins.
