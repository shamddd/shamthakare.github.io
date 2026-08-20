# COLLISION AUDIT: SNELL ET AL. (ICLR 2025, arXiv:2408.03314)

**Date**: August 16, 2026  

---

## 1. ESTABLISHED PRIOR ART BY SNELL ET AL.

* **Reference**: Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar, *"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning"*, ICLR 2025 (arXiv:2408.03314).
* **Established Findings**:
  1. **Prompt Difficulty**: Search efficiency degrades non-linearly on difficult prompts (low base accuracy $p$).
  2. **FLOP Allocation**: Test-time search scaling beats parameter scaling only up to a difficulty-dependent threshold.
  3. **Best-of-$N$ Saturation**: Naive Best-of-$N$ saturates rapidly as base competence drops.

*Conclusion*: Prompt-difficulty-dependent search degradation is fully established prior art.
