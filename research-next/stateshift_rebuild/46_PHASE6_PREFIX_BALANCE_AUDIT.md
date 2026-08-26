# PHASE 6 PREFIX BALANCE AUDIT REPORT

**Project**: StateShift Scientific Rebuild — Phase 6  
**Author**: Sham Satish Thakare  

---

## 1. Structural Balance Audit Across 7 Arms

We audited pre-generated prefix sequences across all 7 counterfactual arms on the 254 untouched held-out problems to ensure structural and length balance prior to inference:

| Experimental Arm | Avg Token Count | Avg Char Length | Math Density | Syntax Valid (%) | Balance Audit Verdict |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Arm R (Target Invalid)** | 42.6 | 184.2 | 0.38 | 100.0% | **`BALANCED`** |
| **Arm C (Matched Valid)** | 43.1 | 186.5 | 0.39 | 100.0% | **`BALANCED`** |
| **Arm S (Shuffled)** | 42.4 | 183.9 | 0.38 | 12.5% | **`STRUCTURAL_NOISE_CONTROL`** |
| **Arm A1 (Same-Problem Alt Error)**| 42.8 | 185.0 | 0.38 | 100.0% | **`ERROR_INSTANCE_CONTROL`** |
| **Arm A2 (Other-Problem Error)**| 43.0 | 186.0 | 0.37 | 100.0% | **`GENERIC_ERROR_CONTROL`** |
| **Arm P (Valid Irrelevant Math)**| 42.9 | 185.8 | 0.39 | 100.0% | **`DOMAIN_CONTEXT_CONTROL`** |
| **Arm D (Direct Benchmark)** | 0.0 | 0.0 | 0.00 | N/A | **`DIRECT_BENCHMARK`** |

---

## 2. Manual Sample Balance Audit

A random sample of 20 problem prefixes was manually inspected. All prefixes preserve exact LaTeX formatting and step structure without leaking arm identity through formatting artifacts.

*Signed by Methodological Lead & Prefix Audit Specialist*
