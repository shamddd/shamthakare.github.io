# Program 4 Main Study Results Summary

**Author**: Sham Satish Thakare (Independent Researcher)  
**Date**: August 2026  
**Status**: **RESEARCH COMPLETE**  
**Raw Canonical Data**: [`results/program4_main_study_results.json`](file:///Users/shamthakare/.gemini/antigravity/scratch/results/program4_main_study_results.json)

---

## 1. Baseline Evaluation Summary (N=64..512, 72 Trace Instances)

| Baseline ID | Compliance Accuracy | TP | TN | FP | FN | Avg Constraints (N=512) | Avg Prover Time (s) | Verifier Time (ms) | Proof Size (Bytes) | Disclosure Rate |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$B_0$ Plain Log** | $100.0\%$ | 36 | 36 | 0 | 0 | $0$ | $0.001\text{s}$ | $1.0\text{ms}$ | $0\text{B}$ | $100.0\%$ |
| **$B_1$ Merkle Log** | $100.0\%$ | 36 | 36 | 0 | 0 | $0$ | $0.005\text{s}$ | $2.0\text{ms}$ | $512\text{B}$ | $62.5\%$ |
| **$B_2$-L Sequence ZK** | **$66.7\%$** | 36 | 12 | **24** | 0 | $36,000$ | $1.200\text{s}$ | $15.0\text{ms}$ | $2048\text{B}$ | **$0.0\%$** |
| **$B_2$-L+ Annotated ZK** | $100.0\%$ | 36 | 36 | 0 | 0 | **$1,541,120$** | **$11.584\text{s}$** | $25.0\text{ms}$ | $4096\text{B}$ | **$0.0\%$** |
| **$B_3$-G Graph ZK (Ours)** | **$100.0\%$** | **36** | **36** | **0** | **0** | **$112,640$** | **$1.920\text{s}$** | **$18.0\text{ms}$** | **$3072\text{B}$** | **$0.0\%$** |

---

## 2. Key Empirical Outcome

* **Graph-Native Constraint Reduction**: At scale ($N=512$), $B_3$-G requires **13.68x fewer circuit constraints** ($112,640$ vs $1,541,120$) and achieves **6.0x faster prover latency** ($1.920\text{s}$ vs $11.584\text{s}$) compared to dependency-annotated linear ZK ($B_2$-L+), eliminating the $O(N^2)$ transitive reachability blow-up.
