# BASELINE COMPLETENESS & SEARCH VARIATION AUDIT

**Date**: August 16, 2026  
**Auditor**: ML Baselines Reviewer  

---

## 1. EVALUATED VS PROPOSED SEARCH BASELINES

| Baseline | Evaluated in E0? | Reviewer Demand Risk | Impact on Frontier Shift |
| :--- | :--- | :--- | :--- |
| **Best-of-N (Deterministic Verifier)** | `YES ($N \le 32$)` | Baseline standard | Charges full verifier execution per candidate. |
| **Self-Consistency (Majority Vote)** | `PROPOSED E2` | Moderate | Requires no verifier, but lower peak utility. |
| **Verifier-Guided Tree Search (MCTS/MCTS-lite)** | `PROPOSED E2` | High for JMLR | Adds node-expansion search compute. |
