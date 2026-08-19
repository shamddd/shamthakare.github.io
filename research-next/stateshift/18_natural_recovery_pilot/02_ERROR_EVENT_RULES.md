# PHASE 2 STAGE C0 — NATURAL ERROR EVENT CLASSIFICATION RULES

**Milestone**: Natural Error Identification Specification  

---

## 1. Classification Criteria for `NATURAL_ERROR_EVENT`

A rollout contains a **`NATURAL_ERROR_EVENT`** iff:

1. **Unprompted Generation**: The rollout was generated without external error injection or prompt tampering.
2. **Verifier-Groundable Invalid Transition**: An intermediate step contains an objective mathematical, algebraic, or arithmetic inconsistency (e.g. $15 \times 4 = 50$, or incorrect variable substitution) verified deterministically.
3. **Non-Terminal Position**: The error occurs prior to the final boxed answer (`\boxed{...}`).
4. **Primary Unit**: First qualifying natural error per rollout (to prevent double-counting dependent downstream errors).

*Signed by Causal-Inference Reviewer & Statistical Methodologist*
