# Sham Satish Thakare
**Pre-Doctoral Researcher · Machine Learning, Distributed Systems & Computational Foundations**  
Capital One Systems Research · APCOER Pune (Savitribai Phule Pune University)  
Pune, Maharashtra, India | Email: shamthakare3000@gmail.com | Website: https://shamddd.github.io/shamthakare.github.io | GitHub: https://github.com/shamddd | SSRN: https://ssrn.com/author=13130226

---

## Research Interests
* **Foundations of Machine Learning & Reasoning**: Reinforcement learning with verifiable rewards (RLVR), policy optimization (GRPO/PPO), uncertainty calibration, length confounding, and state-matched error recovery dynamics.
* **Fault-Tolerant Distributed Systems**: State-machine replication (Raft, Paxos), dynamic quorum adaptation under network partitioning, linearizability verification, and tail latency minimization in modern C++20.
* **Mathematical & Quantum Foundations**: Spectral graph theory, convex optimization, stochastic processes, quantum information foundations (density matrix formalism, unitary dynamics), and quantum circuit compilation complexity.

---

## Education & Honors

### APCOER Pune (Savitribai Phule Pune University) — Pune, India
**Bachelor of Technology (B.Tech.) in Artificial Intelligence & Data Science** | *Jan 2020 – Jun 2024*  
* Cumulative GPA: **8.70 / 10.00** (First Class with Distinction; Final Year SGPA: **9.53 / 10.00**, Department Rank 1).
* **Gold Medal in Mathematics (2024)**: Awarded for highest academic standing across mathematical and quantitative curricula in the university cohort.
* **Core Mathematics Coursework**: Advanced Linear Algebra (Spectral Decomposition, SVD), Probability & Stochastic Processes, Optimization Theory (Convex Optimization, KKT Conditions), Discrete Mathematics & Graph Theory, Calculus & Differential Equations.
* **Computer Science Coursework**: Design & Analysis of Algorithms, Data Structures, Distributed Computing, Operating Systems, Machine Learning, Deep Learning, Computational Intelligence, Database Management Systems.

---

## Research & Professional Experience

### Capital One Systems Research — Pune, India
**Pre-Doctoral Researcher (Distributed Systems & Machine Learning)** | *Jun 2024 – Present*  
*Research Mentorship with Yuri Shelke (Distinguished Engineer at Capital One)*
* Formulated dynamic quorum adaptation algorithms for Raft consensus clusters (`quorumshift`), proving invariant quorum overlap ($\mathcal{Q}_i \cap \mathcal{Q}_j \neq \emptyset$) under dynamic replica re-weighting without violating state-machine linearizability.
* Developed an online latency-profiling and anomaly-filtering estimator eliminating $p99$ tail latency degradation under asymmetric network fault injection and non-uniform round-trip delays across distributed nodes.
* Engineered an asynchronous, lock-free C++20 distributed benchmarking harness evaluating multi-node consensus throughput across heterogeneous network partitions and emulated cross-datacenter WAN topologies.

### APCOER Pune — Pune, India
**Undergraduate Researcher & Teaching Assistant** | *Jun 2023 – May 2024*  
*Advisors: Prof. Sagar Gawande & Prof. Sunil Thakare*
* Investigated token predictive entropy behavior in autoregressive reasoning models, discovering strong completion-length confounding ($r = +0.486$) that undermines heuristic uncertainty weighting in reinforcement learning.
* Designed state-matched continuation evaluation protocols isolating nominal error self-correction from unconditional generative capacity under frozen structural covariates.
* Served as Teaching Assistant for undergraduate courses in *Data Structures, Algorithms, and Foundations of Machine Learning*, conducting tutorials and recitations for cohorts of 120+ engineering students.

---

## Publications & Manuscripts Under Review

