# HYPOTHESES — PROJECT A (FLAGSHIP)

**Canonical Project Title**: *C3A: Causal Counterfactual Credit Assignment for Multi-Turn Tool-Using Foundation Agents*  
**Author**: Sham Thakare  
**Date**: August 2026  

---

## 1. Primary Algorithmic Hypothesis ($H_1$)

> **Hypothesis $H_1$ (Sample Efficiency & Task Completion)**:  
> When fine-tuning foundation models (0.5B–3B parameters) on multi-turn tool interaction tasks ($T \ge 15$ turns), weighting policy gradient advantages by unsupervised counterfactual state-ablation scores ($\hat{\Phi}(s_t, a_t)$) achieves $\ge 20\%$ relative higher Pass@1 task completion on held-out interactive benchmarks compared to trajectory-uniform GRPO and PPO baselines under an identical total token rollout budget.

---

## 2. Theoretical & Mechanistic Hypotheses

### Hypothesis $H_2$ (Policy Gradient Variance Reduction)
> **Statement**: The empirical trace variance of the policy gradient updates under C3A is bounded and strictly lower than standard trajectory-level GRPO:
> $$\mathbb{V}_{\tau \sim \pi_\theta} \left[ \nabla_\theta \mathcal{L}_{\text{C3A}}(\tau) \right] \le (1 - \alpha) \cdot \mathbb{V}_{\tau \sim \pi_\theta} \left[ \nabla_\theta \mathcal{L}_{\text{GRPO}}(\tau) \right]$$
> where $\alpha \ge 0.35$ in environments with trajectory length $T \ge 15$ and non-zero irrelevant tool call frequency.

### Hypothesis $H_3$ (Tool Redundancy Suppression)
> **Statement**: Standard outcome-supervised GRPO leads to "tool bloating" (generating $k > 3$ unnecessary tool invocations per episode to artificially maximize sequence likelihood under sparse positive rewards). C3A counterfactual penalization of non-causal tool returns reduces tool call redundancy by $\ge 45\%$ without decreasing task success rate.

### Hypothesis $H_4$ (Robustness to Stochastic Environment Jitter)
> **Statement**: Under synthetic environment noise injection (15% random tool API error rate and latency jitter), standard GRPO experiences policy divergence (tool failure rate increases by $>30\%$), whereas C3A maintains policy stability by isolating tool stochasticity from policy advantage.

---

## 3. Pre-declared Falsification Boundaries

The primary hypothesis $H_1$ is **formally rejected** if:
1. Held-out Pass@1 accuracy of C3A does not exceed standard outcome-supervised GRPO by at least $\Delta \ge 2.0\%$ across 3 matched random seeds ($p > 0.05$ via two-tailed Welch's t-test).
2. The performance of C3A is equaled or exceeded by a **permuted-credit negative control** (where counterfactual weights are randomly shuffled across time steps).
3. The computational overhead of computing counterfactual ablation advantages exceeds $1.5\times$ the forward-pass time of standard GRPO.
