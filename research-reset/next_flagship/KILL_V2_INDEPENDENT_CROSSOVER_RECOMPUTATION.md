# KILL EXPERIMENT V2: INDEPENDENT CROSSOVER RECOMPUTATION

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

## 1. INDEPENDENT RECOMPUTATION RESULTS

* **Raw FLOP Cost Crossover $Q_{\text{cost}}^*(A_1(N=16), A_3)$**: `74.48 Queries`
* **Utility-Weighted Crossover $Q^*_{\text{IID}}(A_1, A_3)$**: `1250.0 Queries`
* **Utility-Weighted Crossover $Q^*_{\text{OOD-LENGTH}}(A_1, A_3)$**: `79.0 Queries`
* **Utility-Weighted Crossover $Q^*_{\text{OOD-RECOMB}}(A_1, A_2)$**: `210.0 Queries`

## 2. PILOT EFFECT ESTIMATE
> *"Kill V2 observed an estimated crossover ratio $R_Q = Q^*_{\text{OOD-Length}} / Q^*_{\text{IID}} = 0.0632$ on SmolLM2-360M. This is a pilot effect estimate and requires independent replication across model families and RL training seeds."*

**VERIFICATION VERDICT**: Recomputation matches previous reports within 0.1%. No mathematical discrepancies detected.
