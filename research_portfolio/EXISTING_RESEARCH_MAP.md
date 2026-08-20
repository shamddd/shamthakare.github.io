# Existing Public Research Portfolio Map & Overlap Audit

**Candidate / Author**: Sham Thakare (Sham Satish Thakare)  
**Profile**: [https://github.com/shamddd](https://github.com/shamddd)  
**Date**: August 2026  
**Auditor Role**: Senior ML Research Scientist & Scientific Methodologist  

---

## 1. Executive Summary & Deduplication Boundary

This document establishes the canonical baseline of Sham Thakare's existing public research portfolio. Every existing project is mapped by problem, contribution, methods, datasets, models, results, publication status, strengths, weaknesses, and research area. 

> **Strict Non-Duplication Constraint**: All future project proposals generated in this master research program must be **substantively independent** and fundamentally distinct from the existing works below. Any project that merely renames or applies trivial cosmetic modifications to EAR-GRPO, CA-GRPO, AgentGuard, MediRush, AdaptiveReplica, TraceMind, EnclaveShield, SCRE-Align, or AdaptiveRL-Forge is strictly disqualified.

---

## 2. Project-by-Project Forensic Audit

### 1. `adaptive-rl-forge` (`WORK-01` / CARLS)
- **Canonical Title**: *Predicting Reinforcement-Learning Plasticity of Intermediate Language-Model Checkpoints: A Cross-Architecture Diagnostic Study*
- **Research Area**: Reinforcement Learning Dynamics / Foundation Model Plasticity / Pre-training Diagnostics
- **Research Problem**: Pre-training language models consumes immense compute, but practitioners do not know *when* during pre-training a checkpoint develops the structural capacity ("plasticity") to benefit from downstream RL alignment without gradient collapse or policy degeneration.
- **Scientific Contribution**: Introduces the Capability-Aware Reinforcement Learning Scheduler (CARLS) and an empirical diagnostic framework evaluating layer-wise gradient signal-to-noise ratio (SNR), representation drift, and downstream RL loss surface curvature across intermediate pre-training checkpoints.
- **Methods**: Diagnostic probing, layer-wise gradient SNR analysis, Fisher Information Matrix spectral analysis, policy gradient plasticity tracking.
- **Datasets**: Pre-training diagnostic slices (Pythia / OpenWebText subsets), downstream alignment sets (GSM8K, Math, Anthropic HH-RLHF).
- **Models**: SmolLM-135M, DistilGPT2, Pythia-70M/160M/410M, Qwen-2.5-0.5B/1.5B intermediate checkpoints.
- **Results**: Verified empirical run provenance; demonstrates that downstream RL plasticity non-linearly emerges before full loss convergence and is strongly predicted by mid-layer spectral stability.
- **Publication Status**: Journal Article — Submitted to *Journal of Machine Learning Research (JMLR)* (Under Review, August 2026).
- **Strengths**: High methodological rigor, strict run provenance verification, clean rejection of synthetic simulation numbers, deep diagnostic metrics.
- **Weaknesses**: Evaluated on smaller parameter scales ($\le 1.5\text{B}$); does not yet address online RL credit assignment or multi-turn agentic environments.

---

### 2. `ear_grpo_reasoning` (`EAR-GRPO` / `CA-GRPO`)
- **Canonical Title**: *When Confidence Proxies Confound Reasoning Complexity: Pitfalls of Uncertainty-Weighted Credit Assignment in Language Model Reinforcement Learning*
- **Research Area**: Reinforcement Learning from Rule-Based Verifiers (RLVR) / Uncertainty Quantification / Mathematical Reasoning
- **Research Problem**: When applying Group Relative Policy Optimization (GRPO) to mathematical reasoning, whether weighting policy gradient advantages by trajectory-level uncertainty or confidence proxies prevents policy collapse or filters exploration noise.
- **Scientific Contribution**: Falsified the hypothesis that uncertainty-weighted policy gradient credit assignment improves RLVR. Proved that internal confidence proxies (predictive entropy, token NLL, logit margin) are heavily confounded with derivation sequence length ($r \approx +0.49$), penalizing multi-step derivations. Proved via 5-way controlled experiments across 3 matched seeds that Consistency-Aware GRPO yields $\Delta = 0.00\%$ over standard outcome-supervised GRPO.
- **Methods**: Monte Carlo dropout probing audit on zero-dropout architectures, partial correlation analysis $r(\text{Error} \mid \text{Length})$, group advantage weighting, 5-way controlled RL post-training (Standard GRPO, Compute-Matched GRPO, Random-Weight Control, Permuted-Weight Control, CA-GRPO).
- **Datasets**: GSM8K held-out benchmark ($N=100$ independent prompt clusters).
- **Models**: Qwen2.5-0.5B-Instruct, Qwen2.5-Math-1.5B.
- **Results**: Self-consistency consensus has high offline AUROC ($0.812$), but online RL policy gradient weighting provides $80.00\% \pm 0.00\%$ test accuracy—identical to standard GRPO ($80.00\%$).
- **Publication Status**: Journal Article — Submitted to *IEEE Transactions on Artificial Intelligence (IEEE TAI)* (August 2026).
- **Strengths**: Exemplary scientific integrity, transparent negative results, preregistered experimental gate, strong statistical controls (permutation + compute-matched).
- **Weaknesses**: Focused on single-turn math reasoning (GSM8K); does not address long-horizon multi-step interactive agent environments or process verifier distortion.

---

### 3. `scre-align` (`SCRE-Align`)
- **Canonical Title**: *Self-Correcting Reasoning Engine: PRM-Guided MCTS Backtracking for LLM Reasoning*
- **Research Area**: Test-Time Compute / Search / Process Reward Modeling (PRM)
- **Research Problem**: Mitigating reward hacking, uncalibrated entropy spikes, and post-hoc rationalizations in LLM step-by-step reasoning chains during inference.
- **Scientific Contribution**: Implements an inference-time test-time search system coupling Process Reward Models (PRMs) with Monte Carlo Tree Search (MCTS) step backtracking and token entropy pruning.
- **Methods**: MCTS step exploration, PRM score thresholding, predictive entropy filtering, vLLM / FastAPI serving infrastructure.
- **Datasets**: GSM8K, MATH, synthetic multi-step reasoning queries.
- **Models**: DeepSeek-R1-Distill-Qwen-1.5B/7B, Qwen2.5-Math-PRM-7B.
- **Results**: Shows that PRM step backtracking prunes hallucinated sub-steps in test-time inference.
- **Publication Status**: Open-source research codebase / prototype artifact.
- **Strengths**: Practical systems implementation with high-throughput vLLM serving, clean integration of PRM and search.
- **Weaknesses**: Lacks theoretical analysis of PRM search error bounds or test-time verification collapse under out-of-distribution math reasoning.

---

### 4. `agentguard-final` (`AgentGuard`)
- **Canonical Title**: *AgentGuard: Runtime Action Provenance Lineage DAGs and Policy Interception for Autonomous AI Agents*
- **Research Area**: AI Agent Safety / Runtime Policy Enforcement / Threat Mitigation
- **Research Problem**: Autonomous LLM agents executing multi-step tool calls are vulnerable to prompt injection, indirect instruction hijacking, and unauthorized privilege escalation from untrusted external payloads.
- **Scientific Contribution**: Develops a runtime action provenance DAG engine that tracks data-flow lineage from user intent down to tool execution parameters, intercepting malicious or hijacked tool calls via deterministic security invariants.
- **Methods**: Dynamic provenance graph construction, policy rule AST matching, runtime authorization gating, human-in-the-loop escalation.
- **Datasets**: AgentGuardBench (synthetic prompt injection and tool hijacking scenarios).
- **Models**: Multi-agent tool-use runners (Claude-3.5-Sonnet / GPT-4o-mini / local Llama-3-8B).
- **Results**: High detection and blocking rate for indirect injection attacks across tool-use benchmarks.
- **Publication Status**: Open-source research software & working manuscript.
- **Strengths**: Clean software architecture, intuitive provenance graph model, robust policy gateway.
- **Weaknesses**: Primarily evaluated on rule-based attack patterns; lacks adaptive adversarial evaluation against learning attackers.

---

### 5. `medirush` (`MediRush` / `MediRush-SafeAgent`)
- **Canonical Title**: *MediRush: Policy-Constrained Clinical Decision Support & Triage Risk Modeling*
- **Research Area**: Healthcare AI / Clinical ML / Safe Tool-Using Agents
- **Research Problem**: Clinical LLM assistants risk generating unverified diagnostic recommendations, hallucinated drug interactions, and unconstrained action execution in high-stakes healthcare triage.
- **Scientific Contribution**: A policy-constrained clinical agent architecture combining multi-stage intent verification, clinical safety guardrails, dynamic risk assessment, and state verification.
- **Methods**: Multi-tier intent filtering, medical ontology validation, risk score classification, human-in-the-loop escalation.
- **Datasets**: MediRushBench (clinical triage scenarios, contraindication checks).
- **Models**: Med-PaLM-2 / Clinical Llama / Fine-tuned Qwen medical adapters.
- **Results**: Reduces unsafe medical action execution in simulated triage scenarios.
- **Publication Status**: Manuscript in preparation (Target: *Elsevier Artificial Intelligence in Medicine*).
- **Strengths**: Domain-specific constraint modeling, clear safety architecture, full-stack application prototype.
- **Weaknesses**: Evaluated on synthetic benchmark cases rather than prospectively validated clinical trial workflows.

---

### 6. `quorumshift` (`AdaptiveReplica` / `WORK-03`)
- **Canonical Title**: *AdaptiveReplica: Dynamic Quorum Adaptation and Failure-Aware Replica Selection in Distributed Consensus*
- **Research Area**: Distributed Systems / Consensus Protocols / Fault Tolerance
- **Research Problem**: Static majority quorums in Raft/Paxos experience severe p99 tail-latency degradation under asymmetric network partitions and transient node slowdowns.
- **Scientific Contribution**: Dynamic quorum adaptation protocol over Raft joint-consensus configuration transitions, adjusting replica voting weights in real-time based on link latency and packet loss.
- **Methods**: C++20 Raft consensus engine, dynamic weight calculation, joint-consensus state machine transitions.
- **Datasets**: Network degradation fault injection metrics (16 failure scenarios).
- **Models / Artifacts**: C++20 distributed consensus simulator.
- **Results**: Achieves $88.8\%$ reduction in write p99 tail latency (from $120.48\text{ms}$ to $13.50\text{ms}$) under 50ms asymmetric network fault injection while maintaining $100\%$ consistency.
- **Publication Status**: Journal Article — Submitted to *IEEE Transactions on Artificial Intelligence (IEEE TAI)* / Targeted for *IEEE TPDS* (August 2026).
- **Strengths**: High-performance C++20 implementation, formal invariant verification of joint consensus.
- **Weaknesses**: Systems-heavy domain; minimal foundation model or machine learning intersection.

---

### 7. `tracemind` (`TraceMind` / `WORK-04`)
- **Canonical Title**: *TraceMind: Graph-Constrained Causal Reasoning for Root-Cause Localization in Microservice Systems*
- **Research Area**: Cloud Observability / AIOps / Graph Causal Inference
- **Research Problem**: LLMs applied to microservice root-cause analysis hallucinate non-existent fault propagation paths when reasoning over massive unparsed telemetry logs.
- **Scientific Contribution**: Restricts LLM causal inference to valid topological walk paths on OpenTelemetry Service Dependency Graphs (SDGs), fusing trace duration variances, anomaly scores, and log entropy.
- **Methods**: Graph walk constraints, causal edge weight calculation, OpenTelemetry trace parsing, LLM structured extraction.
- **Datasets**: CausalOpsBench (24 cascading fault injection scenarios).
- **Models**: Graph traversal engine + LLM reasoning agents (GPT-4o / Claude / Qwen).
- **Results**: Achieves $100.0\%$ Top-1 root-cause localization accuracy (MRR = $1.00$) vs $0.0\%$ for unconstrained LLM baselines.
- **Publication Status**: Journal Article — Targeted for *IEEE Transactions on Cloud Computing (IEEE TCC)* (August 2026).
- **Strengths**: Bridges graph constraints with LLM reasoning, eliminates topological hallucinations.
- **Weaknesses**: Evaluated on controlled synthetic fault topologies; needs validation on large-scale production microservice graphs with thousands of nodes.

---

### 8. `enclaveshield` (`EnclaveShield` / `WORK-02`)
- **Canonical Title**: *EnclaveShield: Zero-Knowledge Memory Attestation and Side-Channel Mitigation for Hardware Enclaves*
- **Research Area**: Confidential Computing / Hardware Security / Oblivious RAM
- **Research Problem**: Hardware enclaves (Intel SGX, AMD SEV) remain vulnerable to memory access pattern side-channel attacks and heavy performance overhead under standard ORAM.
- **Scientific Contribution**: Adaptive ORAM page access obfuscation coupled with Zero-Knowledge memory attestation proofs.
- **Methods**: Path-ORAM optimization, zero-knowledge attestation circuits, memory trace obfuscation.
- **Datasets**: EnclaveBench (20 memory access workload traces).
- **Publication Status**: Working Paper / Target: *IEEE TDSC*.
- **Strengths**: Solid systems security design and formal threat model.
- **Weaknesses**: Domain-isolated from core ML/RL foundation model research.

---

### 9. `secure-cloud-infrastructure-platform` (`WORK-05`)
- **Canonical Title**: *Compositional AST Invariant Verification for Declarative Container Workload Specifications*
- **Research Area**: Cloud Infrastructure Security / Formal Verification
- **Research Problem**: Misconfigurations in declarative Kubernetes / Terraform specifications lead to privilege escalation and cloud security vulnerabilities.
- **Scientific Contribution**: AST parser and static invariant verification engine for container configurations.
- **Publication Status**: Software research prototype.
- **Strengths**: Practical static analysis tool.
- **Weaknesses**: Software engineering tool without statistical or learning components.

---

## 3. Comprehensive Overlap & Exclusion Matrix

To ensure total novelty and intellectual separation, the table below lists the boundary constraints:

| Existing Project | Core Mechanism / Idea | BANNED in New Projects (Do NOT Repeat) | ALLOWED / OPEN FRONTIER |
| :--- | :--- | :--- | :--- |
| **`adaptive-rl-forge`** | Checkpoint plasticity during pretraining; layer gradient SNR | Pretraining checkpoint selection; simple Fisher SNR tracking | Online test-time adaptation, continual RL stability, representation collapse under multi-turn self-play |
| **`ear_grpo_reasoning`** | Sample-level uncertainty weighting in GRPO for single-turn math; length confounding | Renaming confidence weighting; GSM8K uncertainty scoring; MC-dropout on zero-dropout LLMs | Process verifier misalignment, credit assignment over long-horizon tool trajectories, non-stationary reward shift |
| **`scre-align`** | PRM + MCTS inference search on single-turn math | Basic MCTS search with Qwen PRM; heuristic backtracking | Theoretical limits of search under verifier bias; self-correction collapse; search over latent state-spaces |
| **`agentguard-final`** | Provenance DAG for prompt injection / tool authorization | Rule-based DAG tool filters; basic prompt injection benchmarks | Multi-agent emergent coordination breakdown; causal credit assignment for agent failure across 50+ tool calls |
| **`medirush`** | Clinical triage guardrail pipeline | Rule-based triage classification; medical chatbot prompts | Generalizable agent world-model verification, distributional shift detection in dynamic environments |
| **`tracemind`** | Graph-constrained LLM walk for AIOps root-cause | Simple microservice graph topological path pruning | Causal world-model discovery, dynamic multi-agent credit assignment, state-space representations |
| **`quorumshift`** | Dynamic Raft consensus weights under network jitter | Raft consensus simulation; network tail-latency tuning | Distributed multi-agent consensus learning, Byzantine-robust decentralized agent policy coordination |

---

## 4. Current Research Identity Mapping (Phase 1 Synthesis)

### Primary Research Identity
**Reliable Reinforcement Learning and Post-Training for Foundation Models & Autonomous Agents**

### Secondary Theme 1
**Mechanistic Diagnostics, Representation Dynamics & Failure Calibration in Reasoning Models**

### Secondary Theme 2
**Causal Credit Assignment and Fault-Tolerant Coordination in Long-Horizon Multi-Agent Systems**

### Coherence Justification
Across `adaptive-rl-forge`, `ear_grpo_reasoning`, `tracemind`, and `agentguard-final`, the candidate possesses a rare combination of:
1. **Methodological Skepticism & Rigorous Diagnostic Probing**: Willingness to execute negative controls, discover confounding variables (e.g., length confounding in predictive entropy), and publish rigorous negative findings.
2. **Deep Post-Training & RL Fluency**: Familiarity with RLVR, GRPO, policy gradient dynamics, PRMs, and representation spaces.
3. **Systems & Invariant Engineering**: Mathematical maturity to enforce graph, causal, and safety invariants rather than relying on unconstrained generative heuristics.

This foundation establishes the ideal launchpad for top-tier PhD programs (Harvard, Stanford, MIT).
