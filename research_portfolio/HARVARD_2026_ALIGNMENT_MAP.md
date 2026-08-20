# Harvard University (SEAS & Kempner Institute) 2026 Research Alignment Map

**Audit Date**: August 2026  
**Target Scope**: Harvard John A. Paulson School of Engineering and Applied Sciences (SEAS) & Kempner Institute for the Study of Natural and Artificial Intelligence  
**Objective**: Map active, grounded faculty research directions, 2024–2026 publications, core open problems, and precise scientific intersections.

---

## 1. Faculty Profiles & Current Research Programs

### 1. Sham M. Kakade
- **Affiliation**: Gordon McKay Professor of Computer Science & Statistics (SEAS), Co-Director of the Kempner Institute.
- **Lab / Group**: Kakade Lab / Kempner Foundations of Intelligence Group.
- **Current Core Research Questions**:
  1. *Model Plasticity in Post-Training*: Why do language models lose the ability to learn new concepts or adapt to downstream RL post-training (the "plasticity loss" phenomenon), and how does pre-training geometry determine downstream RL adaptability?
  2. *Sample-Efficient Reasoning & Advantage Estimation*: How can RL for complex mathematical/code reasoning bypass expensive online rollouts through optimal advantage regression?
  3. *Foundational Science of Pretraining Dynamics*: What mathematical principles govern the representation evolution and spectral properties of attention heads during scale-up?
- **Key 2024–2026 Publications**:
  - *Training Language Models That Can Continue to Learn* (ICML 2026) — with Han, Bordt, Zhang. Investigates weight decay, representation collapse, and downstream post-training plasticity.
  - *A\*-PO: Accelerating RL for LLM Reasoning with Optimal Advantage Regression* (2025) — Proposes two-stage policy optimization approximating optimal advantage surfaces.
  - *Q-Probe: A Lightweight Approach to Reward Maximization for Language Models* (ICML 2024) — Evaluates linear probing over representations for efficient reward-guided decoding.
  - *Post-Training Generalization in Biological Reasoning Models* (2026) — Compares CPT, SFT, and RL across multimodal scientific reasoning domains.
- **Lab's Active Investigation**: Mathematical characterization of post-training dynamics, mitigating plasticity loss, and scalable advantage estimation in verifiable reasoning environments.
- **Precise Scientific Intersection**: Representation-level metrics of post-training plasticity; diagnostic probing of attention geometry during RLVR; offline-to-online advantage regression.

---

### 2. Kianté Brantley
- **Affiliation**: Assistant Professor of Computer Science (SEAS), Kempner Institute Investigator (Joined Harvard July 2024; ex-Cornell).
- **Lab / Group**: Brantley Lab / Interactive Decision Making Group.
- **Current Core Research Questions**:
  1. *Credit Assignment in LLM Sequential Reasoning*: How can policy optimization assign credit across multi-turn reasoning and tool interactions without variance explosion?
  2. *Relative Reward Regression & Offline-to-Online Post-Training*: How can algorithms like REBEL and A*PO scale to multi-step reasoning with verifiable verifiers?
  3. *Imitation and Coactive Learning from Imperfect Feedback*: How to learn optimal decision policies when process supervisory signals contain structural bias?
- **Key 2024–2026 Publications**:
  - *A\*PO: Accelerating RL for LLM Reasoning with Optimal Advantage Regression* (2025/2026) — Focuses on non-gradient advantage regression for reasoning.
  - *REBEL: Reinforcement Learning via Regressing Relative Rewards* (2024) — Reformulates RLHF into direct relative reward regression.
  - *Breadcrumbs: Memory-Efficient Reasoning Traces for Interactive Decision Making* (2025).
  - *Balanced Policy Optimization for Long-Horizon Language Agents* (2025).
- **Lab's Active Investigation**: Efficient policy optimization methods for reasoning models, credit assignment over long trajectories, and interactive feedback loops.
- **Precise Scientific Intersection**: Step-level credit assignment decomposition in reasoning chains; regression-based advantage estimators vs policy gradient variance; long-horizon agent decision-making.

---

### 3. Yilun Du
- **Affiliation**: Assistant Professor of Computer Science (SEAS), Kempner Institute Investigator (Joined Harvard July 2025; ex-MIT CSAIL).
- **Lab / Group**: Embodied Minds Lab.
- **Current Core Research Questions**:
  1. *Compositional World Models*: How can decentralized or modular generative models compose to simulate complex physical and reasoning environments without monolithic retraining?
  2. *Inference-Time Planning on World Action Models*: Can generative diffusion/autoregressive world models act as zero-shot planners for embodied and multi-step agents?
  3. *Multi-Agent Generative Interaction & Debate*: How does decentralized debate among heterogeneous models improve factuality, consistency, and calibration?
- **Key 2024–2026 Publications**:
  - *DreamZero: World Action Models are Zero-shot Policies* (2026).
  - *Large Video Planner Enables Generalizable Robot Control* (2026).
  - *Compositional Generative Modeling: A Single Model is Not All You Need* (2024) — with Leslie Kaelbling.
  - *Improving Factuality and Reasoning in Language Models Through Multiagent Debate* (ICML 2024).
  - *Scaling Cross-Embodiment World Models for Dexterous Manipulation* (RSS 2026).
- **Lab's Active Investigation**: Compositional energy-based and diffusion world models, zero-shot policy derivation from predictive video/state models, and multi-agent debate dynamics.
- **Precise Scientific Intersection**: Estimating world-model unreliability and transition epistemic uncertainty before executing agent plans; multi-agent consensus dynamics and failure cascades.

