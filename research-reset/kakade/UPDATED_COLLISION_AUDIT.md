# UPDATED COLLISION AUDIT: 2025–2026 PREDICTIVE RL POST-TRAINING LITERATURE

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  
**Target Scope**: Forensic review of recent 2025–2026 publications on predicting post-RL behavior and establishing the precise novelty boundary for **PRELUDE v1**.

---

## 1. PRIMARY 2025–2026 BASELINE PAPERS AUDITED

### [Paper A] Understanding Reasoning from Pretraining to Post-Training
* **CITATION**: Jingyan Shen, Ang Li, Salman Rahman, Yifan Sun, Micah Goldblum, Matus Telgarsky, Pavel Izmailov. *Understanding Reasoning from Pretraining to Post-Training*. `arXiv:2607.16097` (July 2026).
* **RESEARCH QUESTION**: How do pretraining choices (model size, pretraining tokens, pretraining loss) dictate post-RL performance, and how does RL reshape model capabilities on verifiable reasoning tasks?
* **METHODOLOGY & TESTBED**: Controlled chess and tactical puzzle environment with deterministic verifiers; investigates the full pipeline: Pretraining on human games $\to$ SFT on reasoning traces $\to$ RL post-training on tactical puzzles.
* **PRIMARY FINDINGS**:
  1. Establishes a **joint scaling law** predicting post-RL performance from pretraining metrics (loss, tokens, model scale) and RL compute budget.
  2. Demonstrates that on easy tasks, RL amplifies high-density pretraining moves; on hard tasks, RL can uncover low-probability "tail" solutions.
  3. Formulates a joint compute-allocation framework between pretraining and post-training.
* **INPUT SIGNALS USED**: Macro observables ($B$): pretraining cross-entropy loss, pretraining token count $T$, model parameter count $P$, RL training steps/FLOPs.
* **BLINDSPOT / WHAT IS NOT EVALUATED**: Does not measure frozen internal representation geometry ($\text{erank}$, stable rank, residual stream singular values) or gradient saliency/noise scale. Evaluates scaling trends across pretraining runs rather than zero-shot diagnostic routing of frozen checkpoints.

---

### [Paper B] Quagmires in SFT-RL Post-Training: When High SFT Scores Mislead and What to Use Instead
* **CITATION**: Feiyang Kang, Michael Kuchnik, Karthik Padthe, Marin Vlastelica, Ruoxi Jia, Carole-Jean Wu, Newsha Ardalani. *Quagmires in SFT-RL Post-Training: When High SFT Scores Mislead and What to Use Instead*. `ICLR 2026 Poster` / `arXiv:2510.01624` (OpenReview Forum ID: `mMzie8mLWi`).
* **RESEARCH QUESTION**: Why does high accuracy in the Supervised Fine-Tuning (SFT) stage fail to translate into strong performance after Reinforcement Learning, and what proxy metrics reliably predict post-RL outcomes?
* **METHODOLOGY & TESTBED**: Evaluates hundreds of trained models across multiple model families using SFT and RLVR (GRPO) on 7 mathematical reasoning benchmarks (GSM8K, MATH, SVAMP, etc.).
* **PRIMARY FINDINGS**:
  1. Proves that standard SFT benchmark accuracy is positively misleading and negatively correlated with subsequent RLVR gains in multiple settings.
  2. Discovers that **held-out SFT/generalization loss on reasoning problems** and **Pass@large $k$ ($k=16, 64$)** serve as significantly stronger proxy predictors for final RL outcomes.
* **INPUT SIGNALS USED**: Behavioral / observable features ($B$): SFT accuracy, held-out validation loss, Pass@$k$ curves ($k=16, 64$), held-out perplexity.
* **MAJOR COLLISION BOUNDARY**: This paper explicitly establishes that post-RL behavior can be predicted using behavioral observables (held-out loss and Pass@large $k$). PRELUDE v1 MUST include held-out loss and Pass@large $k$ in the baseline feature set $B$ and evaluate whether internal features $I$ provide incremental predictive power beyond $B$.

---

### [Paper C] On the Interplay of Pre-Training, Mid-Training, and RL on Reasoning Language Models
* **CITATION**: Charlie Zhang, Graham Neubig, Xiang Yue. *On the Interplay of Pre-Training, Mid-Training, and RL on Reasoning Language Models*. `arXiv:2512.07783` (December 2025).
* **RESEARCH QUESTION**: How do pretraining headroom, mid-training, and RL interact to determine final reasoning capabilities under fixed compute budgets?
* **METHODOLOGY & TESTBED**: Controlled empirical sweeps across pretraining stages, mid-training exposure, and RLVR post-training across extrapolative (out-of-distribution math/logic) and contextual reasoning tasks.
* **PRIMARY FINDINGS**:
  1. Identifies **pretraining headroom** and **distance to the edge of competence** as decisive predictors of RL benefit.
  2. Shows that when a model is far from its edge of competence (too easy or completely beyond reach), RLVR yields minimal marginal gain; maximum gain occurs at the "edge of competence" window.
  3. Demonstrates that mid-training shifts the edge of competence, directly altering the marginal return of subsequent RLVR compute.
