# EXPERIMENT PLAN — PROJECT A (FLAGSHIP)

**Canonical Project Title**: *C3A: Causal Counterfactual Credit Assignment for Multi-Turn Tool-Using Foundation Agents*  
**Author**: Sham Thakare  
**Date**: August 2026  

---

## 1. Experimental Pipeline Overview

The experimental evaluation is structured in 4 sequential phases:
```
[Phase 1: Environment & Tool Mock Sandbox Setup]
   │
   ▼
[Phase 2: Offline Diagnostic & Counterfactual Estimator Validation]
   │
   ▼
[Phase 3: Preregistered 5-Way Controlled Online RL Training Sweep]
   │
   ▼
[Phase 4: Robustness Stress-Testing (Noise, Latency, OOD Tools)]
```

---

## 2. Environments & Datasets

1. **InterCode-Bash / InterCode-SQL** (Yang et al., 2023):
   - Multi-turn interactive bash and SQL environments with terminal execution verification.
   - Horizon: $T \in [5, 25]$ turns.
   - Dataset split: 500 training instances, 200 held-out test instances.
2. **ToolBench-Interactive (Sub-split)** (Qin et al., 2024):
   - Realistic multi-API invocation tasks (weather, database, search, mathematical transformation).
   - Horizon: $T \in [5, 20]$ turns.
   - Dataset split: 400 training tasks, 150 held-out test tasks.
3. **Synthetic Causal Tool DAG Environment (CausalTool-Env)**:
   - A perfectly controlled synthetic environment with known ground-truth causal DAGs connecting 10 available tools (where only 3 tools are causally required for task completion, and 7 tools produce distracting or null side-effects).
   - Allows exact mathematical computation of ground-truth Shapley credit to benchmark the estimator $\hat{\Phi}(s_t, a_t)$ against the true oracle $\Phi^*(s_t, a_t)$.

---

## 3. Evaluated Models

- **Primary Model**: `Qwen/Qwen2.5-1.5B-Instruct` (High agentic capability, compact 1.5B scale, fits entirely within single GPU memory).
- **Secondary Model**: `HuggingFaceTB/SmolLM-1.7B` / `Qwen2.5-0.5B-Instruct` (Cross-architecture validation).
- **Fine-Tuning Paradigm**: LoRA ($r=16, \alpha=32$, targeting `q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj`).

---

## 4. Training Hyperparameters (Preregistered)

| Parameter | Value | Rationale |
| :--- | :--- | :--- |
| **Optimizer** | AdamW ($\beta_1=0.9, \beta_2=0.95, \epsilon=10^{-8}$) | Standard for transformer RL |
| **Learning Rate** | $5.0 \times 10^{-6}$ (Cosine decay, 10% warmup) | Prevents policy instability |
| **Batch Size (Prompts)** | 4 | Constrained by GPU memory |
| **Group Size ($G$)** | 4 rollouts per prompt | Standard GRPO group size |
| **Max Trajectory Tokens** | 2,048 tokens ($T \le 25$ turns) | Covers full multi-turn episodes |
| **KL Penalty ($\beta_{\text{KL}}$)** | 0.04 (Token-level reference policy) | Prevents policy drift |
| **Training Steps** | 1,000 gradient updates ($\approx 16,000$ episodes) | Convergence horizon |
| **Random Seeds** | 3 Matched Seeds (`42`, `1337`, `2026`) | Statistical significance |
