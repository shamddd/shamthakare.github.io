# PHASE B: GO / REFORMULATE DECISION & B0 PILOT DESIGN

**Date**: August 16, 2026  
**Auditing Entity**: Antigravity Forensic Research Agent  
**Subject**: Transition Recommendation for **PRELUDE v1**  
**Flagship Scientific Objective**:
$$\boxed{\Large \text{Do frozen internal diagnostics explain residual variation in marginal RLVR gains beyond strong behavioral, training-history, and task-difficulty predictors?}}$$

---

## 1. CURRENT GOVERNANCE DECISION

$$\boxed{\Huge \textbf{REFORMULATE EXPERIMENTAL DESIGN}}$$

### Executive Summary:
1. **FULL PHASE B MATRIX (N=48) NOT AUTHORIZED**: Proceeding directly to a 48-run matrix without empirical variance components is scientifically unwarranted.
2. **PHASE B0 PILOT AUTHORIZED (N=12)**: A controlled 12-run pilot across 3 model families (SmolLM2, Pythia, Qwen2.5), 2 checkpoints per family, 2 task conditions, and 1 RL seed is specified to measure empirical variance components and baseline predictability.
3. **PRE-REGISTRATION LOCKED**: The Phase B0 analytical protocol is locked in [`PHASE_B0_ANALYSIS.md`](file:///Users/shamthakare/.gemini/antigravity/scratch/research/prelude_v1/preregistration/PHASE_B0_ANALYSIS.md) with cryptographic SHA-256 digest `8825f5807952b1476e6412395b29c3244f650a5b1c73cfb4452353c102c6ff6d`.

---

## 2. PHASE B0 EXPERIMENTAL SPECIFICATION (12 RUNS)

```
+----------------------------------------------------------------------------------------------------+
|                                    PHASE B0 PILOT MATRIX SPECIFICATION                             |
+----------------------+--------------------+--------------------+-----------------------------------+
| Model Family         | Model Scale        | Checkpoint Steps   | Tasks (1 Seed)                    |
+----------------------+--------------------+--------------------+-----------------------------------+
| SmolLM2              | SmolLM2-360M       | Step 50k, Step 100k| GSM8K-Easy, GSM8K-Hard (4 runs)   |
| Pythia               | Pythia-410M        | Step 50k, Step 143k| GSM8K-Easy, GSM8K-Hard (4 runs)   |
| Qwen                 | Qwen2.5-0.5B       | Step 50k, Final    | GSM8K-Easy, GSM8K-Hard (4 runs)   |
+----------------------+--------------------+--------------------+-----------------------------------+
| Total Pilot Runs     | 3 Families, 6 Ckpts| 12 Controlled Runs | ~15.5 GPU-Hours Budget            |
+----------------------+--------------------+--------------------+-----------------------------------+
```

---

## 3. THREE FEATURE BLOCKS & PRIMARY TEST

* **$B$ (Behavioral Baselines)**: Pass@1, Pass@8, Pass@64, prompt NLL, held-out generalization loss, sampled solution coverage $\hat{p}_K$, token entropy, model scale $P$, token count $T$.
* **$H$ (Headroom & History)**: Pretraining step age, performance ceiling distance ($1 - \text{Pass@1}$), task difficulty tier, edge-of-competence ($1 - \text{Pass@64}$), SFT status.
* **$I$ (Internal Diagnostics)**: Effective rank ($\text{erank}$), stable rank ($\text{srank}$), linear reward probe AUROC/$R^2$, gradient norms, GNS proxy, LayerNorm gradient ratio.

### Primary Comparison:
$$\text{Model BHI } [f(B, H, I)] \quad \text{vs.} \quad \text{Model BH } [f(B, H)]$$
Evaluating incremental out-of-family predictive value ($\Delta \text{MAE}$, Spearman $\rho$, Kendall $\tau$, sign accuracy, regret).

---

## 4. PHASE B0 KILL CONDITIONS (K1 through K7)

Phase B0 will terminate with a **NO-GO** or mandatory reformulation if:
* **K1**: $\Delta_{\text{RLVR}}$ variance $< 0.001$ across checkpoints.
* **K2**: Model BH predicts post-RL gain with $\text{MAE} < 0.01$ or $\rho > 0.95$.
* **K3**: Internal metrics fail or yield $\text{NaN}/\text{Inf}$ on $>5\%$ of checkpoints.
* **K4**: Internal features $I_j$ are collinear with $(B, H)$ ($R^2 > 0.90$).
* **K5**: $\text{MAE}_{\text{BHI}} \ge \text{MAE}_{\text{BH}}$ under LOMFO-CV.
* **K6**: Rollout seed variance exceeds checkpoint gain variance by $>3.0\times$.
* **K7**: Runtime diverges from Phase A calibration by $>2.5\times$.

---

## 5. REQUIRED POST-B0 DELIVERABLES & RECOMMENDATION OPTIONS

After Phase B0 pilot execution, the system must produce:
1. `PHASE_B0_RESULTS.json`
2. `PHASE_B0_VARIANCE_ANALYSIS.md`
3. `PHASE_B0_DIAGNOSTIC_STABILITY.md`
4. `PHASE_B0_BASELINE_STRENGTH.md`
5. `PHASE_B0_GO_NO_GO.md`

Ending in **exactly one** decision recommendation:
* **`GO — EXPAND TO CONFIRMATORY MATRIX`**
* **`REFORMULATE — SIGNAL/POWER INSUFFICIENT`**
* **`NO-GO — INTERNAL DIAGNOSTICS ADD NO PLAUSIBLE VALUE`**

**STOPPING ACTION**: Execution is halted. Neither Phase B0 nor Phase B will start automatically.
