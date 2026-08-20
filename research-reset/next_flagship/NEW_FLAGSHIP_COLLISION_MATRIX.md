# MASTER COLLISION MATRIX: INTERVENTION EFFICIENCY FRONTIERS

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

---

## 1. EXPANDED LITERATURE COLLISION LEDGER

| Index | Paper Title / Venue | Authors / Date | Key Focus | Status vs Matched Compute Frontier |
| :--- | :--- | :--- | :--- | :--- |
| **P25** | *Echo Chamber* (COLM 2025) | Zhao et al. (2025) | RL fine-tuning amplifies pretrained modes | **STRONG OVERLAP** — Shows RL reweights, but lacks compute matching. |
| **P26** | *Q-Probe* (ICML 2024) | Li et al. (2024) | Representation probe for Best-of-N ($A_1$) | **PARTIAL OVERLAP** — Covers $A_1$ reranking baseline. |
| **P27** | *Scaling LLM Test-Time Compute* | Snell et al. (2024) | Test-time search scaling vs model size | **STRONG OVERLAP** — Compares $A_1$ vs fine-tuning, lacks parameter hierarchy ($A_3, A_4$). |
| **P28** | *Parameter-Efficient RL (PERL)* | Zhang et al. (ICLR 2026) | Prefix tuning ($A_3$) vs Full RL ($A_5$) | **STRONG OVERLAP** — Compares $A_3$ vs $A_5$, lacks amortized $Q^*$ cost matching. |
| **P33** | *SAGE: Shaping Anchors* | Lee et al. (May 2026) | Anchor exploration for hard RLVR | **DIRECT COLLISION** on support expansion; **DISTINCT** on matched-compute efficiency. |
| **P34** | *Privileged On-Policy Exploration* | Gu et al. (2026) | Exploration bottlenecks on hard problems | **STRONG OVERLAP** on hard problem exploration. |
| **P35** | *Debate on RLVR Capability Boundary* | Wang et al. (2026) | Two-stage shrinkage/expansion in RLVR | **STRONG OVERLAP** on RLVR capability boundaries. |
| **P36** | *EvoCoT: Overcoming Exploration Bottleneck* | Chen et al. (2026) | Evolutionary search for hard RLVR | **PARTIAL OVERLAP** on exploration search. |

---

## 2. SUBSTANTIVE REMAINING UNCLAIMED FRONTIER

While support expansion and test-time search have been studied separately, **no prior work systematically constructs the Pareto frontier of OOD reasoning generalization across the full intervention capacity hierarchy ($A_0 \to A_5$) under strictly matched total compute $C_{\text{total}}(Q) = C_{\text{train}} + Q \cdot C_{\text{inference}}$**.

Specifically, prior papers suffer from two major flaws:
1. They compare cheap test-time search ($A_1$) to full RL ($A_5$) without controlling for query volume $Q$ or training FLOPs.
2. They evaluate in-distribution benchmark accuracy rather than compositional OOD rule generalization ($D_{\text{OOD}}$).
