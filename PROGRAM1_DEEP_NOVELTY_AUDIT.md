# Program 1 Deep Novelty Audit & Candidate Evaluation

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Status**: Completed & Selected Candidate A via Route A (Inference-Only)

---

## 1. Audit of Candidate Questions

### Candidate A — Self-Consistency Proxy Failure under RLVR/GRPO (SELECTED)
* **Core Question**: Does RLVR / GRPO post-training weaken or decouple the statistical relationship between reasoning-path agreement (self-consistency) and actual correctness/calibrated uncertainty, even when pass@1 accuracy improves?
* **Scientific Value**: High (Level 1 Phenomenon + Level 2 Mechanism). Addresses a fundamental distribution-shift assumption in LLM inference.
* **Why it Survives Prior Art**: Bereket & Leskovec (2025) focused on token-level probability overconfidence for stochastic outcomes. Candidate A evaluates *trajectory-level self-consistency agreement* on multi-step deterministic math problems, discovering that GRPO-induced trajectory homogenization drives agreement $S \to 1.0$ even on incorrect answer clusters, breaking the AURC (Area Under Risk-Coverage) guarantee.

---

### Candidate B — Negative Flips / Overthinking Prediction
* **Core Question**: Can pre-answer uncertainty or reasoning-path disagreement predict negative flips when additional inference-time reasoning changes a correct short answer into an incorrect long answer?
* **Scientific Value**: Moderate (Level 1 + Level 3).
* **Collision Audit**: Substantially pre-empted by recent 2025 preprints on "Overthinking in Long Chain-of-Thought" and *Damani et al. (ICLR 2025)* adaptive compute allocation.
* **Verdict**: Rejected as primary RQ due to moderate collision risk (Score = 3).

---

### Candidate C — Credit Assignment Granularity & Calibration
* **Core Question**: Does changing RL credit assignment granularity (outcome vs sample vs process level) alter calibration and reasoning-path diversity when final task accuracy is matched?
* **Scientific Value**: Moderate (Level 2 + Level 3).
* **Collision Audit**: Shares structural overlap with your submitted IEEE TAI paper (`ear_grpo_reasoning` CLM-002) and *Lightman et al. (2023)* PRM work.
* **Verdict**: Rejected as primary RQ due to internal collision risk with CLM-002.

---

## 2. Precise Definitions of Self-Consistency Proxies

To prevent treating "self-consistency" vaguely, Program 1 explicitly separates:

1. **Answer Agreement ($S_{\text{ans}}$)**: Exact-match or normalized string identity frequency of the final extracted answer across $K$ sampled trajectories:
   $$S_{\text{ans}}(y^*) = \frac{1}{K} \sum_{k=1}^K \mathbb{I}(\text{Extract}(y_k) = y^*)$$
2. **Majority-Vote Frequency ($f_{\text{maj}}$)**: The relative empirical frequency of the modal answer cluster $y^* = \text{mode}(\{\text{Extract}(y_k)\}_{k=1}^K)$.
3. **Semantic Answer Agreement ($S_{\text{sem}}$)**: Equivalence matching accounting for mathematical notation variants (e.g., $\frac{1}{2} \equiv 0.5$).
4. **Reasoning-Path Similarity ($J_{\text{path}}$)**: Jaccard similarity or n-gram overlap between step-by-step intermediate reasoning steps across trajectories.
5. **Token-Level Entropy ($H_{\text{tok}}$)**: Per-token predictive distribution entropy averaged over the reasoning path:
   $$H_{\text{tok}}(y) = -\frac{1}{|y|} \sum_{t=1}^{|y|} \sum_{v \in V} P(v \mid y_{<t}) \log P(v \mid y_{<t})$$
6. **Sequence Likelihood ($L_{\text{seq}}$)**: Mean log-probability of generated tokens $\frac{1}{|y|} \sum_{t=1}^{|y|} \log P(y_t \mid y_{<t})$.
7. **Verbalized Confidence ($C_{\text{verb}}$)**: Self-reported numerical confidence probability extracted from explicit model prompts (e.g., "Confidence: 85%").

---

## 3. Rigorous Calibration Metrics Suite

Rather than relying solely on ECE (which depends heavily on binning choices), Program 1 evaluates:

1. **Brier Score ($\mathcal{B}$)** (Primary Metric):
   $$\mathcal{B} = \frac{1}{N} \sum_{i=1}^N (S_{\text{ans}, i} - y_i)^2 \quad \text{where } y_i \in \{0, 1\}$$
2. **Area Under Risk-Coverage (AURC)** (Primary Metric): Measures selective classification performance when using $S_{\text{ans}}$ as the confidence threshold to abstain from uncertain predictions.
3. **Expected Calibration Error (ECE)** (Secondary Metric): Equal-width 10-bin calibration error:
   $$\text{ECE} = \sum_{m=1}^M \frac{|B_m|}{N} |\text{acc}(B_m) - \text{conf}(B_m)|$$
4. **Adaptive ECE ($\text{ECE}_{\text{adapt}}$)** (Secondary Metric): Equal-mass binning ECE to eliminate bin density variance.
5. **Negative Log-Likelihood (NLL)**: $\text{NLL} = -\frac{1}{N} \sum_{i=1}^N \left[ y_i \log p_i + (1-y_i) \log(1-p_i) \right]$.
6. **Correctness Prediction AUROC**: Receiver Operating Characteristic area under curve treating $S_{\text{ans}}$ as a binary classifier predicting exact match correctness $y_i$.
7. **Calibration Slope ($\beta_{\text{cal}}$) and Intercept ($\alpha_{\text{cal}}$)**: Logistic calibration curve parameters fitted via $\text{logit}(P(y=1)) = \alpha_{\text{cal}} + \beta_{\text{cal}} \cdot S_{\text{ans}}$.

---

## 4. Evaluation of Experimental Routes (A vs B vs C)

* **Route A — Inference-Only Observational Study (SELECTED)**:
  - *Rationale*: Pre/post-RL reasoning model pairs exist publicly:
    - Base / SFT: `Qwen/Qwen2.5-Math-7B`, `Qwen/Qwen2.5-Math-7B-Instruct`
    - Post-RLVR / GRPO: `DeepSeek-R1-Distill-Qwen-1.5B`, `DeepSeek-R1-Distill-Qwen-7B`, `Qwen/Qwen2.5-Math-7B-Instruct` + RL checkpoints.
  - *Advantage*: Zero GPU training cost (\$0.00 compute spend), $100\%$ reproducible, isolates the exact pre/post-RLVR self-consistency failure phenomenon without training noise.
* **Route B — Minimal LoRA/GRPO Intervention**: Reserved only if Route A reveals an inconclusive signal.
* **Route C — Abandon Program 1**: Rejected; Route A presents an untouched, high-impact scientific phenomenon.

---

## 5. Final Selection: Candidate A via Route A

Program 1 selects **Candidate A (Self-Consistency Proxy Failure under RLVR)** executed via **Route A (Inference-Only Observational Study)**.
