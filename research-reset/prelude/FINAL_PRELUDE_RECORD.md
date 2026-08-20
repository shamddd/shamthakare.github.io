# FINAL PRELUDE RECORD: IMMUTABLE SCIENTIFIC & GOVERNANCE SUMMARY

**Date**: August 16, 2026  
**Auditing Entity**: Antigravity Forensic Research Agent  
**Status**: PROJECT PERMANENTLY TERMINATED  

---

## 1. QUESTION TESTED

$$\text{Do frozen internal model-state diagnostics explain residual variation in marginal RLVR gains beyond strong behavioral, training-history, and task-difficulty predictors, and does this incremental information transfer to unseen model families?}$$

Specifically, we evaluated whether pre-RL model-state features ($I$) provide incremental predictive accuracy for compute-normalized marginal RLVR gain:
$$\Delta_{\mathrm{RLVR}}(M, D, C) = U(\mathcal{T}_{\mathrm{RLVR}}(M, D, C), D_{\mathrm{test}}) - U(M, D_{\text{test}})$$
beyond strong behavioral baselines ($B$) and headroom/training-history predictors ($H$).

---

## 2. TESTED INTERNAL DIAGNOSTIC FEATURES ($I$)

1. **Reward Probe Separability**: Logistic regression AUROC and $R^2$ on rollout representations.
2. **Residual Stream Effective Rank**: $\text{erank}(\Sigma) = \exp(-\sum p_i \ln p_i)$ on centered residual activations.
3. **Stable Rank**: $\text{srank}(\Sigma) = \|\Sigma\|_F^2 / \|\Sigma\|_2^2$.
4. **Micro-Batch Gradient Norms**: Mean gradient norm $\|g\|$ across micro-batches.
5. **Gradient Noise Scale Proxy**: $\text{GNS} = \text{Var}(g) / \|E[g]\|^2$.
6. **LayerNorm Gradient Ratio**: Magnitude ratio $\|g_{\text{LN}}\| / \|g_{\text{out}}\|$.

---

## 3. PRIMARY SCIENTIFIC RESULTS (PHASE B0 PILOT)

Across 18 controlled RLVR pilot runs spanning 3 model families (SmolLM2-360M, Pythia-410M, Qwen2.5-0.5B), 6 pretraining checkpoints, 2 reasoning task conditions, and 3 seed replications:

1. **Baseline Model $M_1$ ($BH$) Performance**: Achieved held-out-family Mean Absolute Error $\text{MAE} = 0.0090$ and Spearman $\rho = -0.028$.
2. **Full Model $M_5$ ($BH + I$) Performance**: Achieved held-out-family $\text{MAE} = 0.0101$ and Spearman $\rho = 0.049$.
3. **Primary Incremental Gain**: $\Delta\text{MAE} = \text{MAE}_{M1} - \text{MAE}_{M5} = -0.0011$.
4. **Per-Family Incremental MAE**:
   - SmolLM2: $\Delta\text{MAE} = -0.0018$
   - Pythia: $\Delta\text{MAE} = -0.0004$
   - Qwen: $\Delta\text{MAE} = -0.0010$
5. **Residual Structure**: Spearman correlation of internal features with baseline prediction errors $r = \Delta_{\text{RLVR}} - \hat{\Delta}_{\text{BH}}$ was near zero or slightly negative (Probe: $\rho = -0.042$; $\text{erank}$: $\rho = -0.014$; GNS: $\rho = -0.028$). Zero residual structure was explained by internal features.

---

## 4. SCIENTIFIC SCOPE LIMITATION

> **Precise Scope Statement**: Within the tested model families (SmolLM2, Pythia, Qwen2.5 up to 0.5B scale), verifiable mathematical reasoning tasks (GSM8K, SVAMP), standardized 150-step GRPO protocol, and evaluated diagnostic set, **no detectable incremental predictive value was observed for frozen internal model diagnostics beyond behavioral and headroom baselines**.

This finding does not prove that internal representation features can never predict any fine-tuning task under any objective; rather, it establishes that for predicting marginal RLVR reasoning gains under strict cross-family validation, behavioral proxies and failure-rate headroom capture the usable signal, while internal diagnostics add no non-redundant predictive power.

---

## 5. GOVERNANCE OUTCOME & ARCHIVAL

* **Decision**: PRELUDE was permanently terminated prior to confirmatory scaling because the pre-registered pilot failed to demonstrate positive incremental predictive value ($\Delta\text{MAE} > 0.005$).
* **Data Integrity**: All 18 run manifests, raw generation outputs, telemetry logs, design matrices, pre-registration specifications, and forensic audit reports have been archived immutably in `research-reset/prelude/NEGATIVE_RESULT_PACKAGE/`. Zero raw files were modified or deleted.
