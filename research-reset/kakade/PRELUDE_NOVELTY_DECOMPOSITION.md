# PRELUDE V1: NOVELTY DECOMPOSITION, FORMULATION & DIAGNOSTIC HIERARCHY

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  
**Artifact**: Formulation Specification for **PRELUDE v1** (*Pre-RLVR Learning Utility Estimation*)

---

## 1. MATHEMATICAL FORMULATION

We define the primary research problem without ungrounded causal vocabulary. PRELUDE v1 is an **algorithm-selection performance prediction problem** for Reinforcement Learning with Verifiable Rewards.

### Core Mathematical Definition:
Let $M$ be a base foundation model checkpoint with parameters $\theta_0$.  
Let $D = (D_{\text{train}}, D_{\text{test}})$ be a target reasoning task distribution equipped with a deterministic ground-truth verification function $r(x, y) \in \{0, 1\}$.  
Let $\mathcal{T}_{\text{RLVR}}$ be a standardized policy gradient post-training operator (e.g., GRPO with fixed hyperparameters) executed for budget $B_{\text{train}}$.

The **true empirical RLVR utility gain** is defined as:
$$\Delta_{\mathrm{RLVR}}(M,D) = U(\mathcal{T}_{\mathrm{RLVR}}(M,D_{\mathrm{train}}), D_{\mathrm{test}}) - U(M, D_{\mathrm{test}})$$
where $U(M', D_{\text{test}}) = \mathbb{E}_{(x, y) \sim D_{\text{test}}} [r(x, M'(x))]$ is the pass@1 evaluation accuracy.

### Two Complementary Prediction Targets:
1. **Continuous Gain Regression Target**:
   $$\text{Predict } \hat{\Delta}_{\text{RLVR}}(M, D) \approx \Delta_{\text{RLVR}}(M, D)$$
   *Evaluation Metrics*: Kendall’s rank correlation $\tau$, Spearman’s $\rho$, and Mean Absolute Error (MAE).
2. **Binary Decision Classification Target**:
   $$Y = \mathbf{1}[\Delta_{\mathrm{RLVR}}(M, D) > \epsilon]$$
   where $\epsilon \ge 0$ is the practitioner's minimum acceptable improvement threshold (e.g., $\epsilon = 0.05$ or $+5\%$).
   *Evaluation Metrics*: Area Under ROC Curve (AUROC), Brier calibration score, and Classification F1.
   *Practical Value*: Solves the high-value practical question: **"Is this model checkpoint worth spending compute on for RLVR?"**

---

## 2. THE FIVE-LEVEL DIAGNOSTIC HIERARCHY

To rigorously determine which pre-training signals contain predictive information about eventual RLVR reasoning gains, we structure diagnostic features into an explicit five-level hierarchy:

```
+----------------------------------------------------------------------------------------------------+
|                                FIVE-LEVEL PRE-RL DIAGNOSTIC HIERARCHY                              |
+-------+-----------------------------+--------------------------------------------------------------+
| Level | Diagnostic Category         | Specific Mathematical Indicators Evaluated at t = 0          |
+-------+-----------------------------+--------------------------------------------------------------+
| L1    | Cheap / Base Baselines      | 1. Base test pass@1 accuracy: U(M, D_test)                   |
|       |                             | 2. Target prompt NLL / cross-entropy loss: L_NLL(M, D)       |
|       |                             | 3. Mean token entropy: H(M(x)) = - sum p(v) log p(v)         |
|       |                             | 4. Model scale (Parameter count P)                           |
+-------+-----------------------------+--------------------------------------------------------------+
| L2    | Generative Support          | 1. Latent solution coverage: p_0 = P(at least 1 of k passes) |
|       | Diagnostics                 | 2. Pass@k curve slope from k=1 to k=16                       |
|       |                             | 3. Linear reward probe separability (AUROC on rollouts)      |
+-------+-----------------------------+--------------------------------------------------------------+
| L3    | Representation Geometry     | 1. Residual stream effective rank: erank(Sigma)              |
|       | Diagnostics                 | 2. Stable rank: srank(Sigma) = ||Sigma||_F^2 / ||Sigma||_2^2 |
|       |                             | 3. Condition number of top-k covariance subspace             |
+-------+-----------------------------+--------------------------------------------------------------+
| L4    | Gradient Saliency           | 1. Empirical gradient norm on micro-batch: ||grad_theta L||  |
|       | Diagnostics                 | 2. Gradient Noise Scale (GNS) variance: Var(grad) / ||E||^2  |
|       |                             | 3. Output layer vs. LayerNorm gradient projection ratio      |
+-------+-----------------------------+--------------------------------------------------------------+
| L5    | Strong Practical Baseline   | Fixed-budget early RLVR pilot: 10 steps of GRPO              |
|       | (The Competitive Benchmark) | with simple linear learning-curve extrapolation              |
+-------+-----------------------------+--------------------------------------------------------------+
```

---

## 3. FALSIFICATION CRITERIA & SCIENTIFIC VALUE

The central scientific test of PRELUDE v1 is evaluated using **Leave-One-Model-Family-Out Cross-Validation (LOMFO-CV)**:
* Train predictor on Model Families $\{A, B\}$ (e.g., SmolLM2 and Pythia).
* Test predictor zero-shot on Model Family $\{C\}$ (e.g., Qwen-2.5).

### Falsification & Negative Result Standard:
1. **The Primary Competitor Test**:
   If frozen diagnostics (L1 + L2 + L3 + L4) achieve a lower rank correlation ($\tau_{\text{diagnostic}} < \tau_{\text{pilot}}$) or lower AUROC on held-out model families than the 10-step early RLVR pilot (L5), we explicitly document this as a **foundational negative result**:
   > *"Zero-shot representation geometry cannot replace early gradient execution for predicting RL post-training reasoning gains in language models."*
2. **The Discovery Test**:
   If frozen support and geometric diagnostics (L2 + L3) match or exceed the early pilot ($\tau_{\text{diagnostic}} \ge \tau_{\text{pilot}}$) on unseen model families, we establish that **latent solution support and residual stream rank are sufficient statistics governing policy gradient receptivity**, enabling instant zero-training compute routing.

Both outcomes represent significant, publishable scientific contributions.
