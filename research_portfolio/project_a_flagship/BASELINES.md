# BASELINES — PROJECT A (FLAGSHIP)

**Canonical Project Title**: *C3A: Causal Counterfactual Credit Assignment for Multi-Turn Tool-Using Foundation Agents*  
**Author**: Sham Thakare  
**Date**: August 2026  

---

## 1. Primary Benchmark Baselines

To rigorously evaluate C3A, we implement 4 canonical and state-of-the-art baselines under identical model architectures, token budgets, and optimizer configurations:

### Baseline 1: Standard Outcome-Supervised GRPO (DeepSeek-R1 / Shao et al., 2024)
- **Mechanism**: Groups $G=4$ rollouts per prompt, calculates terminal episode reward $R(\tau) \in \{0, 1\}$, normalizes advantage $A_i = \frac{R(\tau_i) - \text{mean}(R)}{\text{std}(R) + \epsilon}$, and applies uniform advantage $A_i$ to every token in the trajectory.
- **Expected Failure Mode**: Uniform credit rewards redundant and hallucinated tool calls that occur within successful trajectories, leading to tool bloat and slow convergence.

### Baseline 2: Turn-Level Credit Policy Optimization (TCPO / 2025)
- **Mechanism**: Evaluates intermediate turn value using a baseline difference critic across consecutive turns, distributing rewards to individual turns without explicit causal ablation.
- **Expected Failure Mode**: Fails to distinguish between correlation and causation when tools return non-deterministic or high-entropy outputs.

### Baseline 3: Outcome-Supervised PPO (Schulman et al., 2017)
- **Mechanism**: Standard actor-critic PPO with a learned value network $V_\phi(s_t)$ predicting expected episodic return from token states.
- **Expected Failure Mode**: High memory overhead (critic model) and severe value function estimation error on long multi-turn token sequences.

### Baseline 4: Supervised Fine-Tuning (SFT / ReAct Oracle Demonstrations)
- **Mechanism**: Standard cross-entropy loss over curated expert tool-use demonstrations without reinforcement learning.
- **Expected Failure Mode**: Cannot explore beyond expert traces; susceptible to distribution shift when external tools return unexpected errors.