* **INPUT SIGNALS USED**: Headroom & Training-History features ($H$): pretraining step, distance from performance ceiling, task difficulty, edge-of-competence estimate.
* **MAJOR COLLISION BOUNDARY**: Establishes that pretraining headroom and training-history variables ($H$) are strong predictors of RL benefit. PRELUDE v1 MUST include headroom and training-history variables in $H$ and perform the primary scientific test: **Model BHI vs. Model BH**.

---

## 2. REVISED REFINED SCIENTIFIC QUESTION & FEATURE FAMILIES

### Flagship Scientific Question:
$$\boxed{\Large \text{Do frozen internal model-state diagnostics explain residual variation in marginal RLVR gains beyond strong behavioral, training-history, and task-difficulty predictors, and does this incremental information transfer to unseen model families?}}$$

### Feature Family Definitions:

1. **$B$ — Behavioral / Observable Features (Mandatory Baselines)**:
   - Base Pass@1
   - Pass@$k$ ($k=8$)
   - Pass@large-$k$ ($k=32, 64$)
   - Prompt NLL
   - Held-out task / generalization loss
   - Sampled solution coverage $\hat{p}_K$
   - Mean completion token entropy
   - Model parameter count $P$
   - Known pretraining token count $T$
   - Base output calibration

2. **$H$ — Headroom / Training-History Features (Mandatory Baselines)**:
   - Pretraining checkpoint step / age
   - Distance from apparent performance ceiling ($1 - \text{Pass@1}$)
   - Task difficulty tier
   - Edge-of-competence estimate ($1 - \text{Pass@large-}k$)
   - SFT exposure status
   - Pretraining token exposure metadata

3. **$I$ — Internal Diagnostics (Candidate Contribution)**:
   - Residual stream effective rank ($\text{erank}$)
   - Stable rank ($\text{srank}$)
   - Layerwise singular-value spectra summaries
   - Linear reward probe separability ($\text{AUROC}, R^2$)
   - Micro-batch gradient norm statistics
   - Gradient Noise Scale (GNS) proxies
   - LayerNorm vs. output head gradient projection ratios

---

## 3. PRIMARY SCIENTIFIC TEST DESIGN

To evaluate whether internal features $I$ provide true mechanistic, non-redundant predictive power, we fit low-capacity models (Ridge / ElasticNet) across three nested feature sets:

$$\begin{aligned}
\text{Model } B: \quad \hat{\Delta}_{\text{RLVR}} &= f(B) \\
\text{Model } BH: \quad \hat{\Delta}_{\text{RLVR}} &= f(B, H) \\
\text{Model } BHI: \quad \hat{\Delta}_{\text{RLVR}} &= f(B, H, I)
\end{aligned}$$

* **Primary Scientific Comparison**: **Model BHI vs. Model BH** under Leave-One-Model-Family-Out Cross-Validation (LOMFO-CV).
* **Target Quantity**: Incremental out-of-family predictive value on marginal RLVR gain $\Delta_{\text{RLVR}}(M, D, C) = U(\mathcal{T}_{\text{RLVR}}(M,D,C), D_{\text{test}}) - U(M, D_{\text{test}})$.

---

## 4. SUMMARY COLLISION & DIFFERENTIATION MATRIX

| Research Work | Core Topic & Method | Predictive Signals Used | What PRELUDE v1 Adds (Incremental Contribution) | Baseline Role |
| :--- | :--- | :--- | :--- | :--- |
| **Shen et al. (2026)** (*arXiv:2607.16097*) | Joint scaling laws from Pretraining $\to$ SFT $\to$ RL | Pretraining loss, tokens $T$, scale $P$, RL FLOPs | Evaluates whether internal rank ($\text{erank}$) explains residual variance beyond joint scaling laws. | **Macro Scaling Baseline ($B$)** |
| **Kang et al. (2026)** (*ICLR 2026 / 2510.01624*) | Predictors of RLVR outcome when SFT misleads | Held-out SFT loss, Pass@large $k$ behavioral curves | Evaluates whether internal representation geometry provides additive predictive power beyond Pass@large $k$. | **Behavioral Proxy Baseline ($B$)** |
| **Zhang et al. (2025)** (*arXiv:2512.07783*) | Interplay of pre-training, mid-training, and RL | Pretraining headroom, edge-of-competence, task difficulty | Evaluates whether internal state features $I$ add predictive power beyond competence-edge and headroom variables $H$. | **Headroom & History Baseline ($H$)** |
| **Zhao et al. (2025)** (*Echo Chamber*) | RL amplifies pretraining output modes | Pretraining dataset mixtures & output distributions | Quantitative diagnostic feature extraction from mode concentration. | **Intellectual Inspiration** |
| **Han et al. (2026)** (*Weight Decay Plasticity*) | Weight decay preserves downstream adaptability | Pretraining weight decay, representation separability | Tests internal representation separability as an active pre-intervention feature $I$. | **Intellectual Inspiration** |
