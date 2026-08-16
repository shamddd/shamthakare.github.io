# RED-TEAM AUDIT: INTERVENTION EFFICIENCY FRONTIERS

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

---

## 1. RED-TEAM CRITIQUE & RESPONSES

| Red-Team Question | Critical Risk | Mitigating Scientific Framing |
| :--- | :--- | :--- |
| **Q1: Is this just an engineering benchmark?** | Risk of producing an empirical lookup table without generalizable insights. | Must focus on **OOD compositional generalization** ($D_{\text{OOD}}$) and theoretical amortization threshold $Q^*$, not static in-distribution scores. |
| **Q2: Does PERL / Prefix-RL (2026) already cover $A_3$ vs $A_5$?** | High risk of collision if we only compare Prefix to Full RL. | We compare the entire Pareto frontier ($A_0 \to A_5$) under **strictly matched total compute $C_{\text{total}}(Q)$**, which PERL did not do. |
| **Q3: Is total-compute normalization unfair to one-time training costs?** | One-time training cost $C_{\text{train}}$ dominates for small $Q$, while inference $C_{\text{inf}}$ dominates for large $Q$. | Formally parameterize by query volume $Q$ and solve for the exact **Amortization Horizon $Q^*$** where parameter updates outperform inference search. |
| **Q4: Can differences be explained by hyperparameter tuning?** | If $A_3$ fails simply due to bad learning rate, the frontier is artifactual. | Enforce pre-registered grid search over learning rate and prefix length across all conditions. |

---

## 2. POTENTIAL OUTCOME CATEGORIES & SCIENTIFIC VALUE

Regardless of the empirical outcome, the experiment yields a clean scientific answer:

* **Outcome A (Full RL Unnecessary)**: Low-dimensional steering/prefix ($A_3$) matches full RL ($A_5$) across all $Q$ and OOD tests at matched compute $\implies$ Full RLVR is computationally wasteful for post-training reasoning.
* **Outcome B (Capacity Threshold)**: Full RL ($A_5$) is required only past a specific OOD rule composition depth $d^* \ge 4$ $\implies$ Establishes exact task complexity regime where parameter modification outperforms search.
* **Outcome C (Compute Dominance)**: Performance collapses onto a single master curve determined solely by total FLOPs $C_{\text{total}}$, independent of $A_k$ level $\implies$ Compute equivalence theorem for post-training.
* **Outcome D (Amortization Dominance)**: Best-of-$N$ ($A_1$) dominates for $Q < 10^5$, while Full RL ($A_5$) dominates for $Q > 10^5$ $\implies$ Establishes practical deployment boundaries for LLM reasoning systems.
