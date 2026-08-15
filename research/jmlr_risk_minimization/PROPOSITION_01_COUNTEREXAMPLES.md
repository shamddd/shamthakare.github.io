# PROPOSITION 1: RED TEAM COUNTEREXAMPLE AUDIT

**Date**: August 16, 2026  

---

## COUNTEREXAMPLE AUDIT: WHEN DOES $R_f < 1.0$ FAIL?

Proposition 1 proves $N^*(p_{	ext{OOD}}) > N^*(p_{	ext{IID}})$, but does **NOT** universally guarantee $R_f < 1.0$ for total deployment costs if domain assumptions are violated.

### Counterexamples Where $R_f \ge 1.0$:
1. **Counterexample 1 (RLVR OOD Collapse)**: If the post-trained RLVR policy $A_3$ fails to generalize to OOD ($p_{	ext{RL}}(d_{	ext{OOD}}) < u$), $A_3$ cannot meet target utility $u$, rendering $Q^*_{	ext{frontier}}$ undefined or infinite.
2. **Counterexample 2 (Dominant Training Cost Growth)**: If OOD RLVR post-training requires massive additional training compute $C_{	ext{train, OOD}} \gg C_{	ext{train, IID}}$, the numerator of $Q^*_{	ext{OOD}}$ expands faster than search inference costs.
3. **Counterexample 3 (Verifier Cost Collapse)**: If verifier evaluation cost drops to zero ($C_{	ext{ver}} 	o 0$), Best-of-$N$ inference remains cheap despite sample growth.

*Conclusion*: Proposition 1 requires explicit domain bounds ($A_3$ retains utility $u$, training cost fixed).
