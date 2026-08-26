# PHASE 5 ESTIMAND AND HYPOTHESIS RECONCILIATION

**Project**: StateShift Scientific Rebuild — Phase 5X  
**Author**: Sham Satish Thakare  

---

## 1. Estimand Reconciliation & Disambiguation

We reconcile the primary estimand definitions used across the StateShift project to prevent notation collision:

### Primary Canonical Estimand ($\Gamma_t$)
Defined as the difference-in-differences interaction contrast between Recovery ($R$) and Matched Control ($C$):

$$\Gamma_t = (p_{R,t} - p_{R,0}) - (p_{C,t} - p_{C,0})$$

$$\Gamma_{256} = (0.7039 - 0.3834) - (0.5921 - 0.3892) = 0.3205 - 0.2029 = \mathbf{+0.1176}$$

### Secondary Estimand ($\Gamma_t^{R:D}$)
Defined as the contrast between Recovery ($R$) and Direct Decoding Benchmark ($D$):

$$\Gamma_t^{R:D} = (p_{R,t} - p_{R,0}) - (p_{D,t} - p_{D,0})$$

$$\Gamma_{256}^{R:D} = (0.7039 - 0.3834) - (0.6050 - 0.4010) = 0.3205 - 0.2040 = \mathbf{+0.1165}$$

---

## 2. Formal Hypothesis Specification

* **Two-Sided Primary Hypothesis Test**:
  * $H_0: \Gamma_{256} = 0$
  * $H_1: \Gamma_{256} \ne 0$
* **Inferential Test Results**:
  * Measured Contrast $\hat{\Gamma}_{256} = +0.1176$
  * Standard Error $SE = 0.0114$
  * Two-sided $z = 10.32, p < 0.0001$
  * $95\%$ Problem-Blocked Bootstrap CI: $[+0.0955, +0.1400]$

*Signed by Lead Statistician & Methodologist*
