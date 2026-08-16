# Sham Satish Thakare

**AI/ML Researcher & Research Software Engineer**  
Pune, Maharashtra, India • [GitHub](https://github.com/shamddd) • [Email](mailto:shamthakare3000@gmail.com)

I work on large language model evaluation, agentic AI systems, reinforcement-learning-inspired reasoning diagnostics, AI safety/reliability, and reproducible ML infrastructure. My current research focuses on state-matched, provenance-aware evaluation of recovery behavior in language-model reasoning.

---

## 🔬 Current Research Manuscript

### `recovery_eval`

**Title:** *recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning*  
**Venue:** IEEE International Conference on Big Data (IEEE BigData 2026)  
**Submission ID:** `BigD497`  
**Associated Session:** 11th IEEE Special Session on Machine Learning on Big Data (MLBD 2026), Session #2  
**Status:** **Submitted / Under Review** (Awaiting conference decision)  
**Repository:** [`recovery_eval`](https://github.com/shamddd/recovery_eval)

* **Key Focus**: Distinguishing true error-recovery capability from general baseline continuation fluency gains in reasoning LLMs.
* **Methodology**: Combines verifier-defined recovery states, prospective covariate matching ($d \le 0.25$), append-only cryptographic exposure governance, and primitive neural rollout provenance.
* **Empirical Demonstration**: Evaluated on 400 genuine neural continuations from `Qwen2.5-Math-1.5B` Base vs. Instruct across 20 GSM8K evaluation problems. Measured matched recovery-specific contrast $D_{\text{recovery}} = -0.110$ with a 95% descriptive bootstrap interval of $[-0.240, +0.030]$.
* **Finding**: Under the evaluated state-matched protocol, we did not observe evidence of a recovery-specific advantage for the Instruct checkpoint over the Base checkpoint.

---

## 📄 Research Manuscripts

| Manuscript Title | Targeted Venue / Track | Current Status | Code Repository |
| :--- | :--- | :---: | :---: |
| **recovery_eval: State-Matched and Provenance-Aware Evaluation of Recovery Behavior in Language-Model Reasoning** | IEEE BigData 2026 / MLBD 2026 | Submitted (`BigD497`) | [`recovery_eval`](https://github.com/shamddd/recovery_eval) |
| **AdaptiveReplica: Dynamic Quorum Adaptation and Failure-Aware Replica Selection in Distributed Consensus** | IEEE TAI | Submitted | [`quorumshift`](https://github.com/shamddd/quorumshift) |

---

## 🛠️ Featured Research & Engineering Projects

### 1. [`recovery_eval`](https://github.com/shamddd/recovery_eval) — State-Matched LLM Reasoning Evaluation Infrastructure
State-matched, provenance-aware framework for evaluating recovery behavior in language-model reasoning.
* **Focus**: Model evaluation, data-centric AI, verifier-guided search, reproducibility.
* **Features**: Verifier-defined recovery states, prospective covariate matching, append-only event ledger, primitive BPE rollout provenance, 100% independent analysis reconstruction.
* **Stack**: Python 3.11+, PyTorch, HuggingFace Transformers, Pytest, Tectonic TeX.

### 2. [`agentguard-final`](https://github.com/shamddd/agentguard-final) — AI Agent Reliability & Security Observability Platform
AI agent reliability and security platform for monitoring tool execution, threat events, policy violations, and operational behavior in agentic systems.
* **Focus**: Agentic AI, AI safety & reliability, tool-execution monitoring, LLM security observability.
* **Features**: Real-time policy enforcement engine, tool execution auditing, multi-agent event tracing, interactive security dashboard.
* **Stack**: Python, FastAPI, Next.js, TypeScript, Tailwind CSS, Docker, PostgreSQL.

### 3. [`medirush`](https://github.com/shamddd/medirush) — Hyperlocal Healthcare-Commerce & Logistics Platform
Full-stack hyperlocal healthcare-commerce platform exploring fast medicine delivery, pharmacy workflows, safety-aware AI assistance, and production web/API infrastructure.
* **Focus**: Full-stack web architecture, healthcare APIs, high-throughput backend services.
* **Features**: Real-time order tracking, inventory management, secure authentication, Redis caching, Docker containerization, CI/CD pipeline.
* **Stack**: Next.js, React, TypeScript, FastAPI, PostgreSQL, Redis, Docker, GitHub Actions.

### 4. [`quorumshift`](https://github.com/shamddd/quorumshift) — AdaptiveReplica Distributed Consensus Engine
Research-oriented distributed-systems implementation exploring dynamic quorum adaptation and failure-aware replica selection in Raft-based consensus.
* **Focus**: Distributed systems, consensus protocols, fault tolerance, p99 latency optimization.
* **Features**: Dynamic vote-weight adaptation, asymmetric degradation monitoring, joint-consensus transitions.
* **Stack**: Python, Go, Pytest, Docker.

### 5. [`adaptive-rl-forge`](https://github.com/shamddd/adaptive-rl-forge) — Reinforcement-Learning Experiment Infrastructure
Research tooling for reinforcement-learning experimentation, scheduling, representation diagnostics, and reproducible evaluation workflows.
* **Focus**: RL infrastructure, reward plasticity, diagnostic probing, reproducible benchmarks.
* **Features**: Automated experiment tracking, policy gradient utilities, seed invariance verification.
* **Stack**: Python, PyTorch, Ray/RLlib, Pytest.

### 6. [`tracemind`](https://github.com/shamddd/tracemind) — Graph-Constrained Causal Reasoning for Microservice AIOps
Graph-constrained causal reasoning engine fusing OpenTelemetry traces, metrics, and service dependency graphs for root-cause localization.
* **Focus**: AIOps, graph algorithms, causal observability, microservice diagnostics.
* **Features**: Topological causal walks over Service Dependency Graphs, hallucination-free RCA.
* **Stack**: Python, NetworkX, OpenTelemetry, Pytest.

---

## 🎯 Research Interests

* **Large Language Model Evaluation**: State-matched benchmarks, diagnostic probing, error-recovery verification, counterfactual prompt evaluation.
* **Agentic AI & Tool Safety**: Multi-agent orchestration, tool execution governance, policy enforcement, LLM security observability.
* **Reinforcement Learning & Reasoning**: Policy gradient methods, process supervision, test-time compute scaling, representation geometry.
* **AI Safety & Reliability**: Robustness testing, failure mode taxonomy, dataset exposure prevention, reproducible evidence ledgers.
* **Reproducible ML Systems**: Data-centric AI pipelines, deterministic execution, hardware-bound benchmarks, open scientific software.

---

## 💻 Technical Skills

* **AI / ML**: Python · PyTorch · HuggingFace Transformers · Scikit-learn · Reinforcement Learning · LLM Evaluation · Agentic AI
* **LLM / Agent Systems**: HuggingFace · Tool-using Agents · RAG · Multi-Agent Orchestration · Evaluation Pipelines · Safety & Reliability
* **Backend & Systems**: FastAPI · Flask · REST APIs · PostgreSQL · MySQL · Redis · Docker · CI/CD Pipelines
* **Frontend**: React · Next.js · TypeScript · Tailwind CSS
* **Data & Analytics**: Pandas · NumPy · SciPy · Matplotlib · Seaborn · SQL

---

## 🛡️ Research Integrity & Transparency

I prioritize reproducibility and scientific integrity across all research endeavors:
* **Evidence Provenance**: All active empirical results derive from verifiable raw outputs, cryptographic hashes, and locked pre-execution protocols.
* **Scientific Transparency**: Retraction notices and forensic audit trails are permanently preserved for historical auditability (e.g., exploratory simulation retractions).
* **Open Software**: All evaluation frameworks include automated test suites (`pytest`), single-command reproduction scripts, and complete environment manifests.

---

## ✉️ Connect

* **Email**: [`shamthakare3000@gmail.com`](mailto:shamthakare3000@gmail.com)
* **GitHub**: [`github.com/shamddd`](https://github.com/shamddd)
* **Location**: Pune, Maharashtra, India
