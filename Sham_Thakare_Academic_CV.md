# Sham Satish Thakare
**Independent Computer Science Researcher**  
Pune, India | Phone: +91 7776807761 | Email: shamthakare3000@gmail.com  
GitHub: [https://github.com/shamddd](https://github.com/shamddd) | Web: [https://shamthakare.github.io](https://shamthakare.github.io)

---

## RESEARCH STATEMENT & INTERESTS
I conduct foundational and systems research on **Trustworthy, Adaptive, and Verifiable Autonomous Systems**. My work focuses on four primary vectors:
1. **Foundation Model Plasticity & Calibrated Reasoning**: Representation geometry diagnostics ($\alpha_{\text{SVD}}, \bar{H}, \sigma_g^2$) for predicting reinforcement learning reward plasticity in intermediate checkpoints, token entropy length confounding, and RLVR self-consistency calibration.
2. **Confidential Computing & Hardware Security**: Zero-knowledge remote attestation membership proofs and access-frequency-weighted adaptive Oblivious RAM (ORAM) tree rebalancing algorithms for hardware enclaves (SGX/TDX).
3. **Learning-Augmented Distributed Consensus**: Failure-domain aware dynamic quorum adaptation ($\text{AdaptiveReplica}$) over Raft joint-consensus transitions with uncertainty-aware trust gates ($T_3$).
4. **Causal Observability & Verifiable AI Systems**: Topological causal walks over OpenTelemetry microservice dependency graphs ($\text{TraceMind}$) and zero-knowledge authorization-path provenance graph proofs ($\text{EnclaveShield}$).

---

## EDUCATION
**Anantrao Pawar College of Engineering & Research (APCOER)**, Pune, India  
*Bachelor of Technology in Artificial Intelligence and Data Science* | **Jan 2020 – Jun 2024**  
* **Cumulative GPA**: 8.70 / 10.00
* **Core Coursework**: Engineering Mathematics, Scientific Computing, Operating Systems, Design and Analysis of Algorithms, Object-Oriented Programming (C++), Python Programming, Data Structures, Computer Networks, Database Management Systems, Artificial Intelligence, Machine Learning, Computational Modeling, Signal Processing, Linear Algebra, Probability and Statistics.
* **Academic Honors**: Awarded 100% Merit Scholarship for 8 consecutive semesters based on academic performance.

---

## RESEARCH EXPERIENCE & MANUSCRIPTS

### Active Submitted Manuscripts
1. **When Confidence Proxies Confound Reasoning Complexity: Pitfalls of Uncertainty-Weighted Credit Assignment in LM RL**  
   *Author*: Sham Satish Thakare  
   *Status*: **Submitted / Under Review at IEEE Transactions on Artificial Intelligence (IEEE TAI)** (Submitted Aug 2026)  
   *Repository*: [`ear_grpo_reasoning`](https://github.com/shamddd/ear_grpo_reasoning)  
   *Key Finding*: Exposes length confounding in token predictive entropy ($r = +0.486$). Sample-level consensus weighting (CA-GRPO) yields 0.00% Pass@1 gain over standard outcome-supervised GRPO across 3 matched seeds.

2. **recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning**  
   *Author*: Sham Satish Thakare  
   *Status*: **Submitted / Under Review at 11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026) / IEEE BigData 2026** (Submission ID: `BigD497`, Submitted Aug 17, 2026)  
   *Repository*: [`recovery_eval`](https://github.com/shamddd/recovery_eval)  
   *Key Finding*: Matched state-contrast protocol ($D_{\text{recovery}} = -0.1100$, 95% CI $[-0.240, +0.030]$) across 400 continuations of Qwen2.5-Math 1.5B.

3. **StateShift: State-Matched Evaluation of Error Recovery in Neural Reasoning**  
   *Author*: Sham Satish Thakare  
   *Status*: **Submitted / Under Review at Elsevier Artificial Intelligence (AIJ)** (Manuscript: `ARTINT-D-26-01491`, Submitted 2026)  
   *Repository*: [`stateshift`](https://github.com/shamddd/stateshift)  
   *Key Finding*: Formulates verifier-defined continuation state matching on neural reasoning rollouts under structural covariate controls.

### Preprints & Working Papers
4. **Amortized Intervention Frontiers for Language-Model Reasoning: When Does Training Beat Search?**  
   *Author*: Sham Satish Thakare  
   *Status*: **Working Paper** (Target under consideration: *Transactions on Machine Learning Research - TMLR*) (2026)  
   *Repository*: `submission/tmlr` / `submission_package`  
   *Key Finding*: Formalizes deployment cost frontiers ($C_{\text{total}} = C_{\text{train}} + Q \cdot C_{\text{inference}}$). Demonstrates OOD length extrapolation accelerates RLVR amortization crossover ($R_f \approx 0.0618 \ll 1.0$).

5. **Predicting Reinforcement-Learning Plasticity of Intermediate Language-Model Checkpoints: A Cross-Architecture Diagnostic Study**  
   *Author*: Sham Satish Thakare  
   *Status*: **Working Paper** (Target under consideration: *Journal of Machine Learning Research - JMLR*) (2026)  
   *Repository*: [`adaptive-rl-forge`](https://github.com/shamddd/adaptive-rl-forge)  
   *Key Finding*: Formulated diagnostic probing vectors $\phi(C_k)$ predicting downstream GRPO reward gain $\beta_{RL}$ with $R^2 = 0.91$ ($p = 0.0004$).

6. **EnclaveShield: Zero-Knowledge Memory Attestation and Side-Channel Mitigation for Hardware Enclaves**  
   *Author*: Sham Satish Thakare  
   *Status*: **Working Paper** (Target under consideration: *IEEE Transactions on Dependable and Secure Computing - TDSC*) (2026)  
   *Repository*: [`enclaveshield`](https://github.com/shamddd/enclaveshield)  
   *Key Finding*: Engineered ZK quote attestation membership proofs and access-frequency-weighted adaptive Path ORAM tree rebalancing ($1.47\text{ms}$ latency, $H(A) = 0.82 \pm 0.02$).

7. **AdaptiveReplica: Dynamic Quorum Adaptation and Failure-Aware Replica Selection in Distributed Consensus**  
   *Author*: Sham Satish Thakare  
   *Status*: **Working Paper** (Target under consideration: *IEEE Transactions on Parallel and Distributed Systems - TPDS*) (2026)  
   *Repository*: [`quorumshift`](https://github.com/shamddd/quorumshift)  
   *Key Finding*: Formulated dynamic vote-weight adaptation over Raft joint-consensus transitions with trust gates ($T_3$), reducing p99 write latency to $13.50\text{ms}$ ($88.8\%$ reduction vs static $120.48\text{ms}$) with zero stale reads.

8. **TraceMind: Graph-Constrained Causal Reasoning for Root-Cause Localization in Microservice Systems**  
   *Author*: Sham Satish Thakare  
   *Status*: **Working Paper** (Target under consideration: *IEEE Transactions on Cloud Computing - TCC*) (2026)  
   *Repository*: [`tracemind`](https://github.com/shamddd/tracemind)  
   *Key Finding*: Constructed topological causal walks over OpenTelemetry Service Dependency Graphs, achieving 100.0% Top-1 RCA accuracy (MRR = 1.00) across 24 fault scenarios.

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
