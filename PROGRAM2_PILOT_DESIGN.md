# Program 2 Minimum Viable Pilot Design

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Status**: **PRE-PILOT SPECIFICATION**

---

## 1. Pilot Objectives

1. **Environment Verification**: Confirm local multi-turn agent tool execution harness operates deterministically.
2. **Capability Gate Verification**: Ensure baseline agent model achieves $\ge 70\%$ task completion on clean control trajectories before analyzing failure degradation.
3. **Effect Size Estimation**: Estimate raw counterfactual post-recovery divergence $D(d)$ at depth $d \in \{1, 3, 5\}$ to inform power analysis for main study $N$.
4. **Failure Class Comparison**: Compare persistence curves across $F_1$ (Timeout), $F_2$ (Transient Permission Denial), and $F_4$ (Stale Observation).

---

## 2. Experimental Setup & Counterfactual Matching

* **Tasks**: $N = 30$ multi-turn tool interaction tasks (File management, SQL database queries, user account permission updates, order processing).
* **Counterfactual Matched Control Protocol**:
  - Each task is executed under **Control** (Clean tool responses) and **Failure Injection** ($F_1 / F_2 / F_4$ injected at $t_1$, restored at $t_2$).
  - Prompt, tools, model, temperature ($T=0.2$), and random seed are held 100% identical.
* **Model**: Open function-calling model (`Qwen2.5-Coder-1.5B-Instruct` / `Qwen2.5-7B-Instruct`).
* **Hardware**: Local CPU / MPS execution (**$0.00 spend**).
