# REFINED COLLISION TAXONOMY & PRIOR ART BOUNDARIES

**Date**: August 16, 2026  
**Auditor**: Lead Scientific & Literature Auditor  

---

## 1. REFINED COLLISION CLASSIFICATIONS

1. **Metrical Task Systems & Rent-or-Buy (Classical Online Decision Theory)**:
   > **Classification**: Under simplified stationary-cost, fixed-state, and metric switching assumptions, important subclasses reduce to or strongly overlap with classical online decision problems such as Metrical Task Systems (MTS) and rent-or-buy variants.
   > **Preserved Learning-Specific Gaps**: Classical MTS does not automatically capture intervention-dependent future model state $M_{t+1}$, stochastic competence changes $p_t$, non-stationary task distributions $D_t$, non-metric switching costs, adaptation staleness, catastrophic forgetting, or delayed adaptation benefits.

2. **OAKS (Continual Online Adaptation Benchmark / 2025)**:
   > **Classification**: **`STRONG EMPIRICAL ADJACENCY / PARTIAL COLLISION`**. OAKS benchmarks online adaptation to changing knowledge streams, but does not by itself solve adaptation-vs-search deployment control.

3. **RTTC (Real-Time Test-Time Strategy Selection / 2025)**:
   > **Classification**: **`STRONG OVERLAP`** on adaptive per-query strategy selection. It is not identical to long-horizon parameter-updating adaptation decisions.

4. **Sleep-time Compute (Lin et al., 2025, arXiv:2504.13171)**:
   > **Classification**: **`STRONG CONCEPTUAL OVERLAP`** on amortizing offline compute over multiple future queries. It does not necessarily cover parameter-updating adaptation such as SFT/LoRA/RLVR.

5. **Snell et al. (ICLR 2025, arXiv:2408.03314)**:
   > **Classification**: **`STRONG OVERLAP`** on difficulty/competence-conditioned test-time compute; **`PARTIAL OVERLAP`** on one-time learned adaptation vs repeated search.
