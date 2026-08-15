# UNIT-COUNT ACCOUNTING CORRECTION REPORT

**Date**: August 16, 2026  

---

## 1. EXPLICIT UNIT-COUNT ACCOUNTING AUDIT

* **Untouched Problems**: Exactly 10 untouched GSM8K problems ($N_{\text{prob}}=10$).
* **State Space**: 20 total states = **10 matched state pairs** (1 recovery state $S_R$ and 1 matched control state $S_C$ per problem).
* **Class Partition Correction**:
  - **Class 1 (Source-Trajectory-Derived Verifier-Identifiable Recovery States)**: **14 states = 7 matched state pairs** from 7 problems.
  - **Class 2 (Controlled Injected Failure States)**: **6 states = 3 matched state pairs** from 3 problems.

> **ACCOUNTING RULE**: State counts are strictly reported as 10 matched state pairs (7 Class 1 pairs, 3 Class 2 pairs). Over-counting states as separate independent pairs is strictly prohibited.
