# NEW FLAGSHIP STAGE 1: PROBLEM FORMULATION

**Date**: August 16, 2026  
**Target Alignment**: Harvard ML Foundations / Kempner Institute (Sham Kakade Alignment)  

---

## 1. CENTRAL RESEARCH QUESTION

$$\boxed{\text{When does RL post-training merely reweight reasoning strategies already expressed by the base model, and when does it learn a genuinely different state-dependent reasoning policy?}}$$

---

## 2. FORMAL MECHANISTIC DECOMPOSITION

Let $x$ be a reasoning prompt, $\tau = (s_0, a_1, s_1, \dots, a_T, s_T)$ be a reasoning trajectory, and $z$ be a latent/observable strategy motif (e.g., direct derivation, decomposition, backward search, revision, backtracking).

We decompose RL post-training utility improvements into two distinct terms:
$$\text{RL Improvement} = \underbrace{\text{Strategy Selection Effect}}_{P_{\text{RL}}(z|x) \neq P_{\text{base}}(z|x)} + \underbrace{\text{Within-Strategy Policy Change}}_{P_{\text{RL}}(\tau|z, x) \neq P_{\text{base}}(\tau|z, x)}$$

### Two Competing Hypotheses:
1. **$H_{\text{REWEIGHT}}$ (Strategy Selection Null)**:
   $$P_{\text{RL}}(z|x) \neq P_{\text{base}}(z|x) \quad \text{and} \quad P_{\text{RL}}(\tau|z, x) \approx P_{\text{base}}(\tau|z, x)$$
   RL post-training merely re-allocates probability mass toward successful pre-existing base model strategies.

2. **$H_{\text{STRUCTURAL}}$ (Structural Policy Change Hypothesis)**:
   $$P_{\text{RL}}(\tau|z, x) \not\approx P_{\text{base}}(\tau|z, x)$$
   RL post-training alters the conditional trajectory mechanism itself—learning novel state-dependent transitions (e.g., mid-trajectory error recovery, dynamic verification, adaptive backtracking).
