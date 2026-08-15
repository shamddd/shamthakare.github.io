# ENVIRONMENT MDP SPECIFICATION

**Date**: August 16, 2026  

---

## 1. MDP TUPLE $(\mathcal{S}, \mathcal{A}, P, R, \gamma)$

* **State Space $\mathcal{S}$**: Graph vertex tuple $s = (v_t, g, h_t)$ where $v_t$ is current node, $g$ is goal node, and $h_t$ is execution history.
* **Action Space $\mathcal{A}$**: Finite discrete choices $\mathcal{A}(s) = \{a_1, a_2, \dots, a_K\}$ representing outgoing edges or explicit backtrack token $a_{\text{backtrack}}$.
* **Transition Function $P(s' | s, a)$**: Deterministic graph transitions $v_{t+1} = \delta(v_t, a)$.
* **Reward Function $R(s, a)$**: Sparse task reward: $R(s_T, a) = +1$ if $v_T = g$, else $0$.
