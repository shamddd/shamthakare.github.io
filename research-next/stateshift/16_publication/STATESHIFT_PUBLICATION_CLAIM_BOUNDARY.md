# STATESHIFT PUBLICATION CLAIM BOUNDARY SPECIFICATION

**Milestone**: Phase 1L.0 Publication Claim Boundaries  
**Lock Timestamp**: `2026-08-20 01:44 UTC`  
**Auditor**: Top-Tier Reviewer & Scientific Integrity Auditor  

---

## 1. Permitted Publication Claims

1. **State-by-Checkpoint Interaction**: From checkpoint $t=0$ to $t=256$, target-transition success increased by $11.76$ percentage points more in the Recovery condition than in the matched Control condition ($\Gamma_{256} = 0.1176$, 95% bootstrap CI $[0.0955, 0.1400]$, $p < 0.0001$).
2. **Baseline Parity**: Prior to fine-tuning ($t=0$), Recovery ($38.34\%$) and Control ($38.92\%$) target-transition success rates are statistically indistinguishable ($\Delta = -0.58$ percentage points, $p = 0.68$).
3. **Contamination Robustness**: The strict contamination-filtered sensitivity analysis ($N=388$) confirms an $11.60$-percentage-point interaction ($\Gamma_{256,\text{Strict}} = 0.1160$, 95% CI $[0.0913, 0.1408]$, $p < 0.0001$).
4. **Behavioral Shift**: Fine-tuning induces an endpoint state-selective behavioral shift in target-transition capability.

---

## 2. Prohibited Publication Claims

* ❌ Causal claims unsupported by design (e.g. "fine-tuning causes intelligence").
* ❌ Mechanistic claims regarding internal neural representation shifts.
* ❌ Natural self-correction claims.
* ❌ Trajectory claims (monotonicity, emergence timing, local peaks, inflection points across unobserved steps $t \in \{32..224\}$).
* ❌ Relative percentage ratio claims (e.g. "11.76% acceleration" or "11.76% better").

*Signed by Top-Tier Reviewer & Scientific Integrity Auditor*
