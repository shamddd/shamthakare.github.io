# Existing Research Registry

**Author**: Sham Satish Thakare (Independent Researcher)  
**Date**: August 2026  
**Purpose**: Canonical registry of pre-existing research projects, repositories, manuscripts, and scientific findings to enforce the self-plagiarism firewall and prevent accidental research duplication.

---

## 1. Project Inventory

### Project 1: EAR / GRPO Reasoning
* **Repository**: `ear_grpo_reasoning` ([github.com/shamddd/ear_grpo_reasoning](https://github.com/shamddd/ear_grpo_reasoning))
* **Current Status**: Submitted / Under Review at *IEEE Transactions on Artificial Intelligence (IEEE TAI)* (Aug 2026)
* **Research Question**: Does uncertainty-weighted credit assignment improve LLM reinforcement learning (GRPO) on multi-step reasoning tasks?
* **Scientific Claim**: Token predictive entropy is confounded with derivation length ($r = +0.486$). Sample-level self-consistency consensus weighting yields 0.00% performance gain over standard outcome-supervised GRPO.
* **Hypothesis**: Injecting trajectory uncertainty into GRPO policy gradients will prevent policy collapse. (Falsified).
* **Method**: 5-way controlled RL matrix (Standard-GRPO, Compute-Matched, Random-Weight, Permuted-Control, CA-GRPO).
* **Models**: `Qwen/Qwen2.5-0.5B-Instruct`
* **Datasets**: GSM8K, SVAMP
* **Experiments Performed**: Architectural dropout audit, diagnostic proxy benchmark ($N=100$), 5-way controlled RL matrix across 3 matched seeds.
* **Metrics**: AUROC, AUPRC, Partial Correlation ($r$), Pass@1 accuracy, Policy Entropy, KL divergence.
* **Main Findings**: Zero interior dropout in Qwen2.5 makes MC-dropout deterministic. Internal token entropy misidentifies correct complex derivation as uncertain in 42.1% of cases. Offline error predictability (AUROC = 0.812) does not translate to online RL policy gain.
* **Negative Findings**: CA-GRPO achieves 80.00% accuracy, exactly matching standard unweighted GRPO (0.00% delta).
* **Novelty Claim**: First empirical falsification of online sample-level uncertainty-weighted GRPO credit assignment.
* **Manuscript Title**: *When Confidence Proxies Confound Reasoning Complexity: Pitfalls of Uncertainty-Weighted Credit Assignment in Language Model Reinforcement Learning*
* **Submission Status**: Submitted to IEEE TAI (Aug 2026)
* **Code Contribution**: `src/rl/grpo_trainer.py`, `experiments/run_phase7_cagrpo_matrix.py`
* **Scientific Contribution**: Falsified sample-level uncertainty weighting in GRPO; identified derivation length confounding in token predictive entropy.
* **Unfinished Questions**: Does calibration degeneration occur across model families under GRPO without uncertainty weighting?
* **Potential Future Work**: Process-level Brier calibration rewards (not sample-level credit weighting).

---

### Project 2: AdaptiveRL-Forge / CARLS
* **Repository**: `adaptive-rl-forge` ([github.com/shamddd/adaptive-rl-forge](https://github.com/shamddd/adaptive-rl-forge))
* **Current Status**: Submitted / Under Review at *Journal of Machine Learning Research (JMLR)* (Aug 2026)
* **Research Question**: Can diagnostic probing vectors on intermediate checkpoint representation geometry predict downstream RL reward plasticity before full policy gradient rollouts?
* **Scientific Claim**: Representation geometry probes ($\mathbf{\phi}(C_k) = [\alpha_{\text{SVD}}, \bar{H}, \sigma_g^2]^T$) predict downstream GRPO reward gain $\beta_{\text{RL}}$ with $R^2 = 0.91$ ($p = 0.0004$).
* **Hypothesis**: Intermediate representation entropy and singular value spectrum decay rate correlate linearly with post-training RL adaptability.
* **Method**: Layer-wise SVD decay rate probe, representation entropy, gradient variance profiling.
* **Models**: Pythia series, Qwen2.5 series.
* **Datasets**: Pre-training corpus slices, reasoning benchmark evaluation datasets.
* **Experiments Performed**: Probing vector extraction across 15 intermediate checkpoints, downstream GRPO fine-tuning runs.
* **Metrics**: Probing $R^2$, Pearson $r$, Spearman $\rho$, Compute consumption ratio.
* **Main Findings**: Probing consumes $<2\%$ of compute required for full RL policy gradient rollouts while predicting RL outcome rank with high fidelity.
* **Negative Findings**: SVD decay alone without layer-wise entropy filtering loses predictive power on deeply fine-tuned models.
* **Novelty Claim**: First diagnostic probe vector for predicting RL reward plasticity on intermediate pre-trained checkpoints.
* **Manuscript Title**: *Predicting Reinforcement-Learning Plasticity of Intermediate Language-Model Checkpoints: A Cross-Architecture Diagnostic Study*
* **Submission Status**: Submitted to JMLR (Aug 2026)
* **Code Contribution**: `adaptive_rl_forge/carls/controller.py`, `adaptive_rl_forge/diagnostics/real_diagnostics.py`
* **Scientific Contribution**: Mathematical formulation of representation plasticity probing vector $\mathbf{\phi}(C_k)$.
* **Unfinished Questions**: Can plasticity probes predict model *calibration stability* ($\Delta\text{ECE}$) in addition to reward gain?

---

### Project 3: AdaptiveReplica / quorumshift
* **Repository**: `quorumshift` ([github.com/shamddd/quorumshift](https://github.com/shamddd/quorumshift))
* **Current Status**: Working Paper / Preprint (Targeting *IEEE TPDS*)
* **Research Question**: How can distributed consensus protocols dynamically adapt vote weights and quorum configurations under asymmetric node degradation without sacrificing linearizability?
* **Scientific Claim**: Failure-aware vote-weight adaptation over Raft joint-consensus transitions achieves 99.97% availability and reduces p99 write latency by 88.8% (13.50ms vs 120.48ms) with zero stale reads ($S_{\text{stale}}=0$).
* **Hypothesis**: Dynamic vote-weight decay based on RTT and packet loss maintains consensus invariants while routing writes around degraded nodes.
* **Method**: C++20 Raft joint-consensus engine with dynamic weight decay and asymmetric network fault injection.
* **Models**: N/A (Distributed Systems System Implementation)
* **Datasets**: Synthetic network degradation fault injection traces (16 failure scenarios).
* **Experiments Performed**: 16 asymmetric network degradation scenarios benchmarking static $R=5$ majority vs. AdaptiveReplica.
* **Metrics**: Write p99 latency (ms), Availability (%), Stale read count ($S_{\text{stale}}$), Joint-consensus transition duration.
* **Main Findings**: Dynamic quorum adaptation maintains zero stale reads under asymmetric network partition and node slow-down.
* **Negative Findings**: Static thresholds fail during rapid oscillating network loss; dynamic exponential smoothing is required.
* **Novelty Claim**: First failure-aware Raft joint-consensus vote weight adaptation mechanism with zero linearizability violation.
* **Manuscript Title**: *AdaptiveReplica: Dynamic Quorum Adaptation and Failure-Aware Replica Selection in Distributed Consensus*
* **Submission Status**: Preprint (Targeting IEEE TPDS)
* **Code Contribution**: C++20 Raft consensus engine in `quorumshift/`
* **Scientific Contribution**: Formulation of dynamic weight decay algorithm $w_i(t+1) = w_i(t) \exp(-\gamma \text{RTT}_i - \mu \text{Loss}_i)$.
* **Unfinished Questions**: How does quorum adaptation behave when failure prediction is driven by an online ML model subject to distribution shift?

---

### Project 4: MediRush & AgentGuard
* **Repositories**: `medirush` ([github.com/shamddd/medirush](https://github.com/shamddd/medirush)), `agentguard-final` ([github.com/shamddd/agentguard-final](https://github.com/shamddd/agentguard-final))
* **Current Status**: Working Paper / Manuscript in Prep (Targeting *Elsevier AI in Medicine* and *ACL/IEEE T-IFS*)
* **Research Question**: Can runtime action lineage provenance DAGs and policy interception prevent unauthorized tool execution and indirect prompt injection in autonomous LLM agents?
* **Scientific Claim**: Runtime action provenance DAGs enforce high-privilege authorization boundaries, achieving 0.0% unauthorized tool execution across benchmark attacks.
* **Hypothesis**: Intercepting tool payloads via action lineage verification eliminates high-privilege execution risk.
* **Method**: Provenance DAG construction, runtime policy interceptor gateway, human-in-the-loop escalation.
* **Models**: Tool-calling LLM agents (GPT-4o, Claude 3.5 Sonnet, Qwen2.5-Coder).
* **Datasets**: `AgentGuardBench`, `MediRushBench`.
* **Experiments Performed**: Benchmark evaluation on 80 tool-use scenarios and indirect injection suites.
* **Metrics**: Interception precision/recall, Latency overhead (ms), Refusal rate.
* **Main Findings**: Runtime policy interception successfully blocks 100% of indirect injection attacks attempting privilege escalation.
* **Negative Findings**: Static policy rules produce high false refusal rates on multi-turn ambiguous requests.
* **Novelty Claim**: Provenance lineage DAGs for LLM agent runtime tool policy interception.
* **Manuscript Title**: *AgentGuard: Action Lineage Provenance DAGs and Runtime Policy Interception for Autonomous AI Agents*
* **Submission Status**: Manuscript in Preparation
* **Code Contribution**: Interceptor gateway and provenance DAG module in `agentguard-final/` and `medirush/`
* **Scientific Contribution**: Lineage DAG verification for agent tool interception.
* **Unfinished Questions**: How does agent context depth ($d=0$ cold start vs $d=20$) degrade safety alignment over long-horizon multi-turn sessions?

---

### Project 5: TraceMind
* **Repository**: `tracemind` ([github.com/shamddd/tracemind](https://github.com/shamddd/tracemind))
* **Current Status**: Preprint (Targeting *IEEE TCC*)
* **Research Question**: Does constraining LLM causal reasoning with OpenTelemetry service dependency graphs improve root-cause localization accuracy in cascading microservice failures?
* **Scientific Claim**: Graph-constrained topological causal walks achieve 100.0% Top-1 RCA accuracy (MRR = 1.00) across 24 CausalOpsBench scenarios, compared to 0.0% Top-1 accuracy (MRR = 0.44) for unconstrained LLMs.
* **Hypothesis**: Topologically bounding causal random walks on microservice dependency graphs eliminates hallucinated fault paths.
* **Method**: Topological causal walks over OpenTelemetry Service Dependency Graphs (SDG).
* **Datasets**: `CausalOpsBench` (24 cascading fault scenarios).
* **Experiments Performed**: Comparison of unconstrained LLM reasoning vs. TraceMind graph-constrained walks.
* **Metrics**: Top-1 RCA Accuracy (%), Mean Reciprocal Rank (MRR), Telemetry processing time (ms).
* **Main Findings**: Bounding causal search to valid dependency DAG edges guarantees 1.00 MRR on microservice root cause analysis.
* **Novelty Claim**: First graph-constrained topological causal walk integration for microservice observability.
* **Manuscript Title**: *TraceMind: Graph-Constrained Causal Reasoning for Root-Cause Localization in Microservice Systems*
* **Submission Status**: Preprint (Targeting IEEE TCC)
* **Code Contribution**: Causal walk engine and OpenTelemetry parser in `tracemind/`
* **Scientific Contribution**: Topological walk algorithm $\text{Topological-Walk}(\mathcal{G}_{\text{dep}}, \mathbf{S}_{\text{telemetry}})$.

---

### Project 6: EnclaveShield
* **Repository**: `enclaveshield` ([github.com/shamddd/enclaveshield](https://github.com/shamddd/enclaveshield))
* **Current Status**: Preprint (Targeting *IEEE TDSC*)
* **Research Question**: Can access-frequency-weighted adaptive Path ORAM rebalancing mitigate memory side-channel leakage in hardware enclaves (SGX/TDX) without incurring severe latency penalties?
* **Scientific Claim**: Adaptive Path ORAM tree rebalancing achieves access pattern entropy $H(A) = 0.82 \pm 0.02$ while bounding page access latency to $1.47\text{ms}$ ($2.45\times$ host baseline vs $15.00\text{ms}$ static Path ORAM).
* **Hypothesis**: Dynamic rebalancing based on page access frequency obfuscates access patterns while minimizing tree traversal depth.
* **Method**: ZK quote attestation membership proofs, frequency-weighted tree rebalancing in Path ORAM.
* **Datasets**: `EnclaveBench` 20 workload trace dataset.
* **Experiments Performed**: Latency and entropy benchmarking across 20 memory access trace patterns.
* **Metrics**: Access Pattern Entropy $H(A)$, Page Access Latency (ms), Overhead ratio.
* **Main Findings**: Frequency-weighted rebalancing preserves side-channel obfuscation while reducing static Path ORAM latency by $10.2\times$.
* **Novelty Claim**: Adaptive Path ORAM tree rebalancing paired with ZK remote attestation for hardware enclaves.
* **Manuscript Title**: *EnclaveShield: Zero-Knowledge Memory Attestation and Side-Channel Mitigation for Hardware Enclaves*
* **Submission Status**: Preprint (Targeting IEEE TDSC)
* **Code Contribution**: Path ORAM tree rebalancing engine and ZK quote verifier in `enclaveshield/`
