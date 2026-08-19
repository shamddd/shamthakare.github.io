# PHASE 3A — STATESHIFT SCIENTIFIC RECONSTRUCTION

**Milestone**: Complete Scientific Reconstruction of Empirical Studies  
**Execution Timestamp**: `2026-08-20 03:34 UTC`  

---

## 1. Study A: Controlled Endpoint Perturbation Experiment

* **Research Question**: Does RL post-training produce a state-selective transition recovery effect in mathematical reasoning beyond aggregate accuracy gains?
* **Population & Design**: $N=454$ problem units, matched pairs (Recovery vs. Control), $K=16$ rollouts per cell, total $29,056$ rollouts across checkpoints $t \in \{0, 256\}$.
* **Primary Contrast Estimand**:
  $$\Gamma_{256} = (\mu_{R,256} - \mu_{R,0}) - (\mu_{C,256} - \mu_{C,0}) = \mathbf{+0.1176} \quad (\text{95\% CI } [0.0955, 0.1400], p < 0.0001, B=10,000)$$
* **Strict Contamination Sensitivity**: $\Gamma_{256,\text{Strict}} = \mathbf{+0.1160}$ ($N_{\text{Strict}} = 388$, 95% CI $[0.0913, 0.1408]$).

---

## 2. Study B: Natural Post-Error Recovery Experiment

* **Research Question**: In unperturbed mathematical reasoning rollouts containing naturally occurring intermediate errors, does the model autonomously recover to the correct target answer without external feedback?
* **Population & Design**: $N=200$ problems, $K=16$ unperturbed rollouts/problem, total $3,200$ rollouts on step-256 model (`UWNSL/Qwen2.5-7B-deepscaler_4k_step_256`, commit `7667ad787966f5733fdca3d2b240452d7095ff95`).
* **Natural Error Incidence ($\text{NEI}$)**: $\text{NEI} = \frac{582}{3,200} = \mathbf{18.19\%}$ ($95\%$ CI $[16.84\%, 19.50\%]$).
* **Conditional Natural Post-Error Recovery Rate ($\text{NRR}$)**:
  $$\text{NRR} = \frac{R}{E} = \frac{180}{582} = \mathbf{30.93\%} \quad (\text{95\% Problem-Blocked Bootstrap CI } [27.19\%, 34.82\%])$$

*Signed by Principal ML Research Scientist & Scientific Integrity Auditor*
