# PRIMARY AND SUPPORTING ESTIMANDS V2

**Date**: August 16, 2026  

---

## 1. PRIMARY FLAGSHIP ESTIMAND ($\Delta_{\text{late}}$)

$$\Delta_{\text{late}} = \mathbb{E}_{s \in S_R}\left[V_{\text{FULL}}(s) - V_{\text{PREFIX}}(s)\right] - \mathbb{E}_{s \in S_C}\left[V_{\text{FULL}}(s) - V_{\text{PREFIX}}(s)\right]$$

* **Primary Hypothesis**: $\Delta_{\text{late}} > 0$.
* **Interpretation**: Full RLVR produces a selectively larger value advantage over PrefixRL on recovery states than on matched control states.

---

## 2. SUPPORTING ESTIMANDS

1. **$\Gamma_{\text{FULL}}$**: $\mathbb{E}_{S_R}[V_{\text{FULL}} - V_{\text{BASE}}] - \mathbb{E}_{S_C}[V_{\text{FULL}} - V_{\text{BASE}}]$.
2. **$\Gamma_{\text{PREFIX}}$**: $\mathbb{E}_{S_R}[V_{\text{PREFIX}} - V_{\text{BASE}}] - \mathbb{E}_{S_C}[V_{\text{PREFIX}} - V_{\text{BASE}}]$.
