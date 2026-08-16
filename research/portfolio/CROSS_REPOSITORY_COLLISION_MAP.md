# Cross-Repository Collision Map

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Scope**: Portfolio-wide duplication audit across 10 repositories.

---

## Pairwise Scientific Overlap Matrix

| Pairwise Comparison | Research Question | Algorithm / Architecture | Dataset / Benchmark | Overlap Level | Scientific Disposition |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **`adaptive-rl-forge` vs. `scre-align`** | Checkpoint plasticity prediction vs. MCTS PRM reasoning alignment | Diagnostic probes vs. MCTS tree search + PRM verifiers | Pretraining checkpoints vs. Math PRM benchmarks | **MODERATE** | **Distinct**. `adaptive-rl-forge` studies pre-training RL plasticity dynamics, while `scre-align` studies inference-time tree search alignment. Keep distinct. |
| **`adaptive-rl-forge` vs. `Reinforcement-learning`** | Plasticity prediction vs. unorganized basic RL scripts | Diagnostic probing vs. standard Q-learning/PPO demos | Custom synthetic/PyTorch vs. toy OpenAI Gym | **HIGH** | **Archival**. `Reinforcement-learning` is subsumed by `adaptive-rl-forge`. Recommend archiving `Reinforcement-learning`. |
| **`enclaveshield` vs. `secure-cloud-infrastructure-platform`** | Hardware TEE ZK attestation/ORAM vs. Container spec control plane | ZK quote verification + ORAM tree vs. FastAPI GitOps admission controller | EnclaveBench vs. K8s manifest compliance | **LOW** | **Synergistic**. `secure-cloud-infrastructure-platform` provides control plane governance; `enclaveshield` provides enclave runtime integrity. |
| **`enclaveshield` vs. `agentguard-final`** | Hardware side-channel ORAM vs. LLM agent action provenance DAG | ZK quote verifier vs. Runtime policy interceptor | Page-fault memory traces vs. Multi-step agent tool logs | **MODERATE** | **Distinct**. Hardware enclave security vs. AI agent runtime policy safety. Keep separated. |
| **`tracemind` vs. `quorumshift`** | Microservice graph causal RCA vs. Adaptive consensus quorum shift | Causal graph traversal + OTEL fusion vs. Latency-aware Raft quorum | CausalOpsBench vs. Fault-injection storage workloads | **NONE** | **Completely Independent**. Observability/AIOps vs. Storage consensus. |
| **`medirush` vs. All Repos** | Emergency medical triage / AI clinical decision support | Clinical transformer / risk scoring | Medical clinical datasets | **NONE** | **Preserved**. Preserved publication prep (Target: *Elsevier Artificial Intelligence in Medicine*). Do NOT modify. |

---

## Archival & Migration Plan

### 1. `Reinforcement-learning` (Archival Recommended)
* **Evidence**: Contains raw unorganized script implementations of standard RL algorithms (DQN, PPO) without a unified research hypothesis.
* **Unique Value**: Legacy exploratory code.
* **Action**: Retain read-only archive in GitHub. Do not submit standalone paper.

### 2. `github-portfolio-audit` (Auxiliary Utility)
* **Evidence**: Utility folder containing administrative metadata.
* **Action**: Retain as internal tooling directory.

### 3. `scre-align` (Future Synergy)
* **Evidence**: Strong implementation of MCTS step-backtracking with Process Reward Models (`Qwen2.5-Math-PRM-7B`).
* **Action**: Maintain as separate specialized project on reasoning alignment. Can serve as a downstream evaluation task for models evaluated by `adaptive-rl-forge`.

---

## Detailed Project-by-Project Comparison Table

```
========================================================================================================================
PROJECT                      QUESTION                           METHOD                       OVERLAP    ACTION
========================================================================================================================
adaptive-rl-forge            Checkpoints RL plasticity          Representation entropy probe NONE (JMLR) Preserve JMLR manuscript;
                                                                & singular value spectrum               isolate future extensions
enclaveshield                ZK remote attestation & ORAM       Adaptive Path ORAM tree +    NONE       Audit prior art, implement
                             side-channel mitigation             ZK quote membership proof               real ZK quote benchmark
quorumshift                  Failure-aware dynamic quorum       AdaptiveReplica consensus    NONE       Benchmark against Raft under
                             adaptation                         policy & partition handling             fault injection (p95/p99)
secure-cloud-infra-platform Policy verification & attack path  Static AST invariant engine  NONE       Transform engineering into
                             reduction on container manifests   over K8s specs                          formal policy verification
tracemind                    Graph-constrained causal RCA       OTEL trace/log/metric fusion NONE       Benchmark against baselines
                             over microservice graphs           over Service Dep Graph                  on CausalOpsBench
========================================================================================================================
```
