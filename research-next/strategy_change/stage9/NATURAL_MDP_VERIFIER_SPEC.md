# NATURAL REASONING MDP & OBJECTIVE VERIFIER SPECIFICATION

**Date**: August 16, 2026  

---

## 1. TWO OBJECTIVE VERIFIABLE REASONING DOMAINS

1. **Domain 1: Mathematical Reasoning (GSM8K / MATH Executable Subset)**:
   - Intermediate state $s_t$: Step-by-step mathematical derivation.
   - Objective Verifier: SymPy / Python AST execution checking intermediate numerical values and algebraic equivalences.
   - Recovery State ($s \in S_R$): Derivation containing an identifiable arithmetic/algebraic error at step $t-1$, but where an executable corrective step $t$ leads to the correct final answer.

2. **Domain 2: Programmatic Reasoning (MBPP / HumanEval Program Repair Subset)**:
   - Intermediate state $s_t$: Partial Python implementation / draft function.
   - Objective Verifier: Unit test suite execution ($T_{\text{tests}}$).
   - Recovery State ($s \in S_R$): Code draft that fails $\ge 1$ test assertion, but where a single modular edit/patch $a_{\text{repair}}$ yields 100% test pass.
