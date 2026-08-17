# STATESHIFT PRIMARY ESTIMAND SPECIFICATION (FINAL LOCKED)

**Protocol**: StateShift Primary Estimand & Interaction Formalism  
**Target Variable**: $Y = \text{TARGET\_TRANSITION\_SUCCESS} \in \{0, 1\}$  
**Primary Scalar Endpoint**: **$\Gamma_T$** (Checkpoint-Change Interaction at Final Checkpoint $T=256$)  

---

## 1. Formal Mathematical Estimand Definition

For any model checkpoint $\pi_t$ along the post-training trajectory and state type $g \in \{R, C\}$ (where $R = \text{Recovery Perturbed}, C = \text{Control Valid}$):

$$\mu_{R,t} = \mathbb{E}[Y \mid S_R, \pi_t], \quad \mu_{C,t} = \mathbb{E}[Y \mid S_C, \pi_t]$$

Let $\pi_0$ denote the prespecified starting/base model checkpoint (un-RL'd base model). The checkpoint-wise trajectory changes for Recovery and Control states are defined as:

$$\Delta_{R,t} = \mu_{R,t} - \mu_{R,0}$$
$$\Delta_{C,t} = \mu_{C,t} - \mu_{C,0}$$

The **StateShift Checkpoint-Change Interaction Estimand** at step $t$ is:

$$\boxed{\Gamma_t = \Delta_{R,t} - \Delta_{C,t} = \left(\mu_{R,t} - \mu_{R,0}\right) - \left(\mu_{C,t} - \mu_{C,0}\right)}$$

The **Primary Scalar Endpoint** is evaluated at the final prospectively designated checkpoint $T=256$:

$$\boxed{\Gamma_T = \left(\mu_{R,T} - \mu_{R,0}\right) - \left(\mu_{C,T} - \mu_{C,0}\right)}$$

---

## 2. Directional Scientific Interpretation

- **$\Gamma_T > 0$**: Post-training produces **greater checkpoint-wise improvement at recovery states than controls** (evidence of recovery-selective trajectory learning).
- **$\Gamma_T \approx 0$**: Post-training produces **no detectable recovery-selective behavioral change** (checkpoint trajectory improvement is parallel across Control and Recovery states).
- **$\Gamma_T < 0$**: Post-training produces **smaller checkpoint-wise improvement at recovery states than controls**.

> [!IMPORTANT]
> **No Value-Judged Labeling**: Outcomes are evaluated descriptively. $\Gamma_T \approx 0$ or $\Gamma_T < 0$ is a valid scientific finding refuting recovery-selective post-training assumptions, NOT a "project failure".

---
