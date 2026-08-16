# Sham Satish Thakare
**Independent Computer Science Researcher**  
Pune, India | Phone: +91 7776807761 | Email: shamthakare3000@gmail.com  
GitHub: [https://github.com/shamddd](https://github.com/shamddd) | Web: [https://shamthakare.github.io](https://shamthakare.github.io)

---

## RESEARCH STATEMENT & INTERESTS
I conduct foundational and systems research on **Trustworthy, Adaptive, and Verifiable Autonomous Systems**. My work focuses on four primary vectors:
1. **Foundation Model Plasticity**: Representation geometry diagnostics ($\alpha_{\text{SVD}}, \bar{H}, \sigma_g^2$) for predicting reinforcement learning reward plasticity in intermediate language-model checkpoints.
2. **Confidential Computing**: Zero-knowledge attestation proofs and frequency-weighted adaptive Oblivious RAM (ORAM) tree rebalancing algorithms for hardware enclaves (SGX/TDX).
3. **Distributed Consensus**: Failure-domain aware dynamic quorum adaptation ($\text{AdaptiveReplica}$) for fault-tolerant Raft consensus under asymmetric node degradation.
4. **Causal Observability**: Graph-constrained topological causal walks over OpenTelemetry microservice dependency graphs for root-cause localization.

---

## EDUCATION
**Anantrao Pawar College of Engineering & Research (APCOER)**, Pune, India  
*Bachelor of Technology in Artificial Intelligence and Data Science* | **Jan 2020 – Jun 2024**  
* **Cumulative GPA**: 8.70 / 10.00
* **Core Coursework**: Engineering Mathematics, Scientific Computing, Operating Systems, Design and Analysis of Algorithms, Object-Oriented Programming (C++), Python Programming, Data Structures, Computer Networks, Database Management Systems, Artificial Intelligence, Machine Learning, Computational Modeling, Signal Processing, Linear Algebra, Probability and Statistics.
* **Academic Honors**: Awarded 100% Merit Scholarship for 8 consecutive semesters based on academic performance.

---

## RESEARCH EXPERIENCE & MANUSCRIPTS

### 1. Foundation Model Plasticity & Diagnostic Probes
* **Predicting Reinforcement-Learning Plasticity of Intermediate Language-Model Checkpoints: A Cross-Architecture Diagnostic Study**  
  *Author*: Sham Satish Thakare  
  *Status*: **Submitted / Under Review at Journal of Machine Learning Research (JMLR)** (2026)  
  *Repository*: [`adaptive-rl-forge`](https://github.com/shamddd/adaptive-rl-forge)  
  *Key Finding*: Formulated diagnostic probing vectors $\mathbf{\phi}(C_k)$ measuring layer-wise representation entropy and singular value spectrum decay rates. Demonstrates that checkpoint plasticity predicts downstream GRPO reward gain $\beta_{RL}$ with $R^2 = 0.91$ ($p = 0.0004$), consuming $< 2\%$ of the compute required for full RL policy gradient rollouts.

### 2. Confidential Hardware Enclave Memory Security
* **EnclaveShield: Zero-Knowledge Memory Attestation and Side-Channel Mitigation for Hardware Enclaves**  
  *Author*: Sham Satish Thakare  
  *Status*: **Preprint / Working Paper** (Target: *IEEE Transactions on Dependable and Secure Computing - TDSC*) (2026)  
  *Repository*: [`enclaveshield`](https://github.com/shamddd/enclaveshield)  
  *Key Finding*: Engineered ZK quote attestation membership proofs and access-frequency-weighted adaptive Path ORAM tree rebalancing. Achieves page access pattern entropy $H(A) = 0.82 \pm 0.02$ while bounding page access latency to $1.47\text{ms}$ ($2.45\times$ host baseline vs $15.00\text{ms}$ static Path ORAM).

### 3. Distributed Consensus & Quorum Adaptation
* **AdaptiveReplica: Dynamic Quorum Adaptation and Failure-Aware Replica Selection in Distributed Consensus**  
  *Author*: Sham Satish Thakare  
  *Status*: **Preprint / Working Paper** (Target: *IEEE Transactions on Parallel and Distributed Systems - TPDS*) (2026)  
  *Repository*: [`quorumshift`](https://github.com/shamddd/quorumshift)  
  *Key Finding*: Formulated dynamic vote-weight adaptation over Raft joint-consensus transitions. Achieves $99.97\%$ availability and reduces p99 write latency to $13.50\text{ms}$ ($88.8\%$ reduction vs static $R=5$ majority $120.48\text{ms}$) under asymmetric node degradation with zero stale reads ($S_{\text{stale}} = 0$).

### 4. Microservice AIOps & Causal Observability
* **TraceMind: Graph-Constrained Causal Reasoning for Root-Cause Localization in Microservice Systems**  
  *Author*: Sham Satish Thakare  
  *Status*: **Preprint / Working Paper** (Target: *IEEE Transactions on Cloud Computing - TCC*) (2026)  
  *Repository*: [`tracemind`](https://github.com/shamddd/tracemind)  
  *Key Finding*: Constructed topological causal walks over OpenTelemetry Service Dependency Graphs. Achieves $100.0\%$ Top-1 RCA accuracy (MRR = 1.00) across 24 cascading fault scenarios in `CausalOpsBench`, outperforming unconstrained LLM reasoning (Top-1 = 0.0%, MRR = 0.44).

---

## PROFESSIONAL WORK EXPERIENCE
**Spectra Corporate Service**, Pune, India  
*Data Engineer / Machine Learning Specialist* | **Jun 2024 – Present**  
* Architected scalable data pipelines using C++, Python, and SQL on GCP and AWS (GKE, Compute Engine, IAM, Cloud Storage, Cloud Logging).
* Designed multithreaded Linux system software with strict synchronization invariants, virtual memory isolation, and container security controls.
* Developed automated CI/CD and infrastructure-as-code automation pipelines using Terraform, Docker, Kubernetes, and GitHub Actions.
* Constructed Prometheus and Grafana distributed telemetry dashboards for SLA monitoring and proactive incident detection.

**APCOER Pune**, Pune, India  
*Research Intern / Teaching Fellow* | **Jun 2023 – Dec 2024**  
* Served as Teaching Fellow for *Intro to Algorithms and Their Limitations* and *Foundations of ML: AI Alignment and Safety* (Aug 2024 – Dec 2024).
* Served as Course Producer for *Fundamentals of Computation*, *Introduction to Algorithms*, and *Theory of Computation* (Aug 2022 – May 2023).
* Assisted faculty in experimental design, statistical analysis, and open-source software reproducibility protocols.

---

## TECHNICAL SKILLS
* **Languages**: Python, C++, C, Rust, Go, Java, SQL, Shell (Bash), LaTeX
* **AI & Machine Learning**: PyTorch, GRPO / PPO RL Probes, Transformers, HuggingFace, NumPy, SciPy, Scikit-Learn
* **Confidential Computing & Security**: TEEs (SGX/TDX), Oblivious RAM (Path ORAM), Zero-Knowledge Attestation, POSIX System Security
* **Distributed Systems & Cloud**: Raft Consensus, OpenTelemetry, Docker, Kubernetes, Helm, Terraform, GCP, AWS, Prometheus, Grafana
