# ACTIVE RESEARCH COLLISION MAP: HARVARD ML FOUNDATIONS & KEMPNER INSTITUTE (SHAM KAKADE LAB & AFFILIATES)

**Date**: August 2026  
**Target Lab / Alignment Focus**: Prof. Sham Kakade (Harvard University SEAS / Dept. of Statistics / Kempner Institute for the Study of Natural and Artificial Intelligence)  
**Co-Directors & Senior Collaborators**: Prof. David Alvarez-Melis, Prof. Boaz Barak, Prof. Cengiz Pehlevan, Prof. Yilun Du, Prof. Kianté Brantley, Prof. Sitan Chen, Prof. Lucas Janson  
**Key Postdocs & Active Graduate Students**: Alex Damian, Bingbin Liu, Nihal Nayak, Depen Morwani, Nikhil Vyas, Rosie Zhao, Hanlin Zhang, Alexandru Meterez, Jaeyeon Kim, Natalie Abreu, Chloe Su, Pranav Ajit Nair, Sarah Liaw, Rachit Bansal, Aayush Karan, Mary Letey, Clara Mohri, Roy Rinberg, Gustaf Ahdritz, Yang Hu, Anat Kleiman, Costin-Andrei Oncescu, Mujin Kwun, Samy Jelassi, David Brandfonbrener, Eran Malach, Tessa Han, Sebastian Bordt.

---

## 1. PURPOSE AND TAXONOMY OF RESEARCH COLLISIONS

This document serves as an exhaustive, rigorous collision audit designed to protect research independence. Proposing work that directly mimics or redundantly replicates ongoing projects within the Kakade group or the broader Kempner Institute is a fatal failure mode in graduate admissions and academic collaboration. True intellectual alignment requires identifying the exact frontier of their inquiries, understanding their methodological commitments, and formulating an orthogonal, complementary research program that tackles fundamental open problems.

### Collision Classification Taxonomy
1. **DIRECT COLLISION**: Exact problem, identical formulation, same intervention/hypothesis, overlapping evaluation benchmarks currently under active investigation by Kakade or immediate advisees. (MUST BE AVOIDED/ABANDONED).
2. **STRONG OVERLAP**: Substantial overlap in mathematical objective or experimental setup, but differing slightly in toolchain or parameterization. (HIGH RISK: Requires immediate refactoring/re-scoping).
3. **PARTIAL OVERLAP**: Shared foundational premise (e.g., training dynamics, representation geometry, scaling behavior), but addressing distinct downstream targets, architectures, or theoretical mechanisms. (ACCEPTABLE WITH EXPLICIT DIFFERENTIATION).
4. **ADJACENT**: Intellectually complementary; addresses a natural bottleneck or theoretical question directly spawned by their findings, but remains unaddressed by their current roadmap. (IDEAL COLLABORATIVE TARGET).
5. **DISTINCT**: Completely orthogonal methodology and target problem, retaining philosophical alignment with theoretical rigor and empirical reproducibility. (INDEPENDENT TRAJECTORY).

---

## 2. EXHAUSTIVE GROUP COLLISION MATRIX

