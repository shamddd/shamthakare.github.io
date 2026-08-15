# CORRELATED BEST-OF-N & DEPENDENCE DIAGNOSTIC MODEL

**Date**: August 16, 2026  

---

## 1. INTEGER SAMPLE COMPLEXITY & BOUNDARY CONDITIONS

For $p \in (0, 1)$ and $u \in (0, 1)$, exact integer sample complexity under independent Bernoulli sampling is:
$$N^*(p, u) = \left\lceil rac{\ln(1 - u)}{\ln(1 - p)} ightceil$$

### Boundary Conditions:
* $p = 0 \implies N^* = \infty$ (Utility $u>0$ unachievable).
* $p = 1 \implies N^* = 1$ for any $u \in (0, 1]$.
* $u = 0 \implies N^* = 0$.
* $u = 1 \implies N^* = \infty$ (100% certainty unachievable with finite $N$).

---

## 2. RETRACTION OF EXACT N_eff PASS@N INSERTION

> **REVISION NOTICE**: The formula $N_{	ext{eff}} = rac{N}{1 + (N-1)ho}$ measures **variance inflation** for exchangeable sample means. Inserting $N_{	ext{eff}}$ directly into $1 - (1-p)^{N_{	ext{eff}}}$ as an exact Pass@$N$ probability is mathematically unjustified.

We label $N_{	ext{eff}}$ strictly as a **"variance-based sample dependence diagnostic."** Empirical Pass@$N$ is evaluated directly from stored rollout groups.
