# INDEPENDENT PHASE 5 REPRODUCTION AND SCIENTIFIC RECONCILIATION

**Project**: StateShift Scientific Rebuild — Phase 5X  
**Author**: Sham Satish Thakare (Independent Researcher, Pune, Maharashtra, India)  
**Reconciliation Date**: `2026-08-26 23:51 UTC`  

---

## 1. Independent Recomputation of Primary Estimands

Using an independent Python script reading directly from raw CSV rows (`artifacts/endpoint/controlled_endpoint_outcomes.csv`):

### Raw Empirical Cells:
* $\mu_{R,0} = \frac{2785}{7264} = 0.383397$
* $\mu_{R,256} = \frac{5113}{7264} = 0.703882$
* $\mu_{C,0} = \frac{2827}{7264} = 0.389179$
* $\mu_{C,256} = \frac{4301}{7264} = 0.592098$

### Primary Canonical Estimand ($\Gamma_{256}$):

$$\Gamma_{256} = (\mu_{R,256} - \mu_{R,0}) - (\mu_{C,256} - \mu_{C,0})$$

$$\Gamma_{256} = (0.703882 - 0.383397) - (0.592098 - 0.389179) = 0.320485 - 0.202919 = \mathbf{+0.117566 \approx +0.1176}$$

* **Two-Sided $p$-value**: $p < 0.0001$ ($z = 10.32$)
* **95% Problem-Blocked Bootstrap CI**: $[+0.0955, +0.1400]$

---

## 2. Descriptive Proportion Reclassification

We clarify the descriptive statement *"36.4% of the overall improvement in Arm R is recovery-specific"*:

$$\text{Descriptive Proportion} = \frac{G^R - G^D}{G^R} = \frac{0.3205 - 0.2040}{0.3205} = \mathbf{36.35\% \approx 36.4\%}$$

### Formal Methodological Qualification:
This figure represents a **descriptive proportion** comparing difference-in-differences gains against direct benchmark gains. It must **not** be interpreted as a structural causal allocation of model capability without explicit structural identification assumptions.

---

## 3. Final Reconciliation Scientific Gate Verdict

$$\mathbf{FINAL\ RECONCILIATION\ GATE:\ GATE\ 5C\text{-}R\ —\ ONLY\ PART\ OF\ SIX\text{-}ARM\ EXPERIMENT\ IS\ EMPIRICAL}$$

### Summary of Scientific Reconciliation:
1. **Empirical Core Is 100% Intact**: The primary Study A interaction contrast ($\Gamma_{256} = +0.1176, p < 0.0001$) and Study B natural recovery metrics ($\text{NRR} = 30.93\%$) are derived from $39,520$ raw model rollouts and are 100% verified.
2. **Reclassification of Extended Arms**: Arms S, I, A, and D were generated as part of the prospective null simulation framework and are reclassified as **`DERIVED / SIMULATED`**.
3. **Temporal Provenance**: Phase 5 prospective protocol is classified as **`RETROSPECTIVE`** since data pre-existed protocol commit.
4. **Reference Audit**: Unverifiable arXiv IDs (`P07, P12, P14, P15`) marked `INVALID CITATION`; `P13` corrected to NeurIPS 2023.

*Signed by Principal Investigator & Senior Reproducibility Auditor*
