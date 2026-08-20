# NOVELTY AUDIT — PROJECT A (FLAGSHIP)

**Canonical Project Title**: *C3A: Causal Counterfactual Credit Assignment for Multi-Turn Tool-Using Foundation Agents*  
**Author**: Sham Thakare  
**Date**: August 2026  

---

## 1. Adversarial Prior-Art Search & Semantic Collision Checks

We conducted systematic searches across arXiv, Google Scholar, OpenReview, ACL Anthology, and ICLR/NeurIPS 2024–2026 proceedings for exact and semantic variants:
1. `"Causal Credit Assignment" + "Tool Use" + "Language Models"`
2. `"Counterfactual Shapley" + "GRPO" + "Agentic RL"`
3. `"Turn-Level Reward" + "Ablation" + "ToolBench"`
4. `"Trajectory Advantage Decomposition" + "External APIs"`

### Collision Findings
- **Collision Item 1: Counterfactual Shapley Credit Assignment ($\phi$-PPO, 2026)**
  - *Difference*: $\phi$-PPO is formulated strictly for continuous vector state spaces and robotic locomotion. It does not address autoregressive transformer token generation, discrete tool syntax calling, or multi-turn prompt context.
- **Collision Item 2: Turn-level Credit Policy Optimization (TCPO, 2025)**
  - *Difference*: TCPO computes turn advantages using a baseline critic over dialogue turns. It does not perform causal counterfactual intervention or ablation over external tool state transitions.
- **Collision Item 3: EAR-GRPO / CA-GRPO (Author's own prior work, 2026)**
  - *Difference*: EAR-GRPO investigated sample-level uncertainty and self-consistency weighting in *single-turn mathematical reasoning* (GSM8K). C3A operates in a completely distinct domain (*multi-turn interactive tool-using agents*), uses *causal intervention ablation operators* rather than predictive entropy/consensus, and solves long-horizon delayed feedback rather than single-turn confidence proxies.

---

## 2. Definitive Claims of Novelty

1. **First Token-Efficient Counterfactual Ablation Operator for Tool Agents**: We introduce an attention-mask-based counterfactual intervention operator that evaluates the marginal outcome impact of tool call return payloads without re-executing expensive external APIs or recursive tree rollouts.
2. **Causal Advantage Weighting Function for Agentic GRPO**: We formulate the C3A policy gradient objective:
   $$\mathcal{L}_{\text{C3A}}(\theta) = \mathbb{E}_{\tau \sim \pi_\theta} \left[ \sum_{t=1}^T \frac{\pi_\theta(a_t \mid s_t)}{\pi_{\text{old}}(a_t \mid s_t)} \cdot \hat{A}_{\text{C3A}}(s_t, a_t) \right]$$
   where $\hat{A}_{\text{C3A}}(s_t, a_t) = A_{\text{group}}(\tau) \cdot \hat{\Phi}(s_t, a_t)$, rigorously isolating causal tool value.
3. **Formal Invariant Guarantees**: We prove that under deterministic tool return ablations, C3A converges to the true causal Shapley value with bounded $O(1/\sqrt{K})$ estimation error.
