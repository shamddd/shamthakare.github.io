# STAGE 7 BLINDED STATISTICAL ANALYSIS PLAN (SAP)

**Date**: August 16, 2026  

---

## 1. PRIMARY ESTIMAND AND HYPOTHESES

* **Primary Endpoint**: $\Delta_{\text{late}} = \mathbb{E}_{S_R}[V_{\text{FULL}} - V_{\text{PREFIX}}] - \mathbb{E}_{S_C}[V_{\text{FULL}} - V_{\text{PREFIX}}]$ on `OOD-D`.
* **Primary Null Hypothesis ($H_0$)**: $\Delta_{\text{late}} \le 0$.
* **Primary Alternative Hypothesis ($H_1$)**: $\Delta_{\text{late}} > 0$.
* **Primary Sample**: Fresh training seeds $43, 44, 45, 46$ ($N=4$).
* **Hierarchical Uncertainty**: Seed-level block bootstrap ($B=1,000$ iterations) respecting `seed -> graph -> matched pair`. Asymptotic $N=4$ limitations explicitly noted.
