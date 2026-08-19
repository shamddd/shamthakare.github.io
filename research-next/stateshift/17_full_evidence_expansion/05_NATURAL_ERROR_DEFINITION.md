# PHASE 2 STAGE A — NATURAL ERROR EVENT DEFINITIONS

**Milestone**: Prospective Natural Error Classification  

---

## 1. Natural Error Criteria

A rollout contains a **`NATURAL_ERROR_EVENT`** iff:

1. **Model-Generated Error**: The error occurs spontaneously during unperturbed model decoding (zero prompt tampering or state injection).
2. **Verifier-Detectable Invalid Transition**: The rollout contains an intermediate step that violates deterministic mathematical rules (e.g. $12 + 7 = 21$), symbolic verifier constraints, or logical consistency.
3. **Non-Terminal Location**: The error occurs prior to the final answer box / target token position.

---

## 2. Survivor Bias & Control Denominator

Natural errors are endogenous model events. To prevent survivor bias:
* **Control Denominator**: Conditioned on rollouts containing a verified `NATURAL_ERROR_EVENT`.
* **Baseline Comparison**: Compared against (A) error-free rollouts on the same problem, and (B) token-matched baseline rollouts.

*Signed by Causal-Inference Reviewer & Statistical Methodologist*