| Research Area / Topic | Active Papers & Researchers (Kakade Lab / Kempner) | Collision Status | Collision Analysis & Differentiation Boundary |
| :--- | :--- | :--- | :--- |
| **RL Post-Training Dynamics & Pretraining Bias** | *Echo Chamber: RL Post-training Amplifies Behaviors Learned in Pretraining* (Zhao, Meterez, Kakade, Pehlevan, Jelassi, Malach, COLM 2025) | **STRONG OVERLAP** to **DIRECT COLLISION** if studying RL amplification of pretraining distributions. | Zhao et al. investigate how RL fine-tuning amplifies majority modes from pretraining distributions and induces scale-dependent biases. Any proposed project merely evaluating "what pretraining data does RL amplify" is a direct collision. **Differentiation**: Moving from *descriptive observation* of RL amplification to *pre-intervention decision rules* predicting when RLVR will collapse into mode-seeking vs discover novel solution paths. |
| **Model Plasticity & Weight Decay** | *Weight Decay Improves Language Model Plasticity* (Han, Bordt, Zhang, Kakade, arXiv/ICML 2026) | **DIRECT COLLISION** if proposing weight decay tuning for post-training adaptability. | Han et al. already proved that strong weight decay during pretraining induces linearly separable representations that preserve downstream plasticity (fine-tuning gain). **Differentiation**: Instead of tuning pretraining weight decay, develop training-free or pilot-based spectral/geometric estimators of a frozen checkpoint's remaining plasticity under specific target intervention types (SFT vs RLVR vs DPO). |
| **Prescriptive Scaling Laws & Capability Frontiers** | *Prescriptive Scaling Reveals the Evolution of Language Model Capabilities* (Zhang, Jin, Syrgkanis, Kakade, ICML 2026 Oral) | **STRONG OVERLAP** | Zhang et al. formalize smoothed quantile regression on pretraining FLOPs to predict frontier accuracy bounds across historical checkpoints (Proteus 2k). Proposing compute-to-benchmark capability curves is redundant. **Differentiation**: Prescriptive scaling models macro compute-to-accuracy limits; an orthogonal problem is *micro-level intervention routing*—predicting if *this specific checkpoint* at step $t$ requires continuous pretraining, SFT, or RLVR to cross a specific reasoning threshold. |
| **Second-Order Optimization & Preconditioning** | *The Potential of Second-Order Optimization for LLMs: A Study with Full Gauss-Newton* (Abreu, Vyas, Kakade, Morwani, ICLR 2026); *SOAP* (Vyas et al., 2024/2025); *Shampoo Preconditioner* (Morwani et al., 2024) | **DIRECT COLLISION** if designing second-order optimizers, Gauss-Newton approximations, or Adam-Shampoo hybrids. | The group (Natalie Abreu, Depen Morwani, Nikhil Vyas) is the world leader in second-order LLM optimization. Proposing an optimizer like SOAP, Adalayer, or Gauss-Newton variants is a direct collision. **Differentiation**: Do not propose optimization algorithms. Utilize their optimization insights (e.g., gradient eigenspace alignment, Hessian curvature) as diagnostic features for *predicting adaptation dynamics*. |
| **Learning Rate Schedules & Batch Size Balancing** | *Seesaw: Accelerating Training by Balancing LR and Batch Size* (Meterez, Morwani, Wu, Pehlevan, Kakade, ICLR 2026); *Anytime Pretraining* (Meterez et al., 2026); *Critical Batch Size Scaling* (Zhang, Morwani, Vyas, Kakade, ICLR 2025) | **STRONG OVERLAP** if modifying pretraining schedules or batch size curves. | Meterez, Morwani, and Pehlevan actively dominate horizon-free schedules, weight averaging, and critical batch size scaling laws. **Differentiation**: Leave pretraining scheduling to their group; focus on post-training budget allocation (intervention selection) given a fixed compute ceiling. |
| **Lightweight Reward Maximization & Probing** | *Q-Probe: A Lightweight Approach to Reward Maximization for Language Models* (Li, Jelassi, Zhang, Kakade, Wattenberg, Brandfonbrener, ICML 2024) | **PARTIAL OVERLAP** / **ADJACENT** | Li et al. train linear probes on residual stream representations of frozen models to reweight test-time candidate completions via rejection sampling. **Differentiation**: Q-Probe acts at test-time for sample re-ranking. An adjacent foundational question: Can internal residual stream representations and probe linear separability predict whether full-weight RL fine-tuning will succeed or suffer from policy degradation? |
| **Length Generalization & Transformer Circuit Sparsity** | *The Role of Sparsity for Length Generalization in Transformers* (Golowich, Jelassi, Brandfonbrener, Kakade, Malach, ICML 2025) | **PARTIAL OVERLAP** | Golowich et al. formalize predictive position coupling and sparse dependency graphs for length generalization. **Differentiation**: Focus on reasoning depth and verification capacity under compute constraints rather than positional token sparsity. |
| **Diffusion Token Ordering & Non-Autoregressive Planning** | *Train for the Worst, Plan for the Best: Understanding Token Ordering in Masked Diffusions* (Kim, Du, Kakade, ICML 2025 Outstanding Paper); *Selective Underfitting* (Song et al., 2025) | **PARTIAL OVERLAP** | Jaeyeon Kim and Yilun Du focus on non-autoregressive decoding paths and score extrapolation in diffusion models. **Differentiation**: Keep focus firmly anchored on autoregressive LLM reasoning, RLVR training dynamics, and post-training intervention utility. |
| **Multi-Agent Debate & Inter-Model Communication** | *Economy of Minds* (Xu, Du, Kakade, 2026); Decentralized coordination and emergent agent communication (Kempner / Du / Kakade) | **STRONG OVERLAP** if proposing generic LLM debate or multi-agent consensus protocols. | Yilun Du, Sham Kakade, and collaborators actively study multi-agent economic coordination, communication emergence, and decentralized planning. Proposing simple LLM-debate or prompt-based multi-agent consensus is both weak and colliding. **Differentiation**: Frame multi-agent or verifier-generator interactions strictly through formal decision theory, asymmetric verification complexity (NP-like verification vs generation), or rigorous test-time compute allocation bounds. |
| **Optimal Advantage Regression & Policy Optimization** | *Accelerating RL for LLM Reasoning with Optimal Advantage Regression* (Brantley, Kakade, 2025/2026) | **DIRECT COLLISION** if deriving new advantage regression / policy gradient loss objectives for reasoning. | Kianté Brantley and Sham Kakade work directly on policy gradient formulations and advantage estimators for reasoning LLMs. **Differentiation**: Treat policy optimization algorithms as black-box intervention operators $a \in \mathcal{A}$ within a meta-decision framework, evaluating their utility bounds rather than reinventing the base RL loss. |

