# CROSSOVER THEOREM: FORMAL PROOF OF SUFFICIENT CONDITIONS

**Date**: August 16, 2026  

---

## THEOREM 1 (Deployment Frontier Contraction Under Base Competence Shift)

Let $A_1$ be an inference-time search strategy (e.g., Best-of-$N$) with $C_{	ext{train}}(A_1) = 0$, and let $b$ be an up-front adaptation method with $C_{	ext{train}}(b) > 0$. Let $D_{	ext{IID}}$ and $D_{	ext{OOD}}$ be task distributions with base single-sample success probabilities $p_{	ext{IID}} > p_{	ext{OOD}} > 0$.

### SUFFICIENT CONDITIONS FOR $Q^*(A_1, b; D_{	ext{OOD}}, u) < Q^*(A_1, b; D_{	ext{IID}}, u)$:
Suppose:
1. **Target Utility Feasibility**: $U(b; D_{	ext{IID}}) \ge u$ and $U(b; D_{	ext{OOD}}) \ge u$.
2. **Fixed Up-Front Adaptation Cost**: $C_{	ext{train}}(b; D_{	ext{IID}}) = C_{	ext{train}}(b; D_{	ext{OOD}}) = C_{	ext{train}}(b)$.
3. **Search Cost Explosion**: $C_{	ext{infer}}(A_1; D_{	ext{OOD}}, u) > C_{	ext{infer}}(A_1; D_{	ext{IID}}, u)$.
4. **Bounded Adaptation Inference Growth**: $C_{	ext{infer}}(b; D_{	ext{OOD}}, u) - C_{	ext{infer}}(b; D_{	ext{IID}}, u) < C_{	ext{infer}}(A_1; D_{	ext{OOD}}, u) - C_{	ext{infer}}(A_1; D_{	ext{IID}}, u)$.

### PROOF:
Under Conditions 1--4, the denominator difference satisfies:
$$[C_{	ext{infer}}(A_1; D_{	ext{OOD}}, u) - C_{	ext{infer}}(b; D_{	ext{OOD}}, u)] > [C_{	ext{infer}}(A_1; D_{	ext{IID}}, u) - C_{	ext{infer}}(b; D_{	ext{IID}}, u)] > 0$$

Taking reciprocals (since both denominators are strictly positive):
$$rac{1}{C_{	ext{infer}}(A_1; D_{	ext{OOD}}, u) - C_{	ext{infer}}(b; D_{	ext{OOD}}, u)} < rac{1}{C_{	ext{infer}}(A_1; D_{	ext{IID}}, u) - C_{	ext{infer}}(b; D_{	ext{IID}}, u)}$$

Multiplying by fixed numerator $C_{	ext{train}}(b) > 0$:
$$Q^*(A_1, b; D_{	ext{OOD}}, u) < Q^*(A_1, b; D_{	ext{IID}}, u) \quad lacksquare$$
