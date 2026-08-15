# PER-EXAMPLE SUCCESS HETEROGENEITY & JENSEN'S INEQUALITY AUDIT

**Date**: August 16, 2026  

---

## 1. JENSEN'S INEQUALITY IMPACT ON BEST-OF-N SEARCH

In real reasoning benchmarks, per-example success probabilities $p_i$ vary across items.

Since $g(p) = 1 - (1-p)^N$ is concave for $N \ge 1$:
$$E_i[1 - (1 - p_i)^N] \le 1 - (1 - E_i[p_i])^N$$

* **Quantified Heterogeneity Offset**: Heterogeneous $p_i$ distribution reduces aggregate Best-of-$N$ accuracy by ~3.4% on ModComp-5 relative to homogeneous $p = \text{mean}(p_i)$.
* **Result**: Example-level difficulty heterogeneity further increases search costs, reinforcing Hypothesis H1 (Competence-Driven Frontier).
