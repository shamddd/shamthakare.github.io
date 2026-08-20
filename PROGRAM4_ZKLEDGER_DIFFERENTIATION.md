# Program 4 vs. zkLedger Scientific Differentiation Ledger

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Purpose**: Formally delineate Program 4 from *zkLedger* (*zkLedger: Privacy-Preserving Auditing for Distributed Ledgers*, NSDI 2018).

---

## 1. Comparative Analysis Matrix

| Feature / Aspect | zkLedger (NSDI 2018) | Program 4 (Ours) |
|---|---|---|
| **Domain** | Permissioned distributed financial ledgers. | **Autonomous multi-step AI agent tool execution**. |
| **Data Representation** | Linear transaction tables (Deposits, transfers, balance columns). | **Non-linear causal provenance DAGs** ($G=(V,E)$). |
| **Audit Query Type** | Numerical aggregation queries (Sum of assets, token counts). | **Graph authorization-path reachability predicates ($u \prec_G v$)**. |
| **Proof Primitive** | Schnorr-type zero-knowledge proofs over commitments. | **Merkle tree inclusion ZK proofs over tool-signed receipts**. |

---

## 2. Definitive Scientific Distinction Statement

> **zkLedger** (NSDI 2018) provides privacy-preserving numerical auditing over linear financial transaction tables. In contrast, **Program 4** evaluates **graph structural reachability predicates ($u \prec_G v$) over multi-step AI agent provenance DAGs**, verifying that downstream tool actions derived their execution authority from valid parent nodes without revealing private prompt text or tool payloads.
