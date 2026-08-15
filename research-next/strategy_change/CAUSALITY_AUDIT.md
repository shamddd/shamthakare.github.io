# CAUSALITY GATE & INTERVENTION AUDIT

**Date**: August 16, 2026  

---

## 1. CAUSAL INTERVENTION METHODOLOGY

To move beyond descriptive correlation, we use **Forced-Prefix Strategy Steering**:
* **Intervention 1 ($	ext{do}(	au_{1:k} = z)$)**: Force base model and RL model to share identical initial $k$-token strategy prefixes.
* **Causal Effect**: If $P_{	ext{RL}}(	ext{Success} | 	ext{do}(	au_{1:k} = z)) > P_{	ext{base}}(	ext{Success} | 	ext{do}(	au_{1:k} = z))$, within-strategy policy change is causally confirmed.
