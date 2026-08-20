# NOVELTY BOUNDARY & COLLISION AUDIT: INTERVENTION FRONTIERS

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

---

## 1. COLLISION AUDIT SUMMARY

Prior literature has investigated fragments of post-training efficiency and reweighting:

1. **Zhao et al. (*Echo Chamber*, COLM 2025; P25)**: Showed that RL fine-tuning amplifies pre-existing modes, but evaluated only standard RL ($A_5$) without defining an explicit computational Best-of-$N$ ($N \ge 10,000$) null model or testing parameter-efficient prefix limits ($A_3$).
2. **Li et al. (*Q-Probe*, ICML 2024; P26)** & **Snell et al. (2024; P27)**: Demonstrated test-time search scaling ($A_1$), but treated test-time scaling as an alternative to fine-tuning rather than as a baseline null model to measure capability emergence boundaries.
3. **Zhang et al. (*PERL*, 2024; P28)**: Proved prefix-RL ($A_3$) matches full RL ($A_5$) on in-distribution tasks, but did not measure out-of-distribution support expansion.

---

## 2. PRECISE NOVELTY BOUNDARY

Our project occupies a distinct, unexamined scientific boundary:

$$\text{Boundary} = \Big\{ \text{Tasks } D \;\Big|\; \text{Pass@10,000}(A_0, D) = 0 \text{ AND } \text{Acc}(A_3, D) > 0.10 \Big\}$$

We test whether minimal parameter interventions ($A_3$ Prefix-RLVR) can cross the **Support Expansion Threshold** where Best-of-$10,000$ verifier search ($A_1$) completely fails, and whether full RL ($A_5$) adds any incremental benefit over $A_3$ once support expansion is achieved.

---

## 3. HARVARD / KAKADE ALIGNMENT AND INDEPENDENCE

* **Intellectual Alignment**: **High**. Aligns with Professor Sham Kakade's fundamental focus on the science of pretraining/post-training interaction, scaling bounds, and efficient learning dynamics.
* **Research Independence**: **8/10**. Distinct theoretical formulation (Support Expansion Boundary vs Reweighting Null) that does not copy any active Kakade group paper while contributing directly to the foundation of post-training theory.
