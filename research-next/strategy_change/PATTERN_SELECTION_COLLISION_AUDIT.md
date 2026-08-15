# COLLISION AUDIT: PATTERN SELECTION IN RL (Chen et al., ICLR 2026 Poster)

**Date**: August 16, 2026  
**Auditor**: Lead Adversarial Novelty Auditor  

---

## 1. COMPREHENSIVE EXTRACTION OF PRIOR ART

* **Reference**: Chen, Li, Zou, *"Reshaping Reasoning in LLMs: A Theoretical Analysis of RL Training Dynamics through Pattern Selection"*, ICLR 2026 Poster.
* **Core Contribution & Established Findings**:
  1. **Pattern Reweighting**: Proves theoretically and empirically that RL post-training primarily reshapes reasoning-pattern distributions ($P_{\text{RL}}(z)$) by optimizing a sparse set of critical decision tokens.
  2. **Pattern Stability**: Demonstrates that pattern-specific success rates ($P(\text{Success}|z)$) remain comparatively stable throughout RLVR training.
  3. **Base-Model Mode Dependence**: Shows RLVR convergence is bounded by the quality and diversity of pre-existing base model patterns.

---

## 2. IMPACT ON OUR NOVELTY CLAIMS

* **Retraction**: Any claim that *"showing RL reweights existing strategy distributions is novel"* is **TOTALLY DESTROYED AND KNOWN PRIOR ART**.
* **Surviving Boundary**: Testing whether RL modifies action distributions $\pi_{\text{RL}}(\cdot|s_k)$ **within an externally controlled, state-matched recovery environment $s_k$** after the pattern/strategy has already been fixed.
