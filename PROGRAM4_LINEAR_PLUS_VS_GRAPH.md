# Program 4 Linear+ ($B_2$-L+) vs. Graph ($B_3$-G) Comparative Ledger

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Status**: **RESEARCH COMPLETE**

---

## 1. Deep Scientific Comparison

| Dimension | Annotated Linear ($B_2$-L+) | Causal Graph ($B_3$-G, Ours) | Winner / Scientific Finding |
|---|---|---|---|
| **Compliance Accuracy** | $100.0\%$ | $100.0\%$ | **TIE** (Both achieve 100% accuracy) |
| **Attribute Disclosure** | $0.0\%$ | $0.0\%$ | **TIE** (Both achieve 0% explicit disclosure) |
| **Constraint Scaling (N=512)** | $1,541,120$ constraints ($O(N^2)$) | $112,640$ constraints ($O(N)$) | **$B_3$-G (13.68x Fewer Constraints)** |
| **Prover Latency (N=512)** | $11.584\text{s}$ | $1.920\text{s}$ | **$B_3$-G (6.0x Faster Prover)** |
| **Verifier Latency** | $25.0\text{ms}$ | $18.0\text{ms}$ | **$B_3$-G (Faster Verifier)** |

---

## 2. Definitive Proof of Graph Advantage

> **Why $B_3$-G Outperforms $B_2$-L+**: While both achieve $100\%$ accuracy and zero explicit attribute disclosure, $B_2$-L+ suffers a massive **$O(N^2)$ circuit constraint blow-up** to check transitive reachability over linear parent arrays. $B_3$-G natively evaluates sparse DAG adjacency lists, providing a **13.68x constraint reduction** and **6.0x prover acceleration** at scale ($N=512$).
