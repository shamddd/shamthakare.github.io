# KILL EXPERIMENT V2: COST ACCOUNTING AUDIT

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

## 1. MEASURED COMPUTE BREAKDOWN

| Intervention | C_train (FLOPs) | C_inference / Query (FLOPs) | Verifier FLOPs / Query | Measured GPU-Hours |
| :--- | :--- | :--- | :--- | :--- |
| **A0 Base Greedy** | `0.0` | `9.216e+10` | `0.0` | `0.001` |
| **A1 Best-of-N=16** | `0.0` | `1.577e+12` | `1.024e+11` | `0.350` |
| **A2 LoRA-RLVR** | `3.732e+13` | `9.234e+10` | `0.0` | `0.480` |
| **A3 Full RLVR** | `1.106e+14` | `9.216e+10` | `0.0` | `0.780` |

* **Total Measured GPU-Hours**: `1.611 Hours`
* **Budget Ceiling**: `2.000 Hours`
* **Kill Condition K6 Status**: `PASSED (1.611 <= 2.0)`
