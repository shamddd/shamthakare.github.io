# MEASURABLE PREFIX SUFFICIENCY ($PS_k$) FORMALISM

**Date**: August 16, 2026  

---

## 1. NON-TAUTOLOGICAL METRIC FOR PREFIX SUFFICIENCY

Instead of defining "Prefix-Decidable" qualitatively, we define **Prefix Sufficiency at length $k$ ($PS_k$)** operationally:

$$PS_k = \max_{z} U\left(\pi_{\text{base}} \,\Big|\, do(\text{prefix}_k = z)\right)$$

where $U$ is expected solution utility under base model continuation given optimal prefix steering $z$.

---

## 2. MEASURABLE TASK CLASSIFICATION

1. **Class A (Prefix-Sufficient Tasks)**:
   $$PS_k \ge 1 - \epsilon$$
   Early strategy selection under base policy is sufficient to achieve near-optimal utility.

2. **Class B (Late Adaptation-Required Tasks)**:
   $$PS_k < 1 - \epsilon \quad \text{and} \quad U(\pi_{\text{RL}}) \ge PS_k + \delta$$
   Prefix steering under base policy is insufficient, but Full RLVR achieves significantly higher utility via late state-contingent decisions at $t > k$.
