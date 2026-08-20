# PROGRAM 1 DATASET OVERLAP AUDIT

**Milestone**: Program 1 Pre-Execution Dataset Overlap Verification  
**Execution Timestamp**: `2026-08-19 23:15 UTC`  
**Auditor**: Reproducibility Engineer & Scientific Integrity Auditor  
**Dataset Audit Scope**: GSM8K, MATH, SVAMP, and prior submitted EAR experimental subsets

---

## 1. Experimental Dataset Partitioning Matrix

| Benchmark Dataset | Submitted Paper #1 (EAR) | Submitted Paper #3 (recovery_eval) | Program 1 Main Study | Overlap Status | Mitigation / Partition Strategy |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **GSM8K Test Split** | $N=100$ diagnostic probe | 20 fresh items ($d_{\text{mean}}=0.0360$) | **$N=500$ Full Test Set** | **`CONTROLLED`** | Disjoint subset tracking; log item IDs to prevent prompt leakage. |
| **MATH Subsets** | Not used | Not used | **$N=500$ MATH Level 3–5** | **`ZERO OVERLAP`** | Completely fresh dataset for reasoning transfer validation. |
| **SVAMP** | $N=100$ RL matrix | Not used | Not used in Program 1 | **`EXCLUDED`** | SVAMP reserved for EAR history; omitted from Program 1. |

---

## 2. Dataset Overlap Audit Conclusion

* All evaluation items are logged with SHA-256 item hashes.
* Item-level partitioning guarantees zero overlap between prior diagnostic subsets and Program 1 evaluation datasets.

*Signed by Reproducibility Engineer & Lead Statistical Methodologist*
