# Program 2 Existing Agent Claims Audit & Infrastructure Reuse

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Repositories Audited**: [`agentguard-final`](file:///Users/shamthakare/.gemini/antigravity/scratch/agentguard-final) & [`medirush`](file:///Users/shamthakare/.gemini/antigravity/scratch/medirush)

---

## 1. Frozen Pre-Existing Claims (Must NOT be Claimed as New)

| Source Repository | Pre-Existing Scientific Claim | Reusability Boundary |
|---|---|---|
| `agentguard-final` | Action lineage provenance DAGs and runtime policy interception eliminate unauthorized high-privilege tool execution across 80 `AgentGuardBench` scenarios. | **FROZEN**. Cannot claim provenance DAG interception of unauthorized tool execution as a new discovery. |
| `medirush` | Intent context filtering and runtime policy guardrails prevent unauthorized healthcare-commerce transactions in `MediRushBench`. | **FROZEN**. Cannot claim static policy-constrained healthcare agent guardrails as a new discovery. |
| `agentguard-final` | Interception gateways achieve zero false refusals on single-turn privilege escalation attacks. | **FROZEN**. Cannot claim single-turn policy interception accuracy as a new contribution. |

---

## 2. Permissible Infrastructure Reuse

The following components from `agentguard-final` and `medirush` may be reused as software infrastructure:
* ✅ Agent execution tracing and tool call logging harnesses.
* ✅ Machine-verifiable policy checkers (e.g., unauthorized tool invocation verifiers).
* ✅ Mock tool execution suites (search, database, file access, order processing, account management).
* ✅ Provenance DAG data structures for recording trajectory histories.

---

## 3. New Scientific Delta for Program 2

Program 2 moves strictly beyond static policy interception:
* **Target Phenomenon**: **Temporal Error Persistence ($d \ge 1$)**.
* **Primary Focus**: Measuring how transient external tool failures ($F_1 \dots F_4$) create persistent hidden-state belief errors that cause machine-verifiable safety violations *after the tool has recovered*.
