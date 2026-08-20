# ONLINE ADAPTATION-OR-SEARCH UNDER UNKNOWN DEPLOYMENT HORIZON

**Date**: August 16, 2026  

---

## 1. FORMULATION OF DYNAMIC SKI-RENTAL WITH COMPETENCE DRIFT

When task distribution $D_t$ drifts over time, base competence $p_t$ fluctuates, making per-query savings $s_t = c_{	ext{search}}(p_t) - c_{	ext{adapt}}(p_t)$ dynamic.

The optimal online stopping time $	au^*$ satisfies:
$$\sum_{t=1}^{	au^*} s(p_t) \ge F$$

This provides a generalized Ski-Rental formulation for LLM deployment under competence drift.
