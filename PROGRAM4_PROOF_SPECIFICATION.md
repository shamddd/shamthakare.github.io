# Program 4 ZK Proof Specification & Cryptographic Semantics

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Status**: **PILOT CRYPTOGRAPHIC SPECIFICATION**

---

## 1. Cryptographic Proof Statement

The ZK proof $\pi$ proves that a committed execution graph $G = (V, E)$ satisfies policy predicate $P$ and reconciles with external receipt anchor $A$:

$$\text{Verify}(R, A, P, \text{Output}, PK_{\text{tool}}, \pi) = \text{True}$$

Where:
* **Public Inputs ($X_{\text{public}}$)**:
  - $R = \text{MerkleRoot}(G)$ (Merkle Graph Root Commitment)
  - $A = A_{\text{final}}$ (Append-Only Receipt Anchor Sequence Hash)
  - $P \in \{P_1, P_2, P_3\}$ (Frozen Policy Automaton Hash)
  - $PK_{\text{tool}}$ (Trusted Tool Public Keys)
  - $\text{Output}$ (Disclosed Terminal Action Payload)
* **Private Witness ($W_{\text{private}}$)**:
  - Node set $V$ and Causal Edge set $E$
  - Tool-signed receipts $r_k = (\text{node\_id}, \text{parent\_ids}, \text{seq}_k, \text{nonce}_k)$
  - Tool signatures $\sigma_k = \text{Sign}_{SK_{\text{tool}}}(r_k)$
  - Private prompt texts, tool parameters, user credentials, intermediate API payloads

---

## 2. Frozen Formal Policy Definitions

1. **$P_1$ (Required Ancestor)**:
   $$\text{Sensitive}(v) \implies \exists u \in V : \text{Authorized}(u) \land \text{Reachable}(u, v)$$
2. **$P_2$ (Dual Ancestor Join)**:
   $$\text{Sensitive}(v) \implies \exists u_1, u_2 \in V : \text{Approved}_1(u_1) \land \text{Approved}_2(u_2) \land \text{Reachable}(u_1, v) \land \text{Reachable}(u_2, v)$$
3. **$P_3$ (Forbidden Ancestor)**:
   $$\text{Sensitive}(v) \implies \neg \exists x \in V : \text{Revoked}(x) \land \text{Reachable}(x, v)$$
