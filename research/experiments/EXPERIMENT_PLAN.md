# Master Portfolio Experiment & Benchmark Plan

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Scope**: Experimental protocol, random seed handling, baseline configurations, statistical tests, and automated runner designs.

---

## Standardized Statistical Protocol

For ALL experiments across all repositories:
1. **Independent Runs**: Minimum $N = 5$ random seeds ($\text{seed} \in \{42, 43, 44, 45, 46\}$).
2. **Descriptive Statistics**: Report Mean $\mu$, Median $M$, Standard Deviation $\sigma$, and 95% Confidence Interval ($95\% \text{ CI} = \mu \pm 1.96 \cdot \frac{\sigma}{\sqrt{N}}$).
3. **Hypothesis Testing**: Two-sided Student's $t$-test or Mann-Whitney $U$ test (for non-normal distributions) comparing proposed method vs. strongest baseline. Report exact $p$-value ($p < 0.01$ significance threshold).
4. **Effect Size**: Cohen's $d = \frac{\mu_{\text{proposed}} - \mu_{\text{baseline}}}{\sigma_{\text{pooled}}}$.
5. **No Selective Reporting**: Report all 5 seeds, including outliers and negative/inconclusive trials.

---

## 1. AdaptiveRL-Forge (`adaptive-rl-forge`)

### Experimental Protocol
* **Goal**: Validate intermediate checkpoint representation metrics ($\alpha_{SVD}, \bar{H}, \sigma_g^2$) against empirical GRPO/PPO post-training RL reward plasticity $\beta_{RL}$.
* **Baselines**:
  - `B0 (Final Checkpoint Late RL)`: Standard fine-tuning at end of pre-training.
  - `B1 (Step 10k Early RL)`: Fine-tuning at premature checkpoint.
  - `B2 (Sequential Pretrain+RL)`: Fixed schedule without diagnostic feedback.
  - `B3 (Random Checkpoint Selection)`: Randomly selected checkpoint.
  - `B4 (CARLS Proposed Probe)`: Representation entropy & singular value diagnostic selection.
* **Metrics**: Predictor Pearson $r$, Spearman $\rho$, $R^2$, Mean Absolute Error (MAE), RL reward gain slope ($\beta_{RL}$).
* **Hardware & Runtime**: Apple Silicon M-series (MPS) / PyTorch 2.x, 5 independent seeds.

---

## 2. EnclaveShield (`enclaveshield`)

### Experimental Protocol
* **Goal**: Measure Zero-Knowledge quote attestation latency and dynamic ORAM page access pattern entropy under controlled side-channel page-fault workloads.
* **Baselines**:
  - `B0 (Unprotected Host)`: Native un-encrypted host execution.
  - `B1 (Standard SGX/TDX)`: Standard enclave without memory access obfuscation.
  - `B2 (Static Path ORAM)`: Fixed-path Path ORAM tree (Stefanov et al. 2013).
  - `EnclaveShield (Proposed)`: Adaptive frequency-weighted ORAM tree + ZK quote verification.
* **Metrics**: ZK Quote Attestation Success (%), Page Access Entropy ($H(A)$), Page Access Latency ($L_{ORAM}$ ms), Latency Ratio ($L_{\text{ORAM}} / L_{\text{native}}$).
* **Workloads**: `EnclaveBench` suite (20 workload scenarios across 5 side-channel threat profiles).

---

## 3. QuorumShift / AdaptiveReplica (`quorumshift`)

### Experimental Protocol
* **Goal**: Evaluate consensus throughput, latency, and stale read frequency under asymmetric node degradation and network partition scenarios.
* **Baselines**:
  - `B0 (Fixed R=3 Static Majority)`: Standard Raft majority quorum ($R=3, N=5$).
  - `B1 (Fixed R=5 Static Majority)`: Static full quorum ($R=5, N=5$).
  - `B2 (Random Placement)`: Random follower selection.
  - `B3 (Latency-Aware Placement)`: Static latency-ranked follower selection.
  - `B4 (Failure-Domain Static)`: Static topology partition policy.
  - `AdaptiveReplica (Proposed)`: Failure-aware dynamic quorum adaptation policy.
* **Metrics**: Availability (%), p50 Latency (ms), p99 Latency (ms), Throughput (ops/sec), Stale Read Count ($S_{\text{stale}}$).
* **Fault Scenarios**: Asymmetric 50ms link latency injection, isolated follower crash, dynamic 3-2 network partition.

---

## 4. Secure Cloud Infrastructure Platform (`secure-cloud-infrastructure-platform`)

### Experimental Protocol
* **Goal**: Measure static manifest AST attack-graph verification precision, recall, and admission latency on Kubernetes declarative workload specifications.
* **Baselines**:
  - `B0 (Unchecked Manifests)`: Native K8s API admission without custom validation.
  - `B1 (Static YAML Rule Linter)`: Isolated attribute checking (KubeLinter rules).
  - `B2 (OPA/Rego Policy Rules)`: Open Policy Agent declarative rule set.
  - `Proposed AST Graph Engine`: Multi-resource AST privilege escalation graph verification.
* **Metrics**: Attack Path Coverage (%), Misconfiguration Detection Precision (%), Recall (%), Verification Overhead (ms).

---

## 5. TraceMind (`tracemind`)

### Experimental Protocol
* **Goal**: Evaluate Root Cause Analysis (RCA) top-k accuracy, Mean Reciprocal Rank (MRR), and diagnostic latency on multi-modal microservice failure streams.
* **Baselines**:
  - `B0 (Threshold Alerts)`: Standard metric threshold alerting rules.
  - `B1 (IsolationForest Metric)`: Unsupervised metric anomaly detector.
  - `B2 (Unconstrained LLM Reasoning)`: Raw log prompt reasoning without graph constraints.
  - `TraceMind (Proposed)`: Graph-constrained topological causal walk over Service Dependency Graphs (SDGs).
* **Metrics**: Top-1 Accuracy (%), Top-3 Accuracy (%), Mean Reciprocal Rank (MRR), Diagnosis Latency (ms).
* **Benchmark**: `CausalOpsBench` (24 fault scenarios across 6 fault injection modes: latency spike, CPU hog, memory leak, packet loss, process crash, disk full).
