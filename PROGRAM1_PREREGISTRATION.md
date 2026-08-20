# Program 1 Preregistration Protocol

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Status**: Preregistered & Frozen Prior to Full Data Collection

---

## 1. Primary Research Question & Hypotheses
* **RQ**: Does RLVR/GRPO post-training degrade the calibration and selective classification performance of self-consistency trajectory agreement ($S_{\text{ans}}$) on multi-step mathematical reasoning via trajectory homogenization ($J_{\text{path}}$)?
* **$H_0$**: Post-RLVR self-consistency agreement $S_{\text{ans}}$ maintains calibrated correctness probabilities ($P(\text{correct} \mid S_{\text{ans}} \ge 0.80) \ge 0.90$) and non-increasing AURC relative to base models.
* **$H_1$**: Post-RLVR self-consistency agreement decouples from epistemic correctness ($P(\text{correct} \mid S_{\text{ans}} \ge 0.80) < 0.65$), worsening AURC by $\ge 40\%$ and driving Brier score ($\mathcal{B}$) up by $\ge 30\%$ due to trajectory homogenization ($J_{\text{path}} \ge 0.80$).

---

## 2. Experimental Endpoints
* **Primary Endpoints**:
  1. **Area Under Risk-Coverage (AURC)**: Selective classification risk using $S_{\text{ans}}$ as abstention threshold.
  2. **Brier Score ($\mathcal{B}$)**: $\mathcal{B} = \frac{1}{N} \sum_{i=1}^N (S_{\text{ans}, i} - y_i)^2$.
  3. **Pairwise Path Similarity ($J_{\text{path}}$)**: Jaccard n-gram step similarity across sampled rollouts.
* **Secondary Endpoints**:
  1. Expected Calibration Error (ECE, 10 equal-width bins)
  2. Adaptive ECE ($\text{ECE}_{\text{adapt}}$, 10 equal-mass bins)
  3. Negative Log-Likelihood (NLL)
  4. Correctness Prediction AUROC
  5. Calibration Slope ($\beta_{\text{cal}}$) and Intercept ($\alpha_{\text{cal}}$)

---

## 3. Model & Dataset Specifications
* **Models (Matched Pre/Post-RLVR Pairs)**:
  - Base / SFT Baseline: `Qwen/Qwen2.5-Math-7B-Instruct`
  - Post-RLVR / GRPO Checkpoint 1: `DeepSeek-R1-Distill-Qwen-1.5B`
  - Post-RLVR / GRPO Checkpoint 2: `DeepSeek-R1-Distill-Qwen-7B`
* **Datasets**:
  - **GSM8K**: Held-out confirmatory test set indices 500–699 ($N=200$).
  - **MATH-500**: Level 3–5 difficulty algebra & number theory subset ($N=200$).
  - *Data Reuse Safeguard*: Indices strictly demarcated; zero overlap with previous `ear_grpo_reasoning` indices.

---

## 4. Sampling & Inference Protocol
* **Rollouts per Prompt ($K$)**: $K = 16$ independent sampled completions per prompt cluster.
* **Temperature Sweep**: Primary $T = 0.7$; sensitivity ablations $T \in \{0.2, 0.5, 0.8, 1.0\}$.
* **Top-p / Top-k**: `top_p = 0.95`, `top_k = 50`.
* **Max Generation Tokens**: 512 tokens.
* **Seeds**: Matched sampling seeds $\{42, 123, 999\}$.

---

## 5. Statistical Analysis & Multiple-Comparison Correction
* **Hypothesis Testing**: Paired two-tailed t-test and non-parametric Wilcoxon signed-rank test comparing pre- vs. post-RLVR AURC, Brier score, and $J_{\text{path}}$.
* **Confidence Intervals**: 1,000-iteration percentile bootstrap $95\%$ CIs for all metric deltas.
* **Multiple-Comparison Correction**: Bonferroni correction for 4 main comparisons ($\alpha_{\text{adj}} = 0.05 / 4 = 0.0125$).

---

## 6. Falsification Criterion
If post-RLVR AURC does NOT worsen by at least $15\%$ relative to the pre-RLVR baseline ($p > 0.0125$), or if $J_{\text{path}}$ on incorrect majority clusters does NOT show a statistically significant increase ($p > 0.0125$), $H_1$ is **FALSIFIED** and Program 1 will be stopped or pivoted.
