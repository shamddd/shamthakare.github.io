# DYNAMIC POST-TRAINING UNDER NON-STATIONARY DEPLOYMENT

**Date**: August 16, 2026  

---

## 1. DYNAMIC SYSTEM STATE & ACTION SPACE

At deployment time step $t = 1, 2, \dots$:
* **Environment State**: $S_t = (D_t, p_t, c_t, M_t)$ where $D_t$ is task distribution, $p_t$ is base competence, $c_t$ is inference unit cost, and $M_t$ is current model adapter state.
* **Action Space $\mathcal{A}_t$**:
  1. $a_{\text{search}}$: Execute test-time search (Best-of-$N$ / MCTS) on $M_t$.
  2. $a_{\text{continue}}$: Serve single completion on $M_t$.
  3. $a_{\text{adapt}}$: Pay one-time adaptation cost $F_{\text{adapt}}$, updating $M_t \to M_{t+1}$ via LoRA/RLVR.
  4. $a_{\text{switch}}$: Pay switching cost $F_{\text{switch}}$ to swap active adapter module.
  5. $a_{\text{readapt}}$: Re-train model on recent non-stationary drift data $D_t$.

---

## 2. OBJECTIVE FUNCTION

$$\min_{\pi} \mathbb{E} \left[ \sum_{t=1}^T \left( C_{\text{action}}(a_t) + C_{\text{infer}}(a_t, S_t) \right) + \lambda \cdot \text{Regret}(\pi) \right] \quad \text{s.t.} \quad U(a_t, S_t) \ge u$$
