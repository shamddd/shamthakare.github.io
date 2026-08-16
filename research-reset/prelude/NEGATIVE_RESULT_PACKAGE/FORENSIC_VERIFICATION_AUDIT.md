# FORENSIC RESEARCH AUDIT: SHAM KAKADE RESEARCH MAP & PRELUDE CLAIMS

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent (Self-Audit Protocol)  
**Target Scope**: Forensic verification of all literature claims, citations, experimental provenance, and novelty statements in `ACTIVE_RESEARCH_COLLISION_MAP.md` and previous alignment reports.

---

## 1. AUDIT OBJECTIVE & METHODOLOGY

The goal of this audit is to conduct an uncompromising, adversarial forensic review of our own previous research claims regarding:
1. The publication record, author affiliations, venues, and findings of Prof. Sham Kakade and the Harvard ML Foundations Group / Kempner Institute (2024–2026).
2. The empirical provenance of previously cited reproduction benchmarks.
3. The validity, novelty, and theoretical boundaries of the proposed **PRELUDE** (Pre-Intervention Learning Utility Estimation) research agenda.

Every claim is audited against primary sources (official proceedings, OpenReview, arXiv, Harvard/Kempner repositories, author websites). All unverified assertions, placeholder citations, and ungrounded experimental numbers are systematically identified, cataloged, and excised from the scientific record.

---

## 2. SUMMARY OF FORENSIC FINDINGS

### A. Literature & Citation Integrity
* **Total Papers Audited**: 21
* **Verified Real Papers**: 20
* **Flagged / Unverified Papers**: 1
  * *Discrepancy Catch*: `Paper 20` (*"Accelerating RL for LLM Reasoning with Optimal Advantage Regression"* attributed to Kianté Brantley and Sham Kakade with placeholder `2602.xxxxx`) was an **unverified synthesis / candidate title**. While both authors are affiliated with Harvard/Kempner and active in RL theory, no publication with this title exists.
  * *Correction*: Downgraded to `POSSIBLE HALLUCINATION / UNVERIFIED SYNTHESIS` and removed from the active citation ledger.
* **Placeholder Citations Resolved**: All placeholder arXiv identifiers (e.g., `2510.xxxxx`, `2601.xxxxx`, `2602.xxxxx`, `2607.xxxxx`) have been resolved to their verified identifiers:
  * *Prescriptive Scaling*: `arXiv:2602.15327` (ICML 2026 Oral)
  * *Weight Decay Improves Plasticity*: `arXiv:2602.11137`
  * *Full Gauss-Newton for LLMs*: `arXiv:2510.09378` (ICLR 2026)
  * *Seesaw Schedule*: `arXiv:2510.14717` (ICLR 2026)
  * *Anytime Pretraining*: `arXiv:2602.03702`
  * *Defense of Quadratic Model*: `arXiv:2607.21716`
  * *Schedule-Free & AdEMAMix*: `arXiv:2502.02431`
  * *LOTION*: `arXiv:2510.08757`
  * *Economy of Minds*: `arXiv:2606.02859`

### B. Experimental Provenance Audit
* **Claimed Numbers Audited**:
  - *"$\lambda_{\text{WD}}=0.0$ pretrain loss: 1.82, post-SFT accuracy: 18.4%; $\lambda_{\text{WD}}=0.1$ pretrain loss: 1.89, post-SFT accuracy: 29.2%"*
  - *"When probe AUROC on base representations >0.78, GRPO achieved +14.2% accuracy gain; when probe AUROC <0.60, GRPO collapsed into +0.8% gain"*
* **Workspace Provenance Check**: Inspection of `/Users/shamthakare/.gemini/antigravity/scratch/research/experiments/` revealed no raw stdout/stderr execution logs, no PyTorch checkpoints, and no random seed logs corresponding to these exact runs.
* **Forensic Verdict**: These numbers were **narrative illustrations / estimated projections**, not real-time executed empirical artifacts in the local workspace.
* **Sanitization Action**: All fabricated/unexecuted numerical values are **DELETED FROM THE SCIENTIFIC RECORD** and replaced with `PLANNED EXPERIMENT — RESULT NOT YET AVAILABLE`.

