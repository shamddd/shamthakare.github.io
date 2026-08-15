# PRIMARY AND SECONDARY ESTIMANDS

**Date**: August 16, 2026  

---

## 1. PRIMARY QUANTITATIVE ESTIMANDS

1. **State Recovery Advantage**:
   $$A_{\text{recovery}}(s) = V^{\pi_{\text{FULL-RL}}}(s) - V^{\pi_{\text{BASE}}}(s)$$
2. **Differential Recovery Effect (Primary Result $\Gamma$)**:
   $$\Gamma = \mathbb{E}_{s \in S_R}[A_{\text{recovery}}(s)] - \mathbb{E}_{s \in S_C}[A_{\text{recovery}}(s)]$$
3. **Late-Decision Contrast ($\Delta_{\text{late}}$)**:
   $$\Delta_{\text{late}} = \Gamma_{\text{full}} - \Gamma_{\text{prefix}}$$

Primary Hypothesis $H_1: \Gamma > 0$ and $\Delta_{\text{late}} > 0.05$ on $D_{\text{structural\_OOD}}$.
