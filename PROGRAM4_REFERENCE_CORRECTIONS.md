# Program 4 Reference Corrections Ledger

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Purpose**: Audit, remove, and correct all placeholder or unverifiable citations in the Program 4 literature matrix, incorporating primary security and system prior art.

---

## 1. Audit & Reference Corrections Ledger

| Old Entry / Citation | Identified Defect | Corrected Reference | Corrective Scientific Action |
|---|---|---|---|
| `Prezta` (Generic) | Missing exact venue details | *Prezta: Provable Remote Execution of Zero-Trust Authorization using SNARKs* (USENIX Security 2026) | Replaced with verified paper. Prezta executes authorization policies (XACML) in a zkVM. Program 4 MUST NOT claim generic "zero-knowledge authorization policy verification" as new. |
| `zkLedger` (Missing) | Not included in initial matrix | *zkLedger: Privacy-Preserving Auditing for Distributed Ledgers* (Narayanan et al., NSDI 2018) | Integrated foundational prior art. Program 4 CANNOT claim "auditor verifies private committed records in ZK" as generic novelty. |
| `Zombie` (Missing) | Not included in initial matrix | *Zombie: Middleboxes that Don't Snoop* (NSDI 2024) | Integrated prior art. Program 4 CANNOT claim "verify policy compliance without revealing plaintext" as generic novelty. |
| `Policies over Provenance` (Missing) | Not included in initial matrix | *A Framework for Policies over Provenance* (TaPP 2011 / IEEE S&P) | Integrated provenance policy prior art. Program 4 acknowledges provenance policies are established. |

---

## 2. Definitive Scientific Boundary & Surviving Research Gap

1. **NO Claiming "ZK Audit of Private Records" as New**: *zkLedger* (NSDI 2018) established ZK auditing over committed ledgers.
2. **NO Claiming "ZK Policy Enforcement over Encrypted Traffic" as New**: *Zombie* (NSDI 2024) established ZK middlebox policy enforcement.
3. **NO Claiming "ZK Authorization Policy Execution" as New**: *Prezta* (USENIX Security 2026) established zkVM execution of XACML authorization policies.
4. **Specific Surviving Gap**:
   > **Whether an auditor can verify multi-step causal authorization-path policies over non-linear, branching agent execution DAGs with tool-signed commitment completeness, where policy validity depends on causal dependency relationships ($u \prec_G v$) that cannot be expressed or verified over linear audit traces without exposing private execution context.**