### C. Novelty & Semantic Collision Reset
* **Previous Overstated Claim**: *"PRELUDE is completely unaddressed, unique, and unprecedented."*
* **Forensic Finding**: Transferability estimation (LogME, TransRate, LEEP), task affinity (Task2Vec), zero-cost NAS proxies (SynFlow, SNIP), and learning curve extrapolation (Freeze-Thaw, AlphaRL) already study performance prediction from frozen representations or pilot signals in adjacent contexts.
* **Reset Position**: PRELUDE is a **candidate research hypothesis whose novelty remains under investigation**. The specific defensible subproblem is narrowed strictly to:
  $$\text{Predicting post-training reasoning improvement } \Delta_{\text{RLVR}}(M, D) \text{ using frozen-model geometric/probe diagnostics vs. a 1\% compute pilot baseline.}$$

---

## 3. AUDITED PAPER-BY-PAPER VERIFICATION TABLE

| ID | Title (Claimed vs Verified) | Verified Authors | arXiv ID | Venue / Status | Primary Source Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **P01** | Prescriptive Scaling Reveals the Evolution of Language Model Capabilities | H. Zhang, J. Jin, V. Syrgkanis, S. Kakade | 2602.15327 | ICML 2026 Oral | **VERIFIED** (OpenReview / arXiv) |
| **P02** | Echo Chamber: RL Post-training Amplifies Behaviors Learned in Pretraining | R. Zhao, A. Meterez, S. Kakade, C. Pehlevan, S. Jelassi, E. Malach | 2504.07912 | COLM 2025 | **VERIFIED** (OpenReview / arXiv) |
| **P03** | Weight Decay Improves Language Model Plasticity | T. Han, S. Bordt, H. Zhang, S. Kakade | 2602.11137 | arXiv (under review) | **VERIFIED** (OpenReview / arXiv) |
| **P04** | The Potential of Second-Order Optimization for LLMs: A Study with Full Gauss-Newton | N. Abreu, N. Vyas, S. Kakade, D. Morwani | 2510.09378 | ICLR 2026 | **VERIFIED** (OpenReview / arXiv) |
| **P05** | Seesaw: Accelerating Training by Balancing Learning Rate and Batch Size Scheduling | A. Meterez, D. Morwani, J. Wu, C. Oncescu, C. Pehlevan, S. Kakade | 2510.14717 | ICLR 2026 | **VERIFIED** (OpenReview / arXiv) |
| **P06** | Anytime Pretraining: Horizon-Free Learning-Rate Schedules with Weight Averaging | A. Meterez, P. A. Nair, D. Morwani, C. Pehlevan, S. Kakade | 2602.03702 | arXiv (COLM 2026 track) | **VERIFIED** (arXiv) |
| **P07** | SOAP: Improving and Stabilizing Shampoo using Adam for Language Modeling | N. Vyas, D. Morwani, R. Zhao, I. Shapira, D. Brandfonbrener, L. Janson, S. Kakade | 2409.11321 | ICLR 2025 | **VERIFIED** (OpenReview / arXiv) |
| **P08** | Q-Probe: A Lightweight Approach to Reward Maximization for Language Models | K. Li, S. Jelassi, H. Zhang, S. Kakade, M. Wattenberg, D. Brandfonbrener | 2402.04333 | ICML 2024 | **VERIFIED** (PMLR / arXiv) |
| **P09** | How Does Critical Batch Size Scale in Pre-training? | H. Zhang, D. Morwani, N. Vyas, J. Wu, D. Zou, U. Ghai, D. Foster, S. Kakade | 2410.18787 | ICLR 2025 | **VERIFIED** (OpenReview / arXiv) |
| **P10** | Deconstructing What Makes a Good Optimizer for Language Models | R. Zhao, D. Morwani, D. Brandfonbrener, N. Vyas, S. Kakade | 2407.07972 | ICLR 2025 | **VERIFIED** (OpenReview / arXiv) |
| **P11** | The Role of Sparsity for Length Generalization in Transformers | N. Golowich, S. Jelassi, D. Brandfonbrener, S. Kakade, E. Malach | 2502.04326 | ICML 2025 | **VERIFIED** (arXiv) |
| **P12** | Train for the Worst, Plan for the Best: Understanding Token Ordering in Masked Diffusions | J. Kim, Y. Du, S. Kakade | 2502.06742 | ICML 2025 (Outstanding Paper) | **VERIFIED** (PMLR / arXiv) |
| **P13** | Selective Underfitting in Diffusion Models | K. Song, J. Kim, S. Chen, Y. Du, S. Kakade, V. Sitzmann | 2506.07788 | NeurIPS 2025 | **VERIFIED** (OpenReview / arXiv) |
| **P14** | Random Scaling of Emergent Capabilities | R. Zhao, T. Qin, D. Alvarez-Melis, S. Kakade, N. Saphra | 2502.01633 | NeurIPS 2025 | **VERIFIED** (OpenReview / arXiv) |
| **P15** | A Defense of the Quadratic Model | A. Meterez, P. A. Nair, D. Morwani, C. Pehlevan, S. Kakade, A. Damian | 2607.21716 | arXiv Preprint | **VERIFIED** (arXiv) |
| **P16** | Connections between Schedule-Free Optimizers, AdEMAMix, and Accelerated SGD Variants | D. Morwani, N. Vyas, H. Zhang, S. Kakade | 2502.02431 | arXiv / OPT Workshop | **VERIFIED** (arXiv / OPT) |
| **P17** | A New Perspective on Shampoo's Preconditioner | D. Morwani, I. Shapira, N. Vyas, E. Malach, S. Kakade, L. Janson | 2406.17757 | ICLR 2025 | **VERIFIED** (OpenReview / arXiv) |
| **P18** | LOTION: Smoothing the Optimization Landscape for Quantized Training | M. Kwun, D. Morwani, H. Su, S. Gil, N. Anand, S. Kakade | 2510.08757 | NeurIPS/ICML 2026 track | **VERIFIED** (OpenReview / arXiv) |
| **P19** | Scaling laws in linear regression: Compute, parameters, and data | L. Lin, J. Wu, S. Kakade, P. L. Bartlett, J. D. Lee | 2406.08447 | NeurIPS 2024 | **VERIFIED** (OpenReview / arXiv) |
| **P20** | Economy of Minds: Emerging Multi-Agent Intelligence with Economic Interactions | G. Xu, Y. Du, S. Kakade, et al. | 2606.02859 | arXiv Preprint | **VERIFIED** (arXiv) |
| **P21** | Accelerating RL for LLM Reasoning with Optimal Advantage Regression | K. Brantley, S. Kakade | N/A (Placeholder 2602.xxxxx) | Unverified | **FLAGGED / REMOVED** |

---

## 4. SYSTEMIC CORRECTIONS IMPLEMENTED

1. **Purged Fictional Attributions**: Deleted all synthetic admissions verdicts and speculative faculty quotes.
2. **Purged Unexecuted Empirical Tables**: Cleaned all numerical claims across artifacts, ensuring only verified or cleanly planned experiments remain.
3. **Causal Vocabulary Rectification**: Replaced loose "causal downstream utility" phrasing with "counterfactual treatment delta under controlled intervention assignment" or "empirical intervention delta $\Delta(M, D, a)$".
4. **Action Space Narrowing**: Split complex heterogeneous action spaces into clean, isolated study designs ($A_{\text{train}}$ vs $A_{\text{infer}}$), focusing PRELUDE v1 strictly on predicting $\Delta_{\text{RLVR}}(M, D)$.
