# Program 4 Security Attack Evaluation Report (A1–A8)

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Status**: **RESEARCH COMPLETE**

---

## 1. Security Attack Evaluation Matrix

| Attack ID | Attack Description | Circuit / Protocol Verification Mechanism | Security Result |
|---|---|---|:---:|
| **$A_1$** | Delete committed node | Witness Merkle Root $R$ mismatch | **REJECTED** |
| **$A_2$** | Delete signed receipt | External Anchor Chain $A_{\text{final}}$ mismatch | **REJECTED** |
| **$A_3$** | Modify parent IDs | HMAC/Ed25519 signature failure & Merkle root failure | **REJECTED** |
| **$A_4$** | Reorder linear storage | Causal reachability ($u \prec_G v$) remains invariant | **ACCEPTED (Invariant)** |
| **$A_5$** | Forge receipt | Signature verification failure under $PK_{\text{tool}}$ | **REJECTED** |
| **$A_6$** | Omit before anchor | Outside protocol boundary (Documented limitation) | **OUTSIDE GUARANTEE** |
| **$A_7$** | Cross-trace receipt replay | Session nonce mismatch ($session\_id$) | **REJECTED** |
| **$A_8$** | Branch splicing | Parent hash commitment & session nonce mismatch | **REJECTED** |

---

## 2. Equivocation & Completeness Boundaries

* **Tool-Signed Receipts**: Protects against tampering, node modification, and cross-trace replay ($A_1, A_3, A_5, A_7, A_8$).
* **External Anchor Chain ($A_{\text{final}}$)**: Protects against untrusted logger omitting signed receipts ($A_2$).
* **Equivocation Analysis**: If a malicious tool emits two conflicting child receipts for the same parent, the external anchor chain exposes duplicate sequence IDs, enabling verifier detection.
