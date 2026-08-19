# PHASE 2 STAGE C0 — NATURAL RECOVERY EVENT CLASSIFICATION RULES

**Milestone**: Natural Recovery Identification Specification  

---

## 1. Classification Criteria for `NATURAL_RECOVERY_SUCCESS`

A rollout episode achieves **`NATURAL_RECOVERY_SUCCESS = 1`** iff:

1. **Prior Verified Error**: The rollout contains a verified `NATURAL_ERROR_EVENT`.
2. **Zero External Assistance**: No external hint, correction, or verifier feedback was supplied to the model.
3. **Autonomous Step Realignment**: The subsequent reasoning steps return to a verifier-consistent state.
4. **Final Answer Correction**: The final boxed answer matches the ground-truth target answer.

---

## 2. Mathematical Estimand & Denominator

* **Natural Error Incidence ($\text{NEI}$)**:
  $$\text{NEI} = \frac{\text{Rollouts with } \ge 1 \text{ Natural Error}}{\text{Total Valid Rollouts } (3,200)}$$

* **Natural Post-Error Recovery Rate ($\text{NRR}$)**:
  $$\text{NRR} = \frac{\text{Qualifying Recoveries } (R)}{\text{Qualifying Error Episodes } (E)}$$

*Signed by Lead Statistical Methodologist & Reproducibility Engineer*
