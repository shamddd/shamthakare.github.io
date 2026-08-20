# PROGRAM 1 MAIN STUDY PREREGISTRATION PROTOCOL

**Study Title**: Trajectory Self-Consistency Decoupling Under Accuracy-Matched Reinforcement Learning with Verifiable Rewards  
**Principal Investigator**: Sham Satish Thakare (Independent Researcher)  
**Execution Timestamp**: `2026-08-19 23:16 UTC`  
**Preregistration Protocol Hash**: SHA-256 `c38290f11902847a460df0823901b2a95c96b1b510793b827e74819a92e10582`  
**Status**: **`FROZEN PROSPECTIVELY BEFORE MAIN DATA COLLECTION`**

---

## 1. Primary Research Question

> **Primary RQ**: When RLVR/GRPO improves or preserves reasoning accuracy, does trajectory self-consistency become a systematically less reliable predictor of correctness, and is that decoupling associated with changes in reasoning-path diversity beyond what can be explained by accuracy, trace length, sampling temperature and problem difficulty?

---

## 2. Hypotheses

* **$H_0$ (Null Hypothesis)**: Conditional on matched task accuracy and decoding configuration, RLVR does not materially change the relationship between trajectory agreement and correctness.
* **$H_1$ (Alternative Hypothesis)**: Even when RLVR preserves or improves reasoning accuracy, trajectory agreement becomes systematically less discriminative or less calibrated as a correctness signal.
* **Mechanistic $H_{1b}$**: Any deterioration in agreement reliability is associated with reduced reasoning-path diversity beyond changes explained by correctness, trace length, and sampling settings.

---

## 3. Capability Gate

A model lineage / checkpoint condition enters the publication-grade primary analysis if and only if it satisfies the capability gate:
* **Baseline Accuracy Threshold**: Task accuracy $\ge 15.0\%$.
* **Bimodal Outcome Requirement**: Both correct ($Y=1$) and incorrect ($Y=0$) trajectory clusters must exist to allow non-degenerate calibration and AUROC calculation.
* **Failure Case Handling**: Conditions failing the capability gate are excluded from primary publication tables and reported separately in `PROGRAM1_FAILURE_CASES.md`.

---

## 4. Model Lineages & Datasets

### Model Lineages ($N_{\text{lineages}} = 2$):
1. **Lineage 1 (Qwen-Math)**: `Qwen/Qwen2.5-Math-1.5B` & `Qwen2.5-Math-7B` (Base vs Instruct / GRPO fine-tuned).
2. **Lineage 2 (DeepSeek-R1 Distill)**: `deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B` & `DeepSeek-R1-Distill-Qwen-7B`.

### Benchmark Datasets ($N_{\text{datasets}} = 2$):
1. **GSM8K**: Full test set ($N=500$ evaluation items).
2. **MATH**: Level 3–5 subset ($N=500$ evaluation items).

---

## 5. Experimental Design & Hyperparameters

* **Trajectory Sampling**: $K \in \{4, 8, 16\}$ rollouts per item.
* **Sampling Temperatures**: $T \in \{0.3, 0.7, 1.0\}$.
* **Primary Endpoint**: Difference in AUROC ($\Delta \text{AUROC}$) for predicting answer correctness using trajectory self-consistency agreement ($K=16, T=0.7$).
* **Secondary Endpoints**: Difference in AURC ($\Delta \text{AURC}$), Brier Score, Expected Calibration Error (ECE), High-Agreement Error Rate (HAER), and Reasoning-Path Diversity (lexical n-gram Jaccard, embedding cosine distance, step-graph similarity).

---

## 6. Accuracy-Matched Statistical Model

To control for competence gains, the key test evaluates the interaction term in a stratified logistic regression:

$$\text{Correctness}_{i,k} \sim \text{Agreement}_{i} + \text{RLCondition} + \left(\text{Agreement}_{i} \times \text{RLCondition}\right) + \text{Difficulty}_i + \text{TraceLength}_{i,k}$$

* **Primary Test Statistic**: Significance and negative sign of the interaction coefficient $\beta_{\text{Agreement} \times \text{RLCondition}}$, testing whether self-consistency agreement becomes less predictive of correctness post-RLVR under accuracy parity.

*Signed by Principal ML Research Scientist & Lead Statistical Methodologist*
