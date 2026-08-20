# PRACTICAL SERVING DECISION RULE FOR REASONING SYSTEMS

**Date**: August 16, 2026  

---

## GENERIC SERVING DECISION BOUNDARY

For any generic adaptation method $b$ (e.g., SFT, LoRA, RLVR, Full Fine-Tuning) and search method $a$ (e.g., Best-of-$N$, MCTS):

**Deploy Adaptation $b$ over Search $a$ IF AND ONLY IF**:
$$Q > Q^*(a, b; D, u) = rac{C_{	ext{train}}(b) - C_{	ext{train}}(a)}{C_{	ext{infer}}(a; D, u) - C_{	ext{infer}}(b; D, u)}$$

under feasibility constraints $U(a; D) \ge u$ and $U(b; D) \ge u$.
