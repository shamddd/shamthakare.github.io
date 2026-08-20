# Program 4 Final External Novelty Audit Report

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Status**: **RESEARCH COMPLETE**

---

## 1. External Literature Decontamination Matrix

| Prior Work / Venue | Canonical Claim | Program 4 Research Delta | Overlap Severity | Decontamination Verdict |
|---|---|---|:---:|---|
| **Prezta** (USENIX Security 2026) | Single-request XACML authorization policy execution in zkVM. | Evaluates multi-step causal DAG authorization paths ($u_1, u_2 \prec_G v$) over tool-signed Merkle provenance graphs. | **2 (Shared Area)** | **PASS**. |
| **Zombie** (NSDI 2024) | Packet-level regex filtering over encrypted TLS streams at middlebox gateways. | Evaluates multi-step causal DAG authorization-path compliance over committed agent traces for external auditors. | **2 (Shared Area)** | **PASS**. |
| **zkLedger** (NSDI 2018) | Numerical audit queries over linear financial transaction tables. | Evaluates graph structural reachability predicates ($u \prec_G v$) over AI agent execution provenance DAGs. | **2 (Shared Area)** | **PASS**. |
| **zkLLM** (ACM CCS 2024) | Verifies neural network weight inference correctness in ZK. | Evaluates multi-step tool policy compliance over provenance graphs, NOT model weight matrix multiplications. | **1 (Low Overlap)** | **PASS**. |
| **Policies over Provenance** (TaPP 2011) | Access control policy framework over provenance graphs. | Integrates cryptographic ZK proofs, selective attribute hiding, and tool-signed receipt completeness. | **2 (Shared Area)** | **PASS**. |

---

## 2. External Novelty Confidence: **90%**
