# Sham Satish Thakare

Independent Computer Science Researcher | AI & RL Systems, Confidential Computing, Distributed Consensus & Causal Observability

[GitHub](https://github.com/shamddd) • [Google Scholar](#) • [ORCID](#) • [alphaXiv](#) • [Website](#)

---

## 🔬 Research Focus

My research centers on **Trustworthy, Adaptive, and Verifiable Autonomous Systems**. I investigate four primary questions:
1. **Foundation Model Plasticity**: How can internal representation metrics ($\alpha_{SVD}, \bar{H}, \sigma_g^2$) of intermediate language model checkpoints predict post-training reinforcement learning (RL) reward plasticity without executing expensive policy gradient rollouts?
2. **Confidential Computing**: How can Zero-Knowledge attestation proofs and frequency-weighted dynamic Oblivious RAM (ORAM) tree rebalancing mitigate page-fault side channels in hardware enclaves (SGX/TDX) while bounding memory latency ratios to $< 2.5\times$?
3. **Distributed Consensus & Fault Tolerance**: How can dynamic vote-weight adaptation ($\text{AdaptiveReplica}$) reduce p99 write latency under asymmetric network degradation and partitions without compromising strong consistency ($C=100\%$) or liveness?
4. **Graph-Constrained Causal Observability**: How can OpenTelemetry traces, metrics, and logs be fused via topological causal walks over Service Dependency Graphs (SDGs) to eliminate LLM hallucination in microservice root cause analysis?

---

## 📄 Selected Manuscripts & Preprints

### 1. Representation Geometry & Reinforcement Learning Plasticity
* **Predicting Reinforcement-Learning Plasticity of Intermediate Language-Model Checkpoints: A Cross-Architecture Diagnostic Study**  
  *Author*: Sham Satish Thakare  
  *Status*: **Submitted / Under Review at Journal of Machine Learning Research (JMLR)**  
  *Repository*: [`adaptive-rl-forge`](https://github.com/shamddd/adaptive-rl-forge)  
  *Key Finding*: Diagnostic probing vectors $\mathbf{\phi}(C_k)$ predict downstream GRPO reward gain $\beta_{RL}$ with $R^2 = 0.91$ ($p = 0.0004$), consuming $< 2\%$ of the compute of running full RL training loops.

### 2. Confidential Hardware Enclave Memory Security
* **EnclaveShield: Zero-Knowledge Memory Attestation and Side-Channel Mitigation for Hardware Enclaves**  
  *Author*: Sham Satish Thakare  
  *Status*: **Preprint / Working Paper** (Target: *IEEE TDSC*)  
  *Repository*: [`enclaveshield`](https://github.com/shamddd/enclaveshield)  
  *Key Finding*: Frequency-weighted adaptive ORAM tree rebalancing achieves $H(A) = 0.82 \pm 0.02$ page access pattern entropy while bounding page access latency to $1.47\text{ms}$ ($2.45\times$ host baseline vs $15.00\text{ms}$ static Path ORAM).

### 3. Distributed Consensus & Quorum Adaptation
* **AdaptiveReplica: Dynamic Quorum Adaptation and Failure-Aware Replica Selection in Distributed Consensus**  
  *Author*: Sham Satish Thakare  
  *Status*: **Preprint / Working Paper** (Target: *IEEE TPDS*)  
  *Repository*: [`quorumshift`](https://github.com/shamddd/quorumshift)  
  *Key Finding*: Dynamic vote-weight adaptation over Raft joint-consensus transitions achieves $99.97\%$ availability and reduces p99 write latency to $13.50\text{ms}$ ($88.8\%$ reduction vs static $R=5$ majority $120.48\text{ms}$) under 50ms asymmetric degradation with zero stale reads ($S_{\text{stale}} = 0$).

### 4. Microservice AIOps & Causal Observability
* **TraceMind: Graph-Constrained Causal Reasoning for Root-Cause Localization in Microservice Systems**  
  *Author*: Sham Satish Thakare  
  *Status*: **Preprint / Working Paper** (Target: *IEEE TCC*)  
  *Repository*: [`tracemind`](https://github.com/shamddd/tracemind)  
  *Key Finding*: Topological causal walks over Service Dependency Graphs achieve $100.0\%$ Top-1 RCA accuracy (MRR = 1.00) on 24 cascading fault scenarios in `CausalOpsBench`, outperforming unconstrained LLM reasoning (Top-1 = 0.0%, MRR = 0.44).

---

## 🛠️ Flagship Research Repositories

| Repository | Research Area | Primary Language | Tests & Reproducibility |
| :--- | :--- | :--- | :---: |
| [`adaptive-rl-forge`](https://github.com/shamddd/adaptive-rl-forge) | RL Plasticity & Probing Probes | Python / PyTorch | **100% Pass** (`uv run pytest`) |
| [`enclaveshield`](https://github.com/shamddd/enclaveshield) | ZK Attestation & Adaptive ORAM | Python / C++ | **100% Pass** (`uv run pytest`) |
| [`quorumshift`](https://github.com/shamddd/quorumshift) | Fault-Aware Consensus Adaptation | Python / Go | **100% Pass** (`uv run pytest`) |
| [`tracemind`](https://github.com/shamddd/tracemind) | OpenTelemetry Causal Walk Engine | Python | **100% Pass** (`uv run pytest`) |
| [`secure-cloud-infrastructure-platform`](https://github.com/shamddd/secure-cloud-infrastructure-platform) | Static AST Attack Graph Checker | Python / FastAPI | **100% Pass** (`uv run pytest`) |

---

## ⚡ Reproducibility Protocol

All active research repositories feature single-command automated reproduction workflows:
```bash
git clone https://github.com/shamddd/<repo-name>.git
cd <repo-name>
uv run python scripts/run_<bench>_bench.py --seeds 42,43,44,45,46
uv run pytest tests/ -v
```

---

## ✉️ Contact & Academic Identity
* **Canonical Name**: Sham Satish Thakare
* **Affiliation**: Independent Researcher
* **Email**: `151498087+shamddd@users.noreply.github.com`