1. **When Confidence Proxies Confound Reasoning Complexity: Pitfalls of Uncertainty-Weighted Credit Assignment in Language Model Reinforcement Learning**  
   **Sham Satish Thakare**  
   *Under Review at IEEE Transactions on Artificial Intelligence (IEEE TAI), 2024.*  
   [Code: https://github.com/shamddd/ear_grpo_reasoning] · [Research Note: https://shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity.html]  
   *Proved empirical completion-length confounding ($r = +0.486, p < 10^{-6}$) in token predictive entropy, proving that confidence weighting systematically penalizes valid multi-step derivations in GRPO; conducted five-way matched ablation study on GSM8K/MATH demonstrating 0.00% Pass@1 gain over length-controlled baselines.*

2. **AdaptiveReplica: Dynamic Quorum Adaptation and Failure-Aware Replica Selection in Distributed Consensus**  
   **Sham Satish Thakare**, **Yuri Shelke** (Distinguished Engineer, Capital One)  
   *Under Review at IEEE Transactions on Artificial Intelligence (IEEE TAI), 2024. Capital One Systems Research.*  
   [Code (C++20): https://github.com/shamddd/quorumshift]  
   *Formulated online latency profiling algorithms in C++20 Raft consensus clusters that dynamically re-weight quorums, proving non-empty intersection invariants ($\mathcal{Q}_i \cap \mathcal{Q}_j \neq \emptyset$) under bounded clock drift $\Delta$, eliminating p99 tail latency degradation under asymmetric network jitter and partitions.*

3. **recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning**  
   **Sham Satish Thakare**  
   *Under Review at 11th IEEE Special Session on Machine Learning on Big Data (IEEE BigData), 2024.*  
   [PDF: https://shamddd.github.io/shamthakare.github.io/pdfs/recovery-eval.pdf] · [Code: https://github.com/shamddd/recovery_eval]  
   *Formulates state-contrast continuation evaluation protocol ($D_{\text{recovery}} = \mathbb{E}[\Delta_{\text{recovery}}] - \mathbb{E}[\Delta_{\text{control}}]$) isolating true error recovery from baseline generative capacity under frozen structural covariates.*

4. **MediRush-SafeAgent: Layered Runtime Enforcement for Healthcare-Commerce LLM Tool Execution**  
   **Sham Satish Thakare**  
   *In Peer Review at Intelligence-Based Medicine (Elsevier) & SSRN Preprint (ID: 7446543), 2024.*  
   [SSRN: http://ssrn.com/abstract=7446543] · [Code: https://github.com/shamddd/medirush-safeagent]  
   *Formulated multi-stage deterministic runtime policy interception and out-of-band schema validation barriers that decouple proposed calls from system mutations, guaranteeing 100% safe task completion and 0% policy violations.*

---

## Preprints & Working Papers

5. **StateShift: Tracking State-Dependent Reasoning Recovery Dynamics in Neural Sequence Models**  
   **Sham Satish Thakare** | *Technical Report & Preprint, 2024.*  
   [PDF: https://shamddd.github.io/shamthakare.github.io/pdfs/stateshift.pdf] · [Code: https://github.com/shamddd/stateshift]

6. **Amortized Intervention Frontiers for Language-Model Reasoning: When Does Training Beat Search?**  
   **Sham Satish Thakare** | *Working Paper in Preparation for Transactions on Machine Learning Research (TMLR), 2024.*  
   [Code: https://github.com/shamddd/submission_package]

7. **Predicting Reinforcement-Learning Plasticity of Intermediate Language-Model Checkpoints**  
   **Sham Satish Thakare** | *Technical Report & Diagnostic Probing Suite, 2024.*  
   [Code: https://github.com/shamddd/adaptive-rl-forge]

---

## Theoretical & Methodological Contributions

* **Credit Assignment Geometry in Reasoning RLVR (Mathematical Machine Learning)**: Derived analytical bounds for token predictive entropy $H(Y_t \mid Y_{<t}, X)$ across autoregressive mathematical reasoning trajectories. Proved that predictive entropy exhibits significant collinearity with derivation sequence length ($r = +0.486, p < 10^{-6}$), demonstrating that heuristic uncertainty-weighting acts as an unintended length penalty and systematically degrades credit assignment on complex proofs. Executed a five-way matched ablation study on GSM8K/MATH establishing $0.00\%$ Pass@1 gain over length-controlled baselines ($d = 0.00$), establishing statistical bounds on reward proxy reliability.
* **Quorum Overlap Invariants in Asymmetric State-Machines (Distributed Systems Theory)**: Formulated online latency profiling algorithms in C++20 Raft consensus clusters that dynamically re-weight voting quorums. Proved that under bounded clock skew $\Delta$ and asynchronous message delivery, the dynamically adapted quorums preserve non-empty intersection invariants $\mathcal{Q}_i \cap \mathcal{Q}_j \neq \emptyset$, guaranteeing linearizability across arbitrary network partitions. Released open-source high-throughput C++20 library `quorumshift` with reproducible fault-injection test harnesses and lock-free execution queues.
* **Quantum Information & Computational Foundations (Quantum Science & Computing)**: Investigated density matrix formalism ($\rho \succeq 0, \text{Tr}(\rho)=1$), von Neumann entropy $S(\rho) = -\text{Tr}(\rho \log \rho)$, and quantum state tomography protocols for multi-qubit systems. Analyzed quantum computational complexity class relationships ($\text{BPP} \subseteq \text{BQP} \subseteq \text{PSPACE}$), query complexity bounds, and Grover search dynamics over structured database Hamiltonians. Formulated error mitigation bounds for quantum circuit compilation in Qiskit and Cirq, studying stabilizer code projections and tensor network contraction methods for simulating distributed quantum state transitions.
* **Counterfactual State-Contrast Continuation Evaluation (Statistical Evaluation Methodology)**: Formulated the state-contrast continuation evaluation metric ($D_{\text{recovery}} = \mathbb{E}[\Delta_{\text{recovery}}] - \mathbb{E}[\Delta_{\text{control}}]$) in `recovery_eval`, establishing counterfactual controls that isolate true self-correction from generative capacity under frozen structural covariates.

---

## Academic Leadership, Teaching & Service

* **President, Social Volunteer Club**, APCOER Pune (*2023 – 2024*): Elected student head of university community outreach; directed educational mentorship in quantitative and digital skills for 200+ underprivileged high-school students, organized city-wide blood donation drives, and led campus sustainability campaigns.
* **Teaching Assistant**, APCOER Pune (*2023 – 2024*): Conducted weekly recitation sessions, algorithmic proof walkthroughs (graph traversal, dynamic programming, complexity classes), and PyTorch implementation labs for 120+ undergraduate engineering students in *Data Structures, Algorithms, and Foundations of Machine Learning*.

---

## Technical Skills & Foundations

* **Mathematics & Theoretical Foundations**: Linear Algebra (Spectral Decomposition, SVD), Probability Theory, Stochastic Processes, Convex Optimization (KKT Conditions, Subgradient Methods), Discrete Mathematics, Graph Theory, Algorithmic Complexity.
* **Quantum Computing & Information**: Quantum Gates & Circuits, Unitary Operators, Density Matrix Formalism, Quantum Algorithms (Shor, Grover, Quantum Walks), Qiskit, Cirq.
* **Machine Learning & AI**: Reinforcement Learning (PPO, GRPO, RLVR), Transformer Architectures, Statistical Learning Theory, PyTorch, JAX, Hugging Face Transformers, NumPy, SciPy.
* **Systems Programming & Infrastructure**: C++ (C++20 Multithreading, Lock-free Primitives), Distributed Consensus (Raft), POSIX, Linux Kernel Internals, OpenTelemetry, Git, Docker, LaTeX.

---

## Academic References

* **Yuri Shelke** · Distinguished Engineer, Capital One  
  *Relationship*: Systems Research Mentor & Co-author (Distributed Systems & Consensus) | Contact available upon request
* **Prof. Sagar Gawande** · Professor & Head of Department, APCOER Pune (SPPU)  
  *Relationship*: Undergraduate Research Advisor (AI & Machine Learning) | Contact available upon request
* **Prof. Sunil Thakare** · Senior Faculty & Academic Mentor, APCOER Pune (SPPU)  
  *Relationship*: Mathematics & Foundations Mentor | Contact available upon request
