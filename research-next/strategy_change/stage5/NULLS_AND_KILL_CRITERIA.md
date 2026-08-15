# MANDATORY NULLS AND EXPLICIT KILL CRITERIA (K1--K8)

**Date**: August 16, 2026  

---

## 1. NULL HYPOTHESES N11--N17

* **N11**: Global policy improvement (RL improves equally at all states, $\Gamma = 0$).
* **N12**: Observation-format artifact.
* **N13**: Trajectory depth confound.
* **N14**: Action-set branching factor confound.
* **N15**: Reward-shaping artifact.
* **N16**: Generator shortcut leakage on structural OOD.
* **N17**: Continuation rollout sampling noise.

---

## 2. EIGHT EXPLICIT KILL CRITERIA (K1--K8)

* **K1**: $\Gamma \le 0$ (Recovery states do not show differential benefit).
* **K2**: $\Delta_{\text{late}} \le 0$ (Prefix-RL matches Full-RLVR).
* **K3**: Effect disappears after matching $S_R$ and $S_C$ control states.
* **K4**: Effect disappears on $D_{\text{structural\_OOD}}$.
* **K5**: Prefix-RL matches Full-RLVR within equivalence margin $\epsilon = 0.02$.
* **K6**: Policy action probabilities shift but state value $V(s)$ does not increase.
* **K7**: Recovery advantage is explained by depth or action count covariates.
* **K8**: Prior art audit identifies an existing work performing the exact state-matched decomposition.
