# KILL EXPERIMENT V2: CROSSOVER UNCERTAINTY ANALYSIS

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

## 1. EVALUATION UNCERTAINTY (BOOTSTRAP 95% CI)

* **$Q^*_{\text{IID}}(A_1, A_3)$**: `1250 [980, 1540] Queries`
* **$Q^*_{\text{OOD-LENGTH}}(A_1, A_3)$**: `79 [62, 102] Queries`
* **$R_Q = Q^*_{\text{OOD}} / Q^*_{\text{IID}}$**: `0.0632 [0.048, 0.086]`

## 2. UNCERTAINTY CATEGORIZATION
* **Evaluation Uncertainty**: Accounted for via test set bootstrap.
* **Unmeasured Training / Model-Family Uncertainty**: Unmeasured in single-model pilot; strictly requires multi-family replication.
