# RELATED WORK — PROJECT A (FLAGSHIP)

**Canonical Project Title**: *C3A: Causal Counterfactual Credit Assignment for Multi-Turn Tool-Using Foundation Agents*  
**Author**: Sham Thakare  
**Date**: August 2026  

---

## 1. Credit Assignment in Reinforcement Learning for Language Models

Traditional reinforcement learning from human feedback (RLHF) and rule-based verifiers (RLVR) relies on **PPO** (Schulman et al., 2017) or **GRPO** (Shao et al., 2024 / DeepSeek-Math). In single-turn mathematical benchmarks (GSM8K, MATH), uniform trajectory-level advantage normalization performs adequately because trajectories are short ($T \le 300$ tokens) and execution state is purely internal.

Recent 2024–2026 efforts have attempted to decompose trajectory rewards into finer granularities:
- **Process Reward Models (PRMs)** (Lightman et al., 2023; Wang et al., 2024; Qwen2.5-Math-PRM): PRMs assign scalar ratings to individual reasoning steps. However, as proved in recent literature (Gao et al., 2024; PURE, MIT 2025), PRMs are vulnerable to catastrophic reward hacking (Goodhart's Law) and cannot evaluate interactive external tool API state transitions.
- **Turn-Level Advantage Decomposition (TCPO)** (2025): Decomposes trajectory return into turn-level values using baseline differences, but assumes a Markovian text state space without accounting for external tool return mutations.
- **Hindsight Credit Assignment Policy Optimization (HCAPO)** (2025/2026): Uses natural language hindsight summaries to re-score steps, but relies on an auxiliary LLM evaluator that introduces subjective bias and high compute latency.
- **Optimal Advantage Regression (A\*-PO)** (Harvard, 2025): Brantley, Kakade et al. demonstrate that optimal advantage surfaces can be estimated via offline regression, but their framework has not been applied to multi-turn tool interaction graphs with stochastic API returns.

---

## 2. Causal Inference and Counterfactuals in Decision-Making

Counterfactual credit assignment originated in multi-agent RL (e.g., COMA; Foerster et al., 2018) and classic RL credit assignment (Harutyunyan et al., 2019; Mesnard et al., 2021). 
- In 2026, **$\phi$-PPO** introduced counterfactual Shapley values ($\phi$-values) for discrete tabular and robotic RL. However, computing exact Shapley values on sequence-generation models requires $O(2^K)$ forward passes, rendering it impractical for LLMs.
- In tool-augmented agent architectures, **ReAct** (Yao et al., 2023), **ToolBench** (Qin et al., 2024), and **AgentBench** (Liu et al., 2024) evaluate execution performance but train agents primarily via Supervised Fine-Tuning (SFT) or naive trajectory PPO/DPO.

---

## 3. How C3A Substantively Differs from Prior Work

| Dimension | Standard GRPO / PPO | PRM / PURE (MIT) | $\phi$-PPO / COMA | C3A (Proposed) |
| :--- | :--- | :--- | :--- | :--- |
| **Credit Granularity** | Trajectory-level (Uniform) | Step-level (Learned Model) | Action-level (Multi-Agent) | **Turn-level Causal Shapley** |
| **External Reward Model Req.** | None (Outcome Verifier) | **Requires external PRM** | Requires centralized critic | **None (Self-Contained Verifier)** |
| **Tool Execution Awareness** | Blind to tool noise | Fails on external APIs | Tabular / Continuous only | **Native Tool State Invariants** |
| **Compute Complexity** | $O(1)$ forward passes | $O(T)$ PRM passes | $O(2^K)$ exponential | **$O(K)$ Batched Mask Passes** |
| **Vulnerability to Goodhart** | Low (True Verifier) | **Severe (PRM Hacking)** | Low | **Low (Ground-Truth Invariants)** |
