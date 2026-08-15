# PREREGISTRATION SPECIFICATION: STATE-MATCHED RECOVERY STUDY

**Date**: August 16, 2026  
**Status**: `GO — PREREGISTRATION READY; PILOT NOT YET AUTHORIZED`  
**Preregistration Protocol Version**: `v1.0-draft`  

---

## 1. ABSTRACT & STUDY SUMMARY

This study specifies a state-matched controlled policy comparison to evaluate whether RL post-training produces disproportionately larger downstream value changes at recovery-critical states ($S_R$) relative to matched control states ($S_C$), after early history has been externally fixed and when evaluating generalization across structurally unseen transition topologies.

---

## 2. FORMAL HYPOTHESES

* **Primary Hypothesis $H_1$**: The differential recovery effect $\Gamma = \mathbb{E}_{s \in S_R}[A_{\text{recovery}}(s)] - \mathbb{E}_{s \in S_C}[A_{\text{recovery}}(s)] > 0$.
* **Key Contrast $H_2$**: $\Delta_{\text{late}} = \Gamma_{\text{full}} - \Gamma_{\text{prefix}} > \delta_{\text{threshold}}$ on held-out $D_{\text{structural\_OOD}}$.
