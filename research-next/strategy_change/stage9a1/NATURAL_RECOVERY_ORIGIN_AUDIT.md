# NATURAL RECOVERY ORIGIN AUDIT REPORT

**Date**: August 16, 2026  

---

## 1. RECOVERY STATE ORIGIN CLASSIFICATION

Recovery states are prospectively partitioned into two explicit scientific classes:

1. **Class 1: Naturally Occurring Verifier-Identifiable Failure States ($N=20$)**:
   - Derived directly from verifier-checked student/model solution logs or human solution branches containing a verifiable error at step $t-1$ and an executable corrective step $t$.
   - **Role**: Drives the **Primary External-Validity Claim**.
2. **Class 2: Controlled Injected Failure States ($N=10$)**:
   - Created via programmatic synthetic error injection (e.g. off-by-one arithmetic, flipped relational operator) with verified valid repairs.
   - **Role**: Drives the **Controlled Mechanistic Validation Set**.

> **DIAGNOSTIC ISOLATION**: Primary claims are evaluated on Class 1. Class 2 serves as a positive control to verify synthetic error injection sensitivity.
