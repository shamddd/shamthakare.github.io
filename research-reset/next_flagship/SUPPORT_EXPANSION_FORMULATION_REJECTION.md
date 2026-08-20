# DECOMMISSION & REJECTION RECORD: FORMULATION 01 (LITERAL SUPPORT EXPANSION)

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  
**Status**: FORMULATION OFFICIALLY REJECTED & DECOMMISSIONED  

---

## 1. REJECTED FORMULATION SPECIFICATION

The previously proposed novelty boundary:
$$\mathcal{B}_{\text{rejected}} = \Big\{ D \;\Big|\; \text{Pass@10,000}(A_0, D) = 0 \quad \text{AND} \quad \text{Acc}(A_3, D) > 0.10 \Big\}$$
and the associated claim that $0 / 10,000$ empirical successes implies policy probability $p < 10^{-6}$, are **OFFICIALLY WITHDRAWN AND DECOMMISSIONED**.

---

## 2. REASON 1: STATISTICAL INVALIDITY OF THE PASS@10,000 BOUND

By the Rule of Three for binomial proportion estimation:
$$\text{Upper 95\% Confidence Bound for } p \text{ given } 0 \text{ successes in } N \text{ trials} \approx \frac{3}{N}$$
For $N = 10,000$:
$$p_{\text{upper, 95\%}} \approx \frac{3}{10,000} = 3 \times 10^{-4}$$

Zero observed successes in 10,000 rollouts does **NOT** establish $p < 10^{-6}$, nor does it prove that a solution lies outside the probability support of the base policy. Equating non-observation in a finite sample to mathematical zero-probability support is statistically fallacious.

---

## 3. REASON 2: DIRECT COLLISION WITH RECENT LITERATURE (SAGE ET AL., 2026)

Recent literature explicitly studies the distinction between sampling efficiency and empirical support expansion:
* **Lee, Kang, & Hwang (May 2026)**: *SAGE: Shaping Anchors for Guided Exploration in RLVR of LLMs* (`arXiv:2605.18864`). Explicitly investigates whether RLVR merely boosts sampling frequency of pre-existing modes versus expanding empirical reasoning support.
* **Zhao et al. (COLM 2025)**: *Echo Chamber* (`arXiv:2411.07643`). Demonstrates that RL fine-tuning primary amplifies pretrained behaviors.

Claiming empirical support expansion as an unexamined novel contribution collides directly with SAGE and Echo Chamber.

---

## 4. REASON 3: INABILITY TO DISTINGUISH RARE-EVENT AMPLIFICATION FROM CAPABILITY CREATION

Standard RLVR optimization increases the likelihood of high-reward trajectories. If a solution has base probability $p = 10^{-4}$, observing 0 successes in 1,000 samples is common ($P(\text{0 successes}) = (1 - 10^{-4})^{1000} \approx 90.5\%$). When RLVR increases its probability to $0.50$, it is performing **rare-event probability amplification**, not creating a new computational capability.

---

## 5. TERMINOLOGY RESET

The following terms are **PERMANENTLY RETIRED**:
* $\times$ "true support expansion"
* $\times$ "new capability outside support"
* $\times$ "zero-support capability"
* $\times$ "provably unavailable behavior"

The following statistically rigorous terms are **MANDATORY**:
* $\checkmark$ **Empirical success coverage**
* $\checkmark$ **Sampled behavioral coverage**
* $\checkmark$ **Pass@$k$ frontier**
* $\checkmark$ **Rare-event success probability**
* $\checkmark$ **Observed strategy diversity**
* $\checkmark$ **Behavioral reachability under a fixed sampling budget**
