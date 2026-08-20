# FORMAL RESEARCH PREREGISTRATION (2026–2027)

**Principal Investigator**: Sham Thakare (Sham Satish Thakare)  
**Date**: August 2026  
**Status**: `FROZEN & COMMITTED PRIOR TO EXPERIMENTATION`  
**Git Hash / Provenance**: Pre-execution freeze  

---

## 1. Study Overview & Integrity Protocol

This document formally freezes the experimental designs, hypotheses, baseline configurations, negative controls, random seeds, and statistical evaluation rules for the **3-Project Master Research Program** prior to running full-scale empirical training runs.

---

## 2. Project A (Flagship): C3A — Causal Counterfactual Credit Assignment

- **Primary Hypothesis**: Weighting multi-turn agent policy gradient updates by counterfactual state-ablation credit scores ($\hat{\Phi}(s_t, a_t)$) yields $\ge 20\%$ relative higher Pass@1 on held-out interactive tool benchmarks compared to trajectory-uniform GRPO and PPO baselines under an identical token budget.
- **Primary Endpoint**: Held-out Task Pass@1 on InterCode-Bash, InterCode-SQL, and ToolBench-Interactive.
- **Secondary Endpoints**:
  1. Policy gradient empirical trace variance $\mathbb{E}[\|\nabla_\theta \mathcal{L}\|^2]$.
  2. Tool call redundancy index (unnecessary tool invocations per solved episode).
- **Frozen Models**:
  - Primary: `Qwen/Qwen2.5-1.5B-Instruct` (LoRA $r=16, \alpha=32$).
  - Secondary: `HuggingFaceTB/SmolLM-1.7B`, `Qwen/Qwen2.5-0.5B-Instruct`.
- **Frozen Baselines**:
  1. Standard Outcome-Supervised GRPO ($G=4$)
  2. Turn-Level Credit Policy Optimization (TCPO)
  3. Standard Actor-Critic PPO
  4. Supervised Fine-Tuning (SFT / ReAct Demonstrations)
- **Frozen Negative Controls**:
  1. $\text{C3A}_{\text{perm}}$ (Permuted turn weights)
  2. $\text{C3A}_{\text{rand}}$ (Gaussian noise advantage scaling)
  3. Compute-Matched GRPO ($G=8$)
  4. Oracle Causal DAG Control ($\text{C3A}^*$ on synthetic `CausalTool-Env`)
- **Frozen Seeds**: `42`, `1337`, `2026`.
- **Statistical Tests**: Two-tailed Welch's t-test with Bonferroni correction ($\alpha = 0.0125$) and Mann-Whitney U test.
- **Stopping Rule**: Exactly 1,000 gradient updates ($\approx 16,000$ episodes). Zero early stopping on test performance.

---

## 3. Project B (Theory/Diagnostic): Representation Rank Collapse in Transformer Deliberation

- **Primary Hypothesis**: The effective spectral rank ($\text{erank}$) of intermediate hidden layer activations ($l \in [0.4L, 0.7L]$) exhibits a $>35\%$ contraction prior to logical derivation breakdown, maintaining partial correlation $|r(\text{erank}, \text{Error} \mid \text{Length})| > 0.40$ ($p < 0.001$) after controlling for sequence length.
- **Primary Endpoint**: Partial correlation $r(\text{Metric}, \text{Error} \mid \text{Length})$ and Error AUROC / AUPRC.
- **Frozen Datasets**: GSM8K ($N=500$), MATH Level 1–5 ($N=500$), LogiQA ($N=300$), synthetic length-balanced arithmetic ($N=200$).
- **Frozen Models**: `Qwen2.5-0.5B-Instruct`, `Qwen2.5-Math-1.5B`, `DeepSeek-R1-Distill-Qwen-1.5B`.
- **Frozen Baselines**: Token Predictive Entropy, Mean Token NLL, Logit Margin Uncertainty, Self-Consistency Consensus ($K=4$).
- **Frozen Negative Controls**: Shuffled token activation control, random projection baseline, length-matched paired derivation control.
- **Statistical Tests**: Partial Pearson and Spearman rank correlation with Fisher z-transform significance testing.

---

## 4. Project C (Systems/Agents): Decentralized Tipping-Point Mitigation in Multi-Agent Consensus

- **Primary Hypothesis**: Multi-agent reasoning debates exhibit a sharp non-linear phase transition in consensus error under adversarial / sycophantic peer pressure; an asynchronous epistemic disagreement-gated cascade breaker improves collective accuracy by $\ge 15\%$ over standard majority debate under 20% Byzantine corruption.
- **Primary Endpoint**: Collective Task Accuracy under varying Byzantine corruption fractions ($f \in [0.0, 0.4]$).
- **Secondary Endpoints**: Sycophancy collapse rate, consensus entropy, communication token overhead.
- **Frozen Datasets**: StrategyQA, GSM8K, Multi-Agent Logic Benchmark (M-LogicBench).
- **Frozen Models**: 3–7 heterogeneous agents using `Qwen2.5-0.5B`, `SmolLM-1.7B`, `Llama-3.2-1B`.
- **Frozen Baselines**: Standard Multi-Agent Debate (Du et al., 2024), Majority Voting, Centralized Leader Orchestration (HACN), Static Random Interventions.
- **Frozen Controls**: Shuffled communication topology, confidence-blind debate baseline, homogeneous model control.
- **Frozen Seeds**: `42`, `100`, `200`, `500`, `1337`.
- **Statistical Tests**: Paired permutation tests ($10,000$ permutations) and two-way ANOVA across corruption fractions.