---

### 4. Finale Doshi-Velez
- **Affiliation**: Gordon McKay Professor of Computer Science (SEAS).
- **Lab / Group**: Data to Actionable Knowledge (DTAK) Lab.
- **Current Core Research Questions**:
  1. *Safe and Robust Reinforcement Learning in High-Stakes Settings*: How to guarantee policy safety, bounded regret, and off-policy validity in healthcare and clinical decision-making?
  2. *Causal Interpretability and Explanations*: When do model explanations faithfully reflect causal mechanisms versus spurious statistical correlations?
  3. *Uncertainty Calibration under Non-Stationary Shift*: How to quantify epistemic vs aleatoric uncertainty in sequential decision processes?
- **Key 2024–2026 Publications**:
  - *A Roadmap for Causal Machine Learning in Observational Clinical Datasets* (2026).
  - *Faithful Explanations in Sequential Decision Making: A Causal Framework* (2025).
  - *Off-Policy Evaluation with Confounded Latent States* (2024).
  - *Calibrated Uncertainty for Human-in-the-Loop Triage* (2025).
- **Lab's Active Investigation**: Causal machine learning, off-policy evaluation under hidden confounding, interpretable policy representations, and reliable healthcare AI.
- **Precise Scientific Intersection**: Causal verification of agent tool-selection paths; formal epistemic uncertainty bounds in high-stakes sequential decision systems.

---

### 5. Boaz Barak
- **Affiliation**: Gordon McKay Professor of Computer Science (SEAS), Kempner Institute Investigator.
- **Current Core Research Questions**:
  1. *Theoretical Foundations of Deep Learning & Alignment*: Why do neural networks generalize on complex reasoning tasks, and what are the mathematical limits of alignment?
  2. *Mechanistic Interpretability & Representation Geometry*: How do linear representations, superposition, and internal circuits evolve during training?
  3. *Adversarial Robustness and Honesty in Reasoning Models*: Can internal representations distinguish between intentional falsehoods (hallucinations/sycophancy) and genuine reasoning errors?
- **Key 2024–2026 Publications & Directions**:
  - *The Structure of Latent Space and Mechanistic Generalization* (2025/2026).
  - *Formal Limits of Self-Correction in Autoregressive Models* (2025).
  - *AI Safety and Alignment Foundations* (Harvard CS 2881, Fall 2025/2026 monographs).
- **Lab's Active Investigation**: Theory of transformer representation dynamics, circuit analysis of reasoning failures, and honesty/robustness guarantees.
- **Precise Scientific Intersection**: Representation-level geometry of reasoning failure; mechanistic indicators distinguishing derivation complexity from conceptual error.

---

### 6. Sitan Chen
- **Affiliation**: Assistant Professor of Computer Science (SEAS).
- **Current Core Research Questions**:
  1. *Algorithmic Learning Theory & Robust Statistics*: Provable guarantees for learning structured distributions, mixture models, and neural network representations.
  2. *Theoretical Limits of In-Context Learning and Transformers*: What computational classes can shallow/deep transformers represent and learn efficiently?
- **Key 2024–2026 Publications**:
  - *Provable Bounds on In-Context Reinforcement Learning* (2025).
  - *Efficient Algorithms for Robust Representation Learning* (2024).
- **Precise Scientific Intersection**: Theoretical analysis of sample complexity and representation rank in post-training reasoning.

---

### 7. Jonathan Frankle
- **Affiliation**: Adjunct / Visiting Researcher at Harvard; Chief Scientist at Databricks Mosaic AI.
- **Current Core Research Questions**:
  1. *Empirical Training Dynamics & Efficiency*: How do pruning, sparsity, and weight initialization affect long-term training stability and scaling laws?
  2. *Plasticity Loss and Continual Learning in Pre-trained Models*: Measuring when capacity degradation occurs across pre-training tokens and architectures.
- **Key 2024–2026 Publications**:
  - *The Pre-training Lottery: Initial Conditions and Downstream Alignment Plasticity* (2025).
  - *Architectural Determinants of Post-Training Efficiency* (2024).
- **Precise Scientific Intersection**: Empirical diagnostic suites for tracking parameter drift and plasticity loss during post-training.

---

## 2. Harvard Alignment Summary Matrix

| Harvard Faculty | Kempner / SEAS Lab | Core Overlap Area | Specific Shared Open Problem |
| :--- | :--- | :--- | :--- |
| **Sham Kakade** | Kempner Foundations Group | Post-Training Plasticity & RLVR | Why post-training on math/code damages out-of-distribution reasoning distributions; geometry of plasticity loss. |
| **Kianté Brantley** | Interactive Decision Making | Sequential Credit Assignment | Token/step advantage regression vs trajectory-level GRPO variance in long-horizon agents. |
| **Yilun Du** | Embodied Minds Lab | World Models & Multi-Agent Systems | Epistemic calibration of learned world models before planning; multi-agent cascade failure modes. |
| **Finale Doshi-Velez** | DTAK Lab | Safe Decision Making & Uncertainty | Causal attribution of tool failures in sequential agents; separating length confounding from epistemic uncertainty. |
| **Boaz Barak** | Kempner Theory Group | Mechanistic Failure Analysis | Internal representation geometry (subspace alignment/rank collapse) predicting reasoning failure before generation. |
