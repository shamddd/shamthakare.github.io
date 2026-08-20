# CONTROLLED TESTBED DESIGN (DESIGN ONLY — NO EXECUTION)

**Date**: August 16, 2026  

---

## 1. ENVIRONMENT SPECIFICATIONS

* **Environment A (Prefix-Decidable Graph Search)**: Target node reachable by picking correct initial edge.
* **Environment B (Forced-Backtracking Maze / Graph)**: Initial edges lead to dead-ends; requires recognizing dead-end state and emitting explicit backtrack token.
* **Environment C (Late Branch-Switch Arithmetic)**: ModComp variant with mid-trajectory operator re-evaluation.

**Evaluated Conditions**:
1. Base Model $M_0$
2. Prefix-RL Model $M_{	ext{Prefix}}$
3. Full RLVR Model $M_{	ext{Full}}$
