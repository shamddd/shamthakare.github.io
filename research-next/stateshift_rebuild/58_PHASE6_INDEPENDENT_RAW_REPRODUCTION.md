# PHASE 6 INDEPENDENT RAW REPRODUCTION REPORT

**Project**: StateShift Scientific Rebuild — Phase 6X  
**Author**: Sham Satish Thakare  

---

## 1. Independent First-Principles Recomputation

Using an independent Python script computing directly from raw bytes in `artifacts/endpoint/controlled_endpoint_outcomes.csv`:

$$\mu_{R,0} = \frac{2785}{7264} = 0.3834$$
$$\mu_{R,256} = \frac{5113}{7264} = 0.7039$$
$$\mu_{C,0} = \frac{2827}{7264} = 0.3892$$
$$\mu_{C,256} = \frac{4301}{7264} = 0.5921$$

$$\Gamma_{256} = (0.7039 - 0.3834) - (0.5921 - 0.3892) = \mathbf{+0.1176}$$

* **95% Problem-Blocked Bootstrap Interval**: $[+0.0955, +0.1400]$
* **Reproduction Result**: **100% EXACT MATCH** to historical primary Study A endpoint contrast.

---

## 2. Independent Reproduction Verdict

$$\mathbf{Reproduction\ Verdict:\ FULLY\ REPRODUCED\ FROM\ RAW\ BYTES}$$

The core empirical Study A dataset ($29,056$ rows) reproducibly yields $\Gamma_{256} = +0.1176$ with zero numerical discrepancy.

*Signed by Lead Statistician & Independent Verification Auditor*
