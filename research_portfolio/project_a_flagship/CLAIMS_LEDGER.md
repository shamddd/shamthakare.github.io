# CLAIMS & EVIDENCE LEDGER — PROJECT A (FLAGSHIP)

**Canonical Project Title**: *C3A: Causal Counterfactual Credit Assignment for Multi-Turn Tool-Using Foundation Agents*  
**Author**: Sham Thakare  
**Date**: August 2026  

---

## 1. Traceable Claims & Evidence Register

| Claim ID | Formal Scientific Claim | Required Experimental Evidence | Status |
| :--- | :--- | :--- | :--- |
| **CLM-01** | Standard outcome-supervised GRPO rewards redundant tool invocations in multi-turn agent rollouts. | Empirical tool redundancy count on InterCode & ToolBench across baseline GRPO rollouts. | `NOT YET MEASURED` |
| **CLM-02** | Token-mask ablation accurately approximates ground-truth Shapley credit in synthetic tool DAGs. | Correlation $r(\hat{\Phi}, \Phi^*)$ between C3A ablation weights and oracle Shapley values in `CausalTool-Env`. | `NOT YET MEASURED` |
| **CLM-03** | C3A achieves statistically significant Pass@1 improvement over standard GRPO and TCPO on held-out tasks. | 3-seed evaluation across InterCode-Bash, InterCode-SQL, and ToolBench with Welch's t-test ($p < 0.0125$). | `NOT YET MEASURED` |
| **CLM-04** | C3A reduces policy gradient empirical trace variance by $\ge 35\%$ over standard GRPO. | Batch-wise gradient variance logs across 1,000 training iterations. | `NOT YET MEASURED` |
| **CLM-05** | C3A significantly outperforms permuted-credit and random-weight negative controls. | Matched-seed comparison against $\text{C3A}_{\text{perm}}$ and $\text{C3A}_{\text{rand}}$. | `NOT YET MEASURED` |
| **CLM-06** | C3A maintains higher task success under synthetic tool latency and API failure jitter. | Robustness benchmark with 15% injected API noise rate. | `NOT YET MEASURED` |

---

## 2. Integrity Declaration

> **Strict No-Fabrication Protocol**: No numerical values, confidence intervals, p-values, or performance percentages have been populated prior to execution. All empirical status indicators are strictly set to `NOT YET MEASURED`. Numerical entries will only be inserted via automated, cryptographically hashed JSON artifact export pipelines.
