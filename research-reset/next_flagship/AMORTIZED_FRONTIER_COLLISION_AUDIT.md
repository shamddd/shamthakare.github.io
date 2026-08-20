# MANDATORY COLLISION AUDIT: AMORTIZED INTERVENTION FRONTIERS

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  
**Target Subject**: Deployment Horizon Amortization ($Q^*$), Matched Compute, and Candidate Re-Audits  

---

## 1. COMPREHENSIVE COLLISION LEDGER FOR FLAGSHIP CANDIDATE #1

| Index | Paper Title | Authors / Venue | Core Focus | Status vs Amortized Frontier $Q^*$ |
| :--- | :--- | :--- | :--- | :--- |
| **P37** | *Parameter-Efficient RL (PERL)* | Zhang et al. (ICLR 2026) | Prefix-RL ($A_2$) vs Full RL ($A_3$) | **STRONG OVERLAP** — Evaluates $A_2$ vs $A_3$, but lacks deployment query horizon $Q$ amortization model. |
| **P38** | *Well Begun, Half Done: Prefix Optimization for Reasoning* | Liu et al. (2025/2026) | Soft prefix initialization for RLVR | **PARTIAL OVERLAP** — Focuses on prefix initialization, not deployment cost crossover. |
| **P39** | *Scaling Test-Time Compute Without Verification is Suboptimal* | Wang et al. (2025/2026) | Best-of-$N$ ($A_1$) + verifier bounds | **STRONG OVERLAP** — Identifies verifier cost in $A_1$, but does not parameterize against training FLOPs $C_{\text{train}}$. |
| **P40** | *sGPO: Trading Inference FLOPs for Training Efficiency* | Park et al. (2025/2026) | Sparse GPO to balance FLOPs | **STRONG OVERLAP** — Trades training FLOPs for rollout FLOPs, but ignores query lifetime $Q^*$. |
| **P41** | *FLOP-Efficient Training via Test-Time Awareness* | Kim et al. (2026) | Early stopping during RLVR | **PARTIAL OVERLAP** — Focuses on stopping training early based on test-time search performance. |
| **P42** | *Test-Time Scaling in Reasoning LLMs: Regimes & Reproducibility* | Zhang et al. (2025/2026) | Comprehensive test-time scaling empirical survey | **STRONG OVERLAP** on $A_1$ scaling laws. |
| **P43** | *When To Solve, When To Verify* | Agrawal et al. (2025/2026) | Verifier cost vs generator cost trade-offs | **PARTIAL OVERLAP** on verifier cost inclusion. |
| **P44** | *Amortized Reasoning Tree Search* | Wu et al. (2025/2026) | Policy distillation from tree search | **STRONG OVERLAP** — Distills search into weights, but treats search as training target rather than deployment competitor. |

---

## 2. RE-AUDIT OF CANDIDATE #2 (AUTONOMOUS TEST-TIME COMPUTE ALLOCATION)

* **Newly Identified Collision Paper**: *Adaptive Test-Time Compute Allocation for Reasoning LLMs via Constrained Policy Optimization* (`arXiv:2604.14853`, April 2026).
* **Collision Analysis**: `arXiv:2604.14853` already formulates adaptive test-time compute allocation under constrained optimization and verification budgets. Claiming stochastic/heavy-tailed latency as the sole distinction is insufficient to guarantee novelty.
* **DOWNGRADE STATUS**: **`HIGH COLLISION / DOWNGRADED TO UNVIABLE`**.

---

## 3. RE-AUDIT OF CANDIDATE #3 (MULTI-AGENT VCG CONTEXT ALLOCATION)

* **Newly Identified Collision Papers**: *Economy of Minds* (2025) and *Test-Time Compute Games* (2025).
* **Collision Analysis**: Market-based token allocation and game-theoretic compute games among LLM agents have been explored in recent multi-agent economics literature. Using VCG auctions without a fundamental theoretical breakthrough constitutes novelty decoration.
* **DOWNGRADE STATUS**: **`HIGH COLLISION / DOWNGRADED TO UNVIABLE`**.

---

## 4. REMAINING UNCLAIMED FRONTIER FOR CANDIDATE #1

Candidate #1 (**Amortized Intervention Frontiers**) remains the **ONLY SCIENTIFICALLY DEFENSIBLE CANDIDATE**, provided it strictly answers:

> **The Amortization Crossover Problem**: What is the analytical and empirical break-even query horizon $Q^*(A_i, A_j)$ where one-time training compute $C_{\text{train}}$ is fully amortized, and how does task difficulty $d$ and OOD compositional shift alter the compute-optimal intervention region $a^*(Q, d)$?
