# BEST-OF-N CANDIDATE DEPENDENCE & CORRELATION AUDIT

**Date**: August 16, 2026  

---

## 1. EMPIRICAL CANDIDATE CORRELATION ANALYSIS

The Idealized IID Best-of-$N$ null assumes candidate completions are independent Bernoulli trials ($1 - (1-p)^N$).

* **Empirical Prompt-Level Pairwise Correlation**: $\rho_{\text{pairwise}} \approx +0.18$ on ModComp-5 (OOD length extrapolation).
* **Effective Sample Size ($N_{\text{eff}}$)**: For $N=32$, due to positive candidate correlation, $N_{\text{eff}} = \frac{N}{1 + (N-1)\rho} \approx \frac{32}{1 + 31(0.18)} = 4.86$.
* **Impact on Null Prediction**: Correlation reduces effective Best-of-$N$ search utility, making search even more expensive under OOD shift than predicted by the independent null.
