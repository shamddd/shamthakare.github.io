# Program 4 Minimum Viable Pilot Design

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Status**: **PRE-PILOT SPECIFICATION**

---

## 1. Pilot Objectives & Test Regimes

1. **Policy Distinguishability Advantage**: Test whether ZK Provenance Graph Proof ($B_4$) correctly accepts $G_{\text{valid}}$ ($TP=100\%$) and rejects $G_{\text{invalid}}$ ($TN=100\%$) on branching/join causal workflows where linear baselines ($B_2$) fail.
2. **Commitment Completeness Verification**: Verify $100\%$ rejection rate when an untrusted logger attempts to delete or forge a tool execution node without a valid tool-signed receipt signature $\sigma_k$.
3. **Disclosure Reduction**: Quantify explicit sensitive attribute disclosure ($0.0\%$ under $B_4$ vs $100\%$ under $B_0$).
4. **Performance Scaling**: Measure proof generation latency, verification latency, and proof size across trace sizes ($N \in \{8, 16, 32\}$ nodes).

---

## 2. Benchmark Workflows

* **Workflows**: $N = 30$ multi-step agent traces:
  - 10 Linear Workflows
  - 10 Branching Workflows
  - 10 Multi-Parent Join Workflows
* **Adversarial Variants**:
  - Missing approval branch
  - Reparented node (pointing auth to failed attempt)
  - Deleted dependency step
  - Forged edge
  - Unauthorized shortcut
