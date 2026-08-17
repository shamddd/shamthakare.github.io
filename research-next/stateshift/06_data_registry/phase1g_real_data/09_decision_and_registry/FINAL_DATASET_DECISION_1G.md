# FINAL DATASET DECISION — PHASE 1G

**Selected Decision**: **OPTION A: FILTERED MATH-500 PRIMARY**  
**Authoritative Decontaminated N**: `365` independent MATH-500 problems  
**Status**: **PASSED REGISTRY GATE**  

---

## 1. Decision Rationale

Real-data forensics yield N = 365 decontaminated, deterministically segmentable, and perturbation-eligible independent problems. This exceeds the minimum feasibility threshold (N >= 20) and provides sufficient statistical power to detect checkpoint trajectory shifts.

---

## 2. Evaluation Pool Hierarchy

1. **PRIMARY_CONSERVATIVE_POOL** ($N=365$): Decontaminated items completely free of RL-stage exact duplicates, high-confidence near duplicates, and structural numeric parameters. This is the **primary benchmark** for Study 1.
2. **SECONDARY_BROAD_POOL** ($N=500$): Broad evaluation set retained for secondary robustness checks.

---
**Verdict**: PROCEED TO STATE REGISTRY FREEZE.
