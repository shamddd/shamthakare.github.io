# Program 4 vs. Prezta Scientific Differentiation Ledger

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Purpose**: Formally delineate Program 4 from *Prezta* (*Prezta: Provable Remote Execution of Zero-Trust Authorization*, USENIX Security 2026).

---

## 1. Comparative Analysis Matrix

| Feature / Aspect | Prezta (USENIX Security 2026) | Program 4 (Ours) |
|---|---|---|
| **Execution Model** | Single-request authorization policy execution in a zkVM. | **Multi-step agent tool execution over Merkle provenance DAGs**. |
| **Policy Scope** | XACML & JWT static access control policies. | **Multi-parent causal DAG authorization paths ($u_1, u_2 \prec_G v$)**. |
| **Trace Structure** | Single request/response payload. | **Non-linear causal DAGs** (Branching, multi-agent delegation, joins). |
| **Completeness Model** | Relies on client request parameters. | **Tool-signed cryptographic receipt chaining ($\sigma_k$)**. |
| **Privacy Boundary** | Hides user identity attributes in JWT. | **Selectively hides prompt text, tool arguments, and API payloads while proving path compliance**. |

---

## 2. Definitive Scientific Distinction Statement

> **Prezta** (USENIX Security 2026) evaluates zkVM remote execution for single-request XACML access control policies. In contrast, **Program 4** evaluates **multi-step causal DAG authorization-path compliance over tool-signed Merkle provenance graphs**. Program 4 addresses causal dependencies across asynchronous tool workflows ($u_1, u_2 \prec_G v$) that single-request zkVM policies cannot express or verify without disclosing non-dependent execution subgraphs.
