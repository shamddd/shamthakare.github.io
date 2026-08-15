# PROPOSITION 1: MATHEMATICAL PROOF

**Date**: August 16, 2026  

---

## PROOF OF PROPOSITION 1

### Part 1: Sample Count Derivation
The success probability of Best-of-$N$ under independent Bernoulli sampling is $1 - (1 - p(d))^N$.
Setting $1 - (1 - p(d))^N = u$:
$$(1 - p(d))^N = 1 - u$$
$$N \ln(1 - p(d)) = \ln(1 - u)$$
Since $p(d) \in (0, 1)$, $\ln(1 - p(d)) < 0$. Dividing both sides:
$$N^*(p, u) = rac{\ln(1 - u)}{\ln(1 - p(d))} \quad lacksquare$$

### Part 2: Ratio Inequality
For $0 < p(d_{	ext{OOD}}) < p(d_{	ext{IID}}) < 1$:
$$0 < 1 - p(d_{	ext{IID}}) < 1 - p(d_{	ext{OOD}}) < 1$$
Taking natural logarithms (monotonically increasing):
$$\ln(1 - p(d_{	ext{IID}})) < \ln(1 - p(d_{	ext{OOD}})) < 0$$
Dividing by $\ln(1 - p(d_{	ext{OOD}})) < 0$ flips the inequality sign:
$$rac{\ln(1 - p(d_{	ext{IID}}))}{\ln(1 - p(d_{	ext{OOD}}))} > 1.0 \quad lacksquare$$
