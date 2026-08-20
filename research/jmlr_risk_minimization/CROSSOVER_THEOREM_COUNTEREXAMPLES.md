# CROSSOVER THEOREM: COUNTEREXAMPLE AUDIT

**Date**: August 16, 2026  

---

## COUNTEREXAMPLES VIOLATING SUFFICIENT CONDITIONS

1. **Violation of Condition 1 (Adaptation OOD Infeasibility)**: If adaptation method $b$ fails on OOD ($U(b; D_{	ext{OOD}}) < u$), $Q^*_{	ext{OOD}} = \infty > Q^*_{	ext{IID}}$.
2. **Violation of Condition 4 (Excessive Adaptation Inference Cost Growth)**: If adapted model responses lengthen drastically on OOD such that $C_{	ext{infer}}(b; D_{	ext{OOD}}) - C_{	ext{infer}}(b; D_{	ext{IID}}) \ge C_{	ext{infer}}(A_1; D_{	ext{OOD}}) - C_{	ext{infer}}(A_1; D_{	ext{IID}})$, denominator contracts or flips sign, yielding $Q^*_{	ext{OOD}} \ge Q^*_{	ext{IID}}$.
