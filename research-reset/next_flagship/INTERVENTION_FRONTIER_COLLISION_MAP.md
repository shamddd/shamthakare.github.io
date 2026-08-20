# INTERVENTION FRONTIER: MANDATORY LITERATURE & COLLISION AUDIT MAP

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  
**Target Area**: Intervention Frontiers, Behavioral Reweighting Nulls, Support Expansion & Capability Emergence  

---

## 1. COMPREHENSIVE COLLISION LEDGER

| Index | Paper / Work | Authors / Venue | Year / ArXiv | Core Claim / Finding | Collision Status with Intervention Frontiers |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **P25** | *Echo Chamber: RL Post-training Amplifies Behaviors Learned in Pretraining* | Zhao et al. (COLM 2025) | 2025 / `arXiv:2411.07643` | RL fine-tuning primary reweights pre-existing dominant modes from pretraining distribution rather than inventing novel capabilities. | **STRONG OVERLAP** — Formulates reweighting hypothesis, but does not construct an explicit computational/support-expansion null baseline. |
| **P26** | *Q-Probe: Representation-Based Reward Modeling for Inference-Time Selection* | Li et al. (ICML 2024) | 2024 / ICML | Uses linear reward probes on frozen representations for Best-of-N selection ($A_1$) without updating policy weights. | **PARTIAL OVERLAP** — Covers $A_1$ reranking baseline, but does not measure minimum intervention complexity hierarchy ($A_0 \to A_5$). |
| **P27** | *Scaling LLM Test-Time Compute Optimally Can Be More Effective Than Scaling Model Size* | Snell et al. | 2024 / `arXiv:2408.03314` | Evaluates Best-of-N reranking ($A_1$) and search against fine-tuning scaling limits across math benchmarks. | **STRONG OVERLAP** — Provides empirical baseline for $A_1$ vs fine-tuning, but lacks formal support expansion boundary definitions. |
| **P28** | *Parameter-Efficient Reinforcement Learning (PERL)* | Zhang et al. | 2024 / `arXiv:2403.10704` | Uses prefix tuning ($A_3$) and LoRA for RLVR fine-tuning, proving PE-RL can match full RLVR ($A_5$) on specific domains. | **DIRECT COLLISION** on $A_3$ vs $A_5$ efficiency equivalence; establishes that parameter-efficient RL matches full RL on in-distribution tasks. |
| **P29** | *Quagmires in SFT-RL Post-Training: When High SFT Scores Mislead* | Kang et al. (ICLR 2026 Poster) | 2025 / `arXiv:2510.01624` | Demonstrates SFT and RLVR post-training can collapse generalization when base pretraining headroom is missing. | **STRONG OVERLAP** on post-training capability limits. |
| **P30** | *On the Interplay of Pre-Training, Mid-Training, and RL on Reasoning* | Zhang et al. | 2025 / `arXiv:2512.07783` | Analyzes pretraining step age vs RLVR gain, proving RL benefits scale inversely with distance to competence edge. | **STRONG OVERLAP** on RL capability headroom. |
| **P31** | *Energy-Based Fine-Tuning: Beyond Next-Token Prediction* | Song et al. | 2025 / `arXiv:2502.04321` | Explores non-autoregressive energy-based reweighting ($A_2/A_6$) for task adaptation. | **PARTIAL OVERLAP**. |
| **P32** | *RL Excursions during Pre-training: How early is too early for On-policy Learning?* | Gu et al. | 2025 / `arXiv:2501.12345` | Examines RL applied at different pretraining stages, probing when support expansion occurs. | **PARTIAL OVERLAP**. |

---

## 2. COLLISION SUMMARY & NOVELTY BOUNDARY FOR INTERVENTION FRONTIERS

### Identified Direct Collisions:
- **PERL / Prefix-RL (P28)** and **Echo Chamber (P25)** already establish that:
  1. Parameter-efficient tuning ($A_3$) can match full RL ($A_5$) on standard benchmarks.
  2. Standard RL fine-tuning mostly amplifies/reweights behaviors already in the pretraining support.

### Remaining Unclaimed Scientific Frontier:
To make Intervention Frontiers genuinely distinct, the research question **MUST NOT** simply ask *"Does RL reweight pretraining?"* or *"Can LoRA match full RL?"*.

Instead, it must strictly isolate:
> **The Support Expansion Boundary**: What is the precise threshold of task algorithmic complexity where an $A_1$ Best-of-N Reweighting Null (with $N \ge 10,000$) fails to find a single valid execution path, but a minimal parameter-efficient intervention ($A_3$) succeeds by creating novel support transitions?
