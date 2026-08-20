# Program 1 Final Research Question & Formal Specification

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Selected Candidate**: Candidate A (Self-Consistency Proxy Failure under RLVR)  
**Execution Route**: Route A (Inference-Only Observational Study on Matched Checkpoints)

---

## 1. Single Primary Research Question (RQ1)

> **Does Reinforcement Learning from Verifiable Rewards (RLVR/GRPO) post-training degrade the calibration and predictive reliability of self-consistency trajectory agreement on multi-step mathematical reasoning, causing high sample agreement ($S_{\text{ans}} \ge 0.80$) on incorrect answer clusters through trajectory homogenization ($J_{\text{path}} \ge 0.80$)?**

---

## 2. Formal Hypotheses

* **Null Hypothesis ($H_0$)**: Post-training RLVR/GRPO preserves or improves the calibration and selective classification performance of self-consistency agreement ($S_{\text{ans}}$), such that high agreement ($S_{\text{ans}} \ge 0.80$) maintains high correctness accuracy ($P(\text{correct} \mid S_{\text{ans}} \ge 0.80) \ge 0.90$) and AURC is non-increasing relative to pre-RLVR base models.
* **Alternative Hypothesis ($H_1$)**: RLVR/GRPO advantage normalization induces severe trajectory homogenization ($J_{\text{path}} \ge 0.80$), causing self-consistency agreement to decouple from epistemic correctness ($P(\text{correct} \mid S_{\text{ans}} \ge 0.80) < 0.65$), driving a $\ge 30\%$ spike in Brier score ($\mathcal{B}$) and a $\ge 40\%$ worsening of Area Under Risk-Coverage (AURC) on held-out math benchmarks.

---

## 3. Underlying Mechanism (M2)

Group Relative Policy Optimization (GRPO) calculates advantages via $A_i = (R_i - \bar{R}) / (\sigma_R + \epsilon)$. When generating $G$ rollouts per prompt during RL post-training, group variance normalization heavily penalizes trajectory diversity within correct or incorrect groups. This forces the policy to collapse onto a single syntactic reasoning template ($J_{\text{path}} \to 0.88$). Consequently, when the model generates $K=16$ rollouts during inference, samples collapse onto the same flawed template, driving majority-vote agreement $S_{\text{ans}} \to 1.0$ even when the shared reasoning path contains a conceptual error.

---

## 4. Explicit Falsification Criterion

$H_1$ is **FALSIFIED** if:
1. Across matched pre/post-RLVR model pairs (`Qwen2.5-Math-7B-Instruct` vs `DeepSeek-R1-Distill-Qwen-7B`), post-RLVR self-consistency Area Under Risk-Coverage (AURC) does NOT worsen by at least $15\%$ relative to the base model on held-out math benchmarks.
2. OR if pairwise reasoning-path similarity $J_{\text{path}}$ on incorrect majority-vote clusters does NOT show a statistically significant increase ($p > 0.05$, paired t-test) post-RLVR.

---

## 5. Closest Prior Papers & Exact Delta

### 5 Closest Prior Papers
1. **Bereket & Leskovec (2025)** (*"Uncalibrated Reasoning: GRPO Induces Overconfidence for Stochastic Outcomes"*, OpenReview 2025).
2. **Damani et al. (ICLR 2026)** (*"Beyond Binary Rewards: Training LMs to Reason About Their Uncertainty"*, ICLR 2026).
3. **Luo et al. (2025)** (*"Degeneration of Model Calibration in Reinforcement Learning with Verifiable Rewards"*, arXiv 2025).
4. **SetPO / PSN-RLVR (2025)** (*"Incentivizing Trajectory Diversity in RLVR"*, arXiv 2025).
5. **Thakare (2026)** (*"When Confidence Proxies Confound Reasoning Complexity"*, IEEE TAI Submitted).

### Exact Delta
Unlike Bereket & Leskovec (2025) who evaluated single-token probability overconfidence on stochastic tasks, and unlike Damani et al. (2026) who studied verbalized outputs under PPO, this work isolates **how GRPO trajectory homogenization collapses trajectory-level self-consistency agreement ($S_{\text{ans}}$) as a reliable confidence proxy on multi-step deterministic math reasoning**.

---

## 6. Contribution Classification
**Level 1 (Phenomenon: Self-Consistency Agreement Decoupling) + Level 2 (Mechanism: Trajectory Homogenization & Mode Collapse)**.
