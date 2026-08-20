# PROBLEM-LEVEL HIERARCHY & UNCERTAINTY AUDIT

**Date**: August 16, 2026  

---

## 1. EXPERIMENTAL HIERARCHY LOCK

$$\text{training seed} \rightarrow \text{domain} \rightarrow \text{problem} \rightarrow \text{state pair} \rightarrow \text{rollout}$$

* **Independence Lock**: 30 distinct problem IDs (15 Math, 15 Code). Exactly 1 recovery state and 1 matched control state per problem ID.
* **Uncertainty Blocking**: Statistical analysis blocks primary uncertainty at BOTH training-seed level ($N=5$) AND problem level ($N_{\text{prob}}=15$). Pseudo-replication across states of the same problem is strictly prohibited.
