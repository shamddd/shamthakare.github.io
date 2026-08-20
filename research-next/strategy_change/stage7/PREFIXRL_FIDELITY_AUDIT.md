# PREFIX-RL IMPLEMENTATION FIDELITY AUDIT

**Date**: August 16, 2026  

---

## 1. COMPARATOR FIDELITY TO ROCHA FILHO ET AL. (2026)

* **Updated Parameters**: On-policy continuation parameters update; prefix tokens remain frozen.
* **Prefix Generation**: Fixed off-policy prefixes $h_k$ drawn from base checkpoint rollouts.
* **Token Budget & Optimizer**: Matched to Full-RLVR (5,000 tokens, AdamW, $lr=1e-5$).
* **Fidelity Rating**: High fidelity to Prefix-RL principle.
