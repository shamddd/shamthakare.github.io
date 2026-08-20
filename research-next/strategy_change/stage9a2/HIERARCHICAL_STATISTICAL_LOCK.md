# HIERARCHICAL STATISTICAL LOCK SPECIFICATION

**Date**: August 16, 2026  

---

## 1. HIERARCHICAL UNCERTAINTY MODELING

$$\text{training seed} \rightarrow \text{domain} \rightarrow \text{problem} \rightarrow \text{state pair}$$

* **Primary Directional Test**: Exact one-sided sign test across $N=5$ fresh training seeds ($P = 0.03125$).
* **Problem-Blocked Uncertainty**: Seed-level effects are reported with problem-blocked cluster standard errors ($N_{\text{prob}}=15$ per domain).
* **Prohibition**: Pooling 5 seeds $\times$ 15 problems = 75 observations as independent replicates is **STRICTLY PROHIBITED**.