---

## 3. IN-DEPTH THEMATIC INVESTIGATIONS & BOUNDARY CONDITIONS

### A. Adaptive Multi-Agent Debate & Inter-Model Communication
- **Current State in Kakade/Kempner Group**: Yilun Du, Boaz Barak, and Sham Kakade have been developing theoretical and empirical models of multi-agent coordination, token economies ("Economy of Minds"), and modular decentralized reasoning.
- **Collision Risk**: High if proposing multi-agent conversational debate, peer-review loops among LLMs, or heuristic voting.
- **Safe Boundary**: Do not propose heuristic multi-agent frameworks. If multi-agent concepts are used, they must be strictly formalized as decentralized game-theoretic equilibrium problems or asymmetric verifier-generator architectures where verifiers provide formal reward signals for RLVR.

### B. Test-Time Compute & Verification vs. Generation
- **Current State**: Kakade group explores test-time scaling through Q-probing (Li et al., 2024), token reordering in non-autoregressive architectures (Kim et al., 2025), and prescriptive scaling of reasoning capabilities (Zhang et al., 2026).
- **Collision Risk**: Medium to High if proposing naive Best-of-$N$ sampling or tree search without theoretical bounds.
- **Safe Boundary**: Investigate the fundamental *trade-off between training-time intervention (RLVR/SFT) and test-time compute (rejection sampling, search)*. Address the open question: For a given task distribution $D$ and compute budget $B$, what is the optimal partition between fine-tuning compute $C_{\text{train}}$ and search compute $C_{\text{test}}$?

### C. Training Plasticity & Representation Geometry
- **Current State**: Tessa Han, Sebastian Bordt, Hanlin Zhang, and Sham Kakade (2026) established that pretraining weight decay preserves plasticity by enforcing linear separability in representations.
- **Collision Risk**: High if exploring weight decay variations during pretraining.
- **Safe Boundary**: Take plasticity as a measurable *state observable* of a trained checkpoint. Investigate whether pre-intervention spectral properties (e.g., effective rank of covariance, gradient feature alignment, NTK condition number) can quantitatively predict the downstream utility $\Delta(M, D, a)$ of RLVR vs SFT without running full training.

---

## 4. STRATEGIC POSITIONING FOR FLAGSHIP PROJECT

To achieve maximum scientific depth while guaranteeing complete intellectual independence:
1. **Never copy an active pipeline**: Do not build another second-order optimizer, do not re-run weight decay pretraining grids, do not propose heuristic agent debate.
2. **Anchor in Decision Theory & Learning Theory**: Kakade’s foundational legacy (e.g., Natural Policy Gradient, conservative policy iteration, spectral methods, sample complexity) is rooted in clean mathematical formulation and rigorous statistical foundations.
3. **Formulate a Forward-Looking Problem**: Target **Pre-Intervention Learning Utility Estimation (PRELUDE)** as an **Optimal Decision Problem / Meta-Estimation Problem**—predicting the causal utility of training interventions before execution.
4. **Collision Status of PRELUDE**: **ADJACENT / DISTINCT**. It consumes insights from Kakade's training dynamics, plasticity, and scaling laws, but formulates an entirely unaddressed meta-level scientific question: *Can the value of a learning intervention be estimated prior to paying its computational cost?*

---
*Verified against primary literature from Harvard ML Foundations, Kempner Institute, ICML, ICLR, NeurIPS, COLM, and OpenReview (2024–2026).*
