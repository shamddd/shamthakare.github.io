# PUBLICATION-READY STATISTICAL REPORT

**Date**: August 16, 2026  

---

## 1. REFINED STATISTICAL REPORTING STATEMENTS

* **Primary Endpoint**: $\Delta_{\text{late}} = \mathbb{E}_{S_R}[V_{\text{FULL}} - V_{\text{PREFIX}}] - \mathbb{E}_{S_C}[V_{\text{FULL}} - V_{\text{PREFIX}]$ on primary `OOD-D`.
* **Exact One-Sided Sign Test**: Across $N=5$ fresh training seeds ($43, 44, 45, 46, 47$), all 5 seed-level effects were positive ($5/5 > 0$).
  - **Exact p-value**: $p = (1/2)^5 = 1/32 = 0.03125$.
  - **Decision Statement**: Reject the symmetric sign null $H_0: \mathbb{P}(\Delta_{\text{late}} > 0) \le 0.5$ at $\alpha = 0.05$.
* **Scope Bounding**: This inference quantifies training-seed replication conditional on the evaluated model family, training setup, and synthetic environment. It does NOT constitute an LLM population-level statement.
* **Placebo Diagnostic Statement**: *"The placebo contrast ($\Delta_{\text{placebo}} = +0.0500$ vs $\Delta_{\text{SR}} = +0.3400$, interaction $\Gamma_{\text{RP}} = +0.2900$) is consistent with the advantage being concentrated more strongly in preregistered recovery-critical states than in placebo states."*
* **Secondary Distributions**: `OOD-B`, `OOD-M`, and `OOD-C` are classified strictly as secondary robustness and generalization diagnostics.
