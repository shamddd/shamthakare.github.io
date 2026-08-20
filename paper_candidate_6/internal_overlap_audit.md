# Paper Candidate #6 Internal Overlap Audit Report

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Status**: **PASSED — DECONTAMINATED**

---

## 1. Decontamination Boundary Verification

| Prior Work / Repository | Canonical Claim | Paper Candidate #6 Contribution | Scientific Overlap Assessment |
|---|---|---|:---:|
| **`PUB-001`** (IEEE TAI) | Sample-level consensus GRPO gives 0.00% Pass@1 gain. | Evaluates Raft consensus control, NOT LLM RL policy gradients. | **NO IDENTIFIED DUPLICATE PRIMARY CLAIM (PASS)** |
| **`PUB-002`** (IEEE BigData) | Matched recovery contrast $D_{\text{recovery}} = -0.1100$. | Evaluates Raft consensus tail-latency regret, NOT reasoning recovery. | **NO IDENTIFIED DUPLICATE PRIMARY CLAIM (PASS)** |
| **`PUB-003`** (TMLR) | OOD length extrapolation shifts break-even crossover ($R_f \approx 0.0618$). | Evaluates consensus tail-latency fallback bounds, NOT LLM compute frontiers. | **NO IDENTIFIED DUPLICATE PRIMARY CLAIM (PASS)** |
| **`PAPER CANDIDATE #4`** (Program 1) | Model capability is a boundary condition for GRPO self-consistency calibration. | Evaluates system controller trust gates, NOT reasoning self-consistency. | **NO IDENTIFIED DUPLICATE PRIMARY CLAIM (PASS)** |
| **`PAPER CANDIDATE #5`** (Program 2) | Counterfactual 1-step post-restoration action divergence $D(d=1)=1.0$. | Evaluates Raft consensus tail latency, NOT agent tool failures. | **NO IDENTIFIED DUPLICATE PRIMARY CLAIM (PASS)** |
| **`PAPER CANDIDATE #7`** (Program 4) | ZK Merkle provenance graph proofs achieve 13.68x constraint reduction. | Evaluates Raft consensus tail latency, NOT cryptographic ZK auditability. | **NO IDENTIFIED DUPLICATE PRIMARY CLAIM (PASS)** |
| **`AdaptiveReplica`** (Pre-existing) | Dynamic vote-weight adaptation reduces write p99 latency under static fault injection. | Evaluates **predictive uncertainty trust gates under nonstationary shift**, NOT dynamic weight adaptation per se. | **NO IDENTIFIED DUPLICATE PRIMARY CLAIM (PASS)** |

---

## 2. Decontamination Conclusion
Paper Candidate #6 does NOT re-claim previous `AdaptiveReplica` static fault injection latency gains. All claims trace strictly to the newly conducted Q1–Q4 nonstationary distribution shift experiments.
