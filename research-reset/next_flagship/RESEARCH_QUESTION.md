# FLAGSHIP RESEARCH QUESTION: INTERVENTION FRONTIERS

**Date**: August 16, 2026  
**Status**: PROPOSED NEW FLAGSHIP CANDIDATE (PHASE C DISCOVERY)  
**Author**: Antigravity Forensic Research Agent  

---

## 1. PRIMARY SCIENTIFIC QUESTION

$$\text{What is the minimum intervention complexity } A_k \in \{A_0, A_1, A_2, A_3, A_4, A_5\} \text{ required to produce a task capability improvement}$$
$$\text{that cannot be achieved by a Behavioral Reweighting Null } \mathcal{N}_{\text{reweight}}(A_1, N=10,000) \text{ on the base policy?}$$

---

## 2. INTERVENTION HIERARCHY $A_0 \to A_5$

* **$A_0$ (Greedy / Base Generation)**: Zero-shot/Few-shot generation under temperature $T=0$.
* **$A_1$ (Behavioral Reweighting Null — Best-of-$N$)**: Un-updated base policy generation under $T=0.7$ with top-$p=0.95$ for sample sizes $N \in \{1, 10, 100, 1000, 10000\}$ filtered by a deterministic verifier.
* **$A_2$ (Prefix / Prompt Steering)**: Soft-prompt insertion or hand-crafted system prompt steering without parameter updates.
* **$A_3$ (Parameter-Efficient RLVR — Prefix/LoRA RL)**: On-policy GRPO updating $< 0.5\%$ of parameters (prefix tokens or LoRA adapters).
* **$A_4$ (Parameter-Efficient Full SFT + RL)**: SFT warm-start followed by parameter-efficient GRPO.
* **$A_5$ (Full RLVR)**: Standard GRPO updating 100% of model parameters.

---

## 3. FORMAL DEFINITION OF "NEW CAPABILITY" (SUPPORT EXPANSION)

We define a **New Capability** not as a numerical bump on standard in-distribution benchmarks, but as **Empirical Support Expansion**:

$$\text{Support Expansion} \iff \text{Accuracy}(A_k, D_{\text{task}}) > 0.10 \quad \text{where} \quad \text{Pass@10,000}(A_0, D_{\text{task}}) = 0$$
$$\text{and} \quad P_{A_0}(\text{solution trajectory } \tau) < 10^{-6} \quad \forall \tau \in \text{valid solutions}$$

If $A_1$ Best-of-$10,000$ achieves non-zero accuracy ($> 0$), the task lies within the **Reweighting Frontier** of the base model, and higher-order interventions ($A_3, A_5$) are classified as **Distributional Reweighting**, not capability emergence.
