# Program 4 Cryptographic Validation Document

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Status**: **RESEARCH COMPLETE**

---

## 1. Cryptographic Primitives & Parameters

* **Hash Primitive**: SHA-256 (256-bit digest).
* **Signature Primitive**: HMAC-SHA256 / Ed25519 (256-bit key length).
* **Merkle Tree Commitment**: Binary Merkle tree over node payload hashes.
* **Anchor Chain**: Append-only recursive hash chain $A_k = H(A_{k-1} \parallel H(r_k) \parallel \sigma_k)$.
* **Circuit Model**: Rank-1 Constraint System (R1CS) / PLONK constraint model simulating RISC Zero / Circom constraint evaluation.

---

## 2. Public vs. Private Witness Separation

* **Public Inputs**: Merkle root $R$, receipt anchor $A$, policy hash $P$, tool public keys $PK_{\text{tool}}$, terminal action.
* **Private Witness**: Trace graph $G=(V,E)$, prompt texts, tool parameters, user credentials, intermediate API payloads, signature nonces.
