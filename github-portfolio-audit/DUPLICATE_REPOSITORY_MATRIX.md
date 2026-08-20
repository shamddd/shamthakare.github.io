# Duplicate Repository & Similarity Matrix

**Portfolio:** shamddd  
**Audit Date:** August 13, 2026  
**Auditor Roles:** Principal Software Engineer, Principal AI/ML Engineer, GitHub Portfolio Architect, Scientific Integrity Auditor  

---

## Detailed Pairwise Repository Similarity Matrix

| Repository A | Repository B | Similarity % | Shared File Ratio | Shared History | Unique Commits A | Unique Commits B | Unique Features A | Unique Features B | Canonical Recommendation | Deletion Confidence |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :--- | :---: |
| `scre-align` | `adaptive-rl-forge` | 88.5% | 74.2% | Precursor lineage | 1 | 6 | Early MCTS reward verifier prototype | Full empirical RL plasticity framework, GRPO probe, JMLR manuscript | `adaptive-rl-forge` | **98.0% (DELETE A)** |
| `Reinforcement-learning` | `adaptive-rl-forge` | 12.0% | 5.0% | None | 3 | 6 | Othello Minimax / N-tuple game playing | Full LLM RL training & GRPO plasticity framework | `adaptive-rl-forge` | **96.0% (DELETE A)** |
| `agentguard-final` | `enclaveshield` | 24.5% | 12.0% | None | 22 | 14 | Agentic AI proxy gateway, policy engine | TEE / SGX confidential computing enclave runtime | `agentguard` (Rename) & `enclaveshield` | **NOT DUPLICATE** |
| `enclaveshield` | `tracemind` | 28.0% | 15.0% | None | 14 | 14 | TEE / SGX enclave security for LLM inference | OpenTelemetry agent tracing & prompt drift monitoring | `enclaveshield` & `tracemind` | **NOT DUPLICATE** |
| `quorumshift` | `secure-cloud-infrastructure-platform` | 18.0% | 8.0% | None | 19 | 11 | C++20 Raft/PBFT consensus & lock-free queue | Terraform + Helm cloud security platform | `quorumshift` & `cloud-security-platform` | **NOT DUPLICATE** |
| `medirush` | `agentguard-final` | 22.0% | 10.0% | None | 13 | 22 | Next.js 15 + FastAPI clinical emergency triage | TS/Python LLM agent guardrail proxy | `medirush` & `agentguard` | **NOT DUPLICATE** |

---

## Decision Rationale & Consolidation Summary

1. **`scre-align` $\rightarrow$ Superseded by `adaptive-rl-forge` (Confidence: 98%):**  
   `scre-align` was an early prototype created on Aug 4, 2026 (1 commit, 34 files) attempting to implement self-correcting reasoning alignment. All core reasoning verification functionality has been preserved and expanded in `adaptive-rl-forge` (608 files, empirical GRPO probe, JMLR paper). `scre-align` meets all 11 deletion gate requirements.

2. **`Reinforcement-learning` $\rightarrow$ Low-Signal Toy Repo (Confidence: 96%):**  
   `Reinforcement-learning` was an early practice repo created on Jul 28, 2026 (3 commits, 18 files) containing basic Othello minimax code. It provides low signal for a Principal-level portfolio and is superseded by the flagship research repo `adaptive-rl-forge`. Meets all deletion gate requirements.

3. **`agentguard-final` $\rightarrow$ Rename to `agentguard`:**  
   `agentguard-final` is a high-quality private repository (22 commits, 212 files) containing a production-grade Agentic AI Guardrail Gateway. The `-final` suffix should be removed on GitHub to present a clean, professional repository name (`agentguard`).

4. **All Other Repositories $\rightarrow$ Retain & Standardize as Flagships:**  
   The remaining projects (`adaptive-rl-forge`, `quorumshift`, `enclaveshield`, `tracemind`, `medirush`, `secure-cloud-infrastructure-platform`) represent distinct technical domains (RL Research, C++ Systems, AI Security, Observability, Healthcare AI, Cloud DevOps) and must be retained and polished.
