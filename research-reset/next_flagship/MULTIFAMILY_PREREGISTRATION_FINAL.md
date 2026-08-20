# FINAL MULTI-FAMILY REPLICATION PREREGISTRATION SPECIFICATION

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

---

## 1. CONFIRMATORY SCIENTIFIC CLAIM

> *"We test whether the deployment-horizon intervention frontier observed in Kill V2 changes systematically between IID and controlled OOD reasoning regimes across independently pretrained model families."*

---

## 2. PRIMARY CONFIRMATORY ENDPOINT

For each model family $f \in \{	ext{SmolLM2}, 	ext{Qwen2.5}, 	ext{TinyLlama}\}$:
$$R_f = \frac{Q^*_{\text{frontier, OOD-Length}}}{Q^*_{\text{frontier, IID}}}$$

* **Primary Evidence Criterion**: Directional replication ($R_f < 1.0$) across at least **2 of 3 model families**.
* **Utility-Cost Constraint**: $Q^*_{\text{frontier}}$ is calculated on the utility-cost Pareto frontier, comparing trained methods against the full Best-of-$N$ Pareto envelope ($N \in \{1, 2, 4, 8, 16, 32\}$).

---

## 3. FALSIFICATION RULES (REPLICATION FAILURE)

The replication claim is **FALSIFIED** if any of the following occur:
* **F1**: Fewer than 2 of 3 model families exhibit $R_f < 1.0$.
* **F2**: Utility-normalized Pareto envelopes eliminate the crossover shift.
* **F3**: Best-of-$N$ Pareto envelope strictly dominates $A_2$ and $A_3$ across all query volumes $Q \in [1, 10^5]$.
* **F4**: Training seed variance dominates between-regime crossover variance.
