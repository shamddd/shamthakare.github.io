# PROPOSITION 1: FORMAL STATEMENT & DOMAIN ASSUMPTIONS

**Date**: August 16, 2026  

---

## PROPOSITION 1 (Inference Cost Scaling Under Base Accuracy Decay)

Let $p(d) \in (0, 1)$ be the single-sample success probability of a base model $A_0$ on task complexity $d$. Let candidate completions for Best-of-$N$ search ($A_1$) be independent and identically distributed Bernoulli random variables with parameter $p(d)$. Let $u \in (0, 1)$ be a target utility threshold.

1. The minimum sample count $N^*(p, u) \in \mathbb{R}^+$ required to achieve expected utility $U(A_1(N^*), d) \ge u$ is:
$$N^*(p, u) = rac{\ln(1 - u)}{\ln(1 - p(d))}$$

2. Under distribution shift $d_{	ext{IID}} 	o d_{	ext{OOD}}$ where $p(d_{	ext{OOD}}) < p(d_{	ext{IID}})$, the ratio of required search samples satisfies:
$$rac{N^*(p_{	ext{OOD}}, u)}{N^*(p_{	ext{IID}}, u)} = rac{\ln(1 - p(d_{	ext{IID}}))}{\ln(1 - p(d_{	ext{OOD}}))} > 1.0$$
