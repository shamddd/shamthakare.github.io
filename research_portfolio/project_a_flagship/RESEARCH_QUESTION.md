# RESEARCH QUESTION — PROJECT A (FLAGSHIP)

**Canonical Project Title**: *C3A: Causal Counterfactual Credit Assignment for Multi-Turn Tool-Using Foundation Agents*  
**Author**: Sham Thakare (Sham Satish Thakare)  
**Date**: August 2026  
**Primary Discipline**: Reinforcement Learning / Post-Training / Autonomous Language Agents  

---

## 1. Primary Scientific Question (RQ1)

> **In multi-turn autonomous agent interactions ($T \ge 20$ turns) with external environment tools and APIs, can an unsupervised counterfactual state ablation estimator isolate the true marginal causal contribution of intermediate tool invocations from stochastic environment noise, outperforming trajectory-uniform advantage weighting without requiring external learned Process Reward Models (PRMs)?**

---

## 2. Subordinate Research Questions

### RQ2 (Variance Reduction vs. Bias Trade-off)
How does counterfactual ablation advantage estimation ($\hat{A}_{\text{C3A}}(s_t, a_t)$) affect policy gradient empirical variance $\mathbb{E}[\|\nabla_\theta \mathcal{L}_{\text{PG}}\|^2]$ compared to standard trajectory-level Group Relative Policy Optimization (GRPO) and outcome-level Proximal Policy Optimization (PPO)?

### RQ3 (Robustness to Environment Stochasticity)
When external tool environments introduce non-stationary latencies, transient network dropouts, or stochastic API return payloads, does causal credit assignment prevent the policy from collapsing into degenerate "shallow-tool" exploration traps that plague standard outcome-supervised GRPO?

### RQ4 (Computational Scalability)
Can counterfactual credit estimation be computed within a single batched inference pass using token mask intervention without requiring recursive $O(T \cdot K \cdot C)$ Monte Carlo tree rollouts?

---

## 3. Motivation & Scope

Reinforcement learning from verifiable rewards (RLVR) has achieved massive success in closed, single-turn mathematical and algorithmic reasoning (e.g., DeepSeek-R1, OpenAI o1/o3, Qwen-2.5-Math). However, extending RLVR to **agentic workflows**—where foundation models interact iteratively with external environments, shell sandboxes, SQL databases, and web APIs across tens or hundreds of steps—encounters the fundamental **Long-Horizon Credit Assignment Dilemma**:
1. Terminal outcome rewards (Task Success $\in \{0, 1\}$) are sparse and delayed.
2. Uniform trajectory-level advantage assignment (standard GRPO) applies equal credit/blame to all $T$ turns. A successful trajectory containing 1 brilliant tool call and 9 redundant/erroneous tool calls rewards all 10 calls equally, inducing severe policy bloat, hallucinated tool arguments, and catastrophic sample inefficiency.
3. Learned Process Reward Models (PRMs) trained on static math/code cannot generalize to non-stationary external environment dynamics and suffer from severe reward hacking under policy optimization (Goodhart's Law).

C3A directly solves this foundational open problem.
