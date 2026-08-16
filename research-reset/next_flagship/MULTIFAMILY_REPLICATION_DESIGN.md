# MULTI-FAMILY CONFIRMATORY REPLICATION EXPERIMENTAL DESIGN

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

## 1. PRE-REGISTERED DESIGN SPECIFICATIONS

* **Target Model Families (3 Distinct Families)**:
  1. `SmolLM2-360M-Instruct`
  2. `Qwen2.5-0.5B-Instruct`
  3. `Pythia-410M-deduped`
* **RL Training Seeds**: 2 independent training seeds per family (Seed 42, Seed 1337) $\implies 6$ training runs per intervention.
* **Task Regimes**: IID (ModComp-3) and OOD-LENGTH (ModComp-5).
* **Interventions**: $A_0, A_1(N), A_2 \text{ (LoRA-RLVR)}, A_3 \text{ (Full RLVR)}$.
* **Confirmatory Primary Metric**: $R_f = Q^*_{\text{frontier, OOD}} / Q^*_{\text{frontier, IID}}$ across all 3 families.
