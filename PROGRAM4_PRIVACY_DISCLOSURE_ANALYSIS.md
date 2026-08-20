# Program 4 Selective Privacy & Metadata Disclosure Analysis

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Status**: **PILOT PRIVACY ANALYSIS**

---

## 1. Explicit Sensitive Attribute Disclosure Rates

| Baseline | Disclosed Attributes (Prompt, Payload, Credential) | Disclosure Rate (%) | Unavoidable Metadata Revealed |
|---|---|:---:|---|
| **$B_0$ Plain Log** | All prompt texts, tool parameters, API tokens | **$100.0\%$** | Complete trace history |
| **$B_1$ Merkle Log** | Disclosed leaves needed for Merkle verification | **$62.5\%$** | Partial trace leaves & tree depth |
| **$B_2$-L Sequence ZK** | None (All witness fields hidden) | **$0.0\%$** | Trace sequence length $N$, policy ID |
| **$B_2$-L+ Annotated ZK** | None (All witness fields hidden) | **$0.0\%$** | Sequence length $N$, parent ID array |
| **$B_3$-G Graph ZK (Ours)** | **None (All witness fields hidden)** | **$0.0\%$** | **Node count $N$, Merkle root $R$, policy ID** |

---

## 2. Explicit Non-Claims & Metadata Leakage

* **Explicit Sensitive Attributes ($0.0\%$ Revealed in $B_3$-G)**: Prompt texts, user identities, credentials, tool arguments, intermediate API payloads.
* **Unavoidable Public Metadata**: Verifier observes trace node count $N$, Merkle root commitment $R$, external receipt anchor $A$, policy automaton hash $P$, and proof generation timing.
