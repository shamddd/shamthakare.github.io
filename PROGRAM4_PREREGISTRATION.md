# Program 4 Experimental Preregistration Document

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Status**: **PRE-PILOT PREREGISTERED SPECIFICATION**

---

## 1. Formal Hypotheses

* **Null Hypothesis ($H_0$)**: Graph-aware ZK provenance proofs provide no policy-distinguishability advantage or disclosure reduction over linear ZK trace proofs ($B_2/B_3$), and cannot faithfully distinguish $G_{\text{valid}}$ from $G_{\text{invalid}}$ without disclosing private trace attributes.
* **Alternative Hypothesis ($H_1$)**: Graph-aware ZK provenance proofs ($B_4$) achieve $100\%$ policy distinguishability ($TP=100\%, FP=0\%$) on branching causal workflows where linear baselines ($B_2$) fail, while eliminating explicit private attribute disclosure ($0.0\%$ sensitive fields revealed) and verifying tool-signed commitment completeness.

---

## 2. Experimental Baselines

1. **$B_0$ (Plain Full Audit Log)**: Full visibility (100% attribute disclosure).
2. **$B_1$ (Merkle Authenticated Log)**: Merkle root integrity with selective leaf disclosure.
3. **$B_2$ (ZK Linear Trace Proof)**: ZK proof enforcing sequential linear execution.
4. **$B_3$ (zkVM Authorization Policy Baseline - Prezta-style)**: Single-turn request authorization check.
5. **$B_4$ (ZK Provenance Graph Proof - Ours)**: ZK proof over Merkle provenance graph verifying causal DAG reachability ($u_1, u_2 \prec_G v$).

---

## 3. Endpoints & Metrics

* **Primary Security Endpoint**: Policy Distinguishability Advantage ($TP, TN, FP, FN$) on $G_{\text{valid}}$ vs $G_{\text{invalid}}$ pairs.
* **Secondary Endpoints**:
  - Explicit Private Attribute Disclosure Rate (%)
  - Proof Generation Latency (seconds)
  - Verification Latency (milliseconds)
  - Proof Size (bytes)
