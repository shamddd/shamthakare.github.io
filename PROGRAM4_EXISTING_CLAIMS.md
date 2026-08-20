# Program 4 Existing System Claims Audit & Reusability Boundary

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Repositories Audited**: [`tracemind`](file:///Users/shamthakare/.gemini/antigravity/scratch/tracemind), [`enclaveshield`](file:///Users/shamthakare/.gemini/antigravity/scratch/enclaveshield), [`agentguard-final`](file:///Users/shamthakare/.gemini/antigravity/scratch/agentguard-final), [`medirush`](file:///Users/shamthakare/.gemini/antigravity/scratch/medirush)

---

## 1. Frozen Pre-Existing Claims (Must NOT be Claimed as New)

| System / Repository | Pre-Existing Scientific Claim | Reusability Boundary |
|---|---|---|
| **`TraceMind`** | Graph-constrained LLM inference over OpenTelemetry Service Dependency Graphs (SDGs) achieves $100\%$ Top-1 RCA localization accuracy. | **FROZEN**. Cannot claim OpenTelemetry SDG graph-constrained root cause localization as new. |
| **`EnclaveShield`** | Hardware enclave SGX attestation, ZK quote verification, and Path ORAM node rebalancing for confidential microservice trace processing. | **FROZEN**. Cannot claim hardware enclave SGX remote attestation or Path ORAM rebalancing as new. |
| **`AgentGuard`** | Provenance DAGs and runtime policy interception gateways prevent unauthorized high-privilege tool execution. | **FROZEN**. Cannot claim provenance DAG interception of unauthorized tool execution as new. |
| **`MediRush`** | Healthcare intent context guardrails prevent unauthorized medical transactions. | **FROZEN**. Cannot claim domain-specific healthcare intent guardrails as new. |

---

## 2. Hard Anti-Combination Rule

> **Strict Rule**: Program 4 MUST NOT merely claim novelty by combining pre-existing components (e.g. *"TraceMind DAG + EnclaveShield + Zero-Knowledge + LLM Agent"*). A valid research contribution requires an unresolved systems/security problem that cannot be solved by simply linking existing modules.

---

## 3. New Scientific Delta for Program 4

Program 4 isolates a genuinely unaddressed systems/security problem:
* **Target Problem**: **Privacy-Preserving Zero-Knowledge Verification of Agent Policy Compliance**.
* **Primary Focus**: Proving that a multi-step tool-using agent execution complied with machine-verifiable authorization policies (e.g. authorization-path compliance) **WITHOUT disclosing private prompt texts, tool parameters, API payloads, or user credentials to external auditors**.
