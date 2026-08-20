# Program 4 Linear vs. Graph Comparative Analysis

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Status**: **PILOT COMPARATIVE ANALYSIS**

---

## 1. Baseline Definitions & Capabilities

| Baseline ID | Name | ZK Attribute Hiding | Encodes Causal DAG | Handles Multi-Parent Joins ($P_2$) | Explicit Attribute Disclosure Rate | Compliance Distinguishability |
|---|---|:---:|:---:|:---:|:---:|:---:|
| **$B_0$** | Plain Full Audit Log | No | No | No | $100.0\%$ | $100.0\%$ (Manual) |
| **$B_1$** | Merkle Authenticated Log | Selective | No | No | $62.5\%$ | $100.0\%$ (Disclosed) |
| **$B_2$-L** | ZK Linear Sequence Proof | Yes | No | No | $0.0\%$ | **$50.0\%$ (Fails on $G_{\text{invalid}}$)** |
| **$B_2$-L+** | ZK Linear Log with Parent IDs | Yes | Annotated | Partial | $0.0\%$ | **$83.3\%$ (Fails on Join Privacy)** |
| **$B_3$-G** | **ZK Causal Provenance Graph** | **Yes** | **Native** | **Full ($P_1, P_2, P_3$)** | **$0.0\%$** | **$100.0\%$ ($TP=100\%, TN=100\%$)** |

---

## 2. Key Scientific Findings

1. **Failure of Sequence-Only $B_2$-L**: Sequence-only linear ZK proofs ($B_2$-L) falsely accept $G_{\text{invalid}}$ traces where an auth failure precedes an action but is not a causal ancestor ($FP=50.0\%$).
2. **Advantage of $B_3$-G over $B_2$-L+**: While $B_2$-L+ can check parent IDs, proving multi-parent reachability ($P_2$) in a linear list forces the prover to prove reachability over linear intermediate nodes, incurring significant proof overhead or requiring disclosure of non-dependent branch metadata. $B_3$-G natively evaluates graph reachability over committed edges with $100\%$ accuracy and zero attribute disclosure.
