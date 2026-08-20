# Novelty Collision Map

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Scope**: Systematic collision analysis against published literature.

---

## Standardized Collision Audit Matrix

| Project | Primary Literature Match | Year | Venue | Method Comparison | Baseline Setup | Metric Comparison | Similarity | Collision Risk | Technical Difference & Scientific Defense |
| :--- | :--- | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| **`adaptive-rl-forge`** | Lyle et al. (*Plasticity in Deep RL*) | 2023 | ICLR | Evaluates plasticity loss in deep RL vs. Our representation diagnostic probing | Toy/Gridworld vs. PyTorch LM checkpoints (Pythia/Qwen) | Train loss vs. Predictor correlation ($R^2$, MAE) & RL gain ($\beta_{RL}$) | **30%** | **LOW** | We predict pre-training checkpoint RL plasticity *before* launching RL fine-tuning loops. JMLR manuscript strictly preserved. |
| **`enclaveshield`** | Ahmad et al. (*Obliviate*) | 2018 | NDSS | Static Path ORAM on SGX file system vs. Our ZK remote attestation + Adaptive ORAM | Static binary access vs. EnclaveBench side-channel workloads | Latency (15x) vs. Latency ratio (< 2.5x) & Page Access Entropy ($H \ge 0.8$) | **40%** | **LOW** | Combines ZK quote verification with dynamic access frequency-weighted ORAM tree rebalancing. |
| **`quorumshift`** | Howard et al. (*Flexible Paxos*) | 2016 | FP | Disjoint read/write quorum sizes vs. Our failure-domain dynamic quorum adaptation | Static network topology vs. Fault-injection network partitions | Throughput vs. p95/p99 Latency under asymmetric failure ($13.5\text{ms}$ vs $120.4\text{ms}$) | **35%** | **LOW** | Dynamic vote weight adaptation over Raft joint-consensus protocol with $0$ stale reads under partition. |
| **`secure-cloud-infra-platform`** | Torres et al. (*IaC Static Analysis*) | 2021 | USENIX Security | Rule-based YAML linter vs. Our AST privilege escalation graph checker | KubeLinter rules vs. Multi-stage attack graph synthesis | Rule count vs. Attack path coverage & precision/recall | **45%** | **MODERATE** | Transforms rule checking into graph AST traversal for multi-resource IAM/K8s privilege escalation. |
| **`tracemind`** | Wu et al. (*MicroRCA*) | 2020 | IEEE NOMS | Correlation graph on metric anomalies vs. Our graph-constrained OTEL trace/log/metric fusion | Synthetic fault metrics vs. CausalOpsBench 24 fault scenarios | Top-1 Accuracy (75%) vs. Top-1 Accuracy (100%), MRR (1.00) | **40%** | **LOW** | Incorporates graph-constrained topological walks over Service Dependency Graphs fusing traces, metrics, and logs. |
