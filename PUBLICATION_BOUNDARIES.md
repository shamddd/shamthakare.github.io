# Publication Boundaries & Intellectual Property Rights

**Author**: Sham Satish Thakare  
**Purpose**: Document clear, non-overlapping boundaries between prior submitted manuscripts and the 4 new Primary Research Programs to enforce research integrity and prevent self-plagiarism.

---

## 1. Frozen Prior Manuscripts (Do Not Mutate)

| Manuscript ID | Canonical Title | Submission Venue | Frozen Scientific Claims | Reusable Infrastructure |
|---|---|---|---|---|
| `WORK-01` | *Predicting Reinforcement-Learning Plasticity of Intermediate Language-Model Checkpoints: A Cross-Architecture Diagnostic Study* | JMLR (Under Review) | Probing vector $\mathbf{\phi}(C_k)$ predicts downstream GRPO reward gain $\beta_{\text{RL}}$ ($R^2=0.91$). | `adaptive-rl-forge` codebase infrastructure & Pythia probe extraction tools. |
| `WORK-02` | *EnclaveShield: Zero-Knowledge Memory Attestation and Side-Channel Mitigation for Hardware Enclaves* | Target: IEEE TDSC | ZK quote attestation and adaptive Path ORAM frequency rebalancing ($H(A)=0.82$, latency $1.47\text{ms}$). | ZK quote verifier and Path ORAM tree node rebalancer. |
| `WORK-03` | *AdaptiveReplica: Dynamic Quorum Adaptation and Failure-Aware Replica Selection in Distributed Consensus* | Target: IEEE TPDS | Dynamic vote-weight adaptation in Raft joint consensus ($88.8\%$ latency reduction, zero stale reads). | C++20 Raft joint-consensus engine and fault injector. |
| `WORK-04` | *TraceMind: Graph-Constrained Causal Reasoning for Root-Cause Localization in Microservice Systems* | Target: IEEE TCC | Topological causal walks over OpenTelemetry dependency graphs ($100\%$ Top-1 RCA accuracy, MRR=1.00). | OpenTelemetry trace parser & dependency graph engine. |
| `WORK-05` | *When Confidence Proxies Confound Reasoning Complexity: Pitfalls of Uncertainty-Weighted Credit Assignment in LM RL* | IEEE TAI (Under Review) | Token entropy length confounding ($r=+0.486$); 0.00% gain from online sample-level consensus credit weighting. | `ear_grpo_reasoning` repository (100% frozen). |

---

## 2. Mandatory Boundary Invariants for New Manuscripts

1. **New Paper for Program 1**:
   - **Must Not Claim**: That sample-level uncertainty weighting improves GRPO credit assignment (falsified in IEEE TAI submission).
   - **Must Claim**: Cross-family/cross-scale generalization of GRPO-induced overconfidence (*Bereket & Leskovec 2025*) and process-level Brier calibration rewards.

2. **New Paper for Program 2**:
   - **Must Not Claim**: Merely that policy interception guards agent tool execution (established in `agentguard-final` / `medirush`).
   - **Must Claim**: Multi-turn context-depth ($d=0 \to 20$) safety degradation and tool failure hidden-state belief persistence.

3. **New Paper for Program 3**:
   - **Must Not Claim**: Merely that dynamic quorums reduce Raft write latency under network failure (established in `quorumshift`).
   - **Must Claim**: Reliability envelopes and fallback bounds when learned online controllers encounter nonstationary distribution shift.

4. **New Paper for Program 4**:
   - **Must Not Claim**: Graph-constrained walks alone (established in `tracemind`) or Path ORAM alone (established in `enclaveshield`).
   - **Must Claim**: Zero-knowledge auditable provenance tracing for dynamic multi-step agent execution streams.
