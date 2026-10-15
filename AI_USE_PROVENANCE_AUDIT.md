# AI Use Provenance Audit

**Author**: Sham Satish Thakare  
**Target Paper**: *Estimator Validity, Reasoning Complexity, and Negative-Control Protocols for Uncertainty-Weighted Credit Assignment in RLVR Post-Training*  
**Research Essay**: *When Confidence Proxies Confound Reasoning Complexity*  
**Last Audit Date**: August 21, 2026  

---

## 1. Human-Originated Scientific Work

The foundational scientific contributions, hypotheses, experimental designs, and raw empirical data are 100% human-originated by Sham Satish Thakare:

- **Research Formulation**: Identification of potential length confounding in token predictive entropy for RLVR.
- **Experimental Design**: 5-way controlled RL post-training protocol ($K=4/8$ rollouts, 256-token budget, 5 control methods).
- **Compute Graph Audit**: Audit of `Qwen2ForCausalLM` discovering 0 active `nn.Dropout` modules and $\text{Var}(\log P) = 0.0$.
- **Raw Data & Logs**: Experimental execution outputs (`GSM8K`, $N=100$ prompt clusters; RLVR training across $N=3$ seeds).
- **Primary Manuscript Draft**: Original LaTeX text and Word manuscript authored by Sham Satish Thakare.

---

## 2. Provenance Matrix

| Artifact Component | AI System | Type of Assistance | Human Verification | Manuscript Disclosure Required? |
|---|---|---|---|---|
| **Core Research Question** | None (Human) | Original scientific hypothesis formulation | Author | No |
| **Experimental Code (`ear_grpo_reasoning`)** | Gemini / Antigravity Agent | Code structuring, testing scripts, figure generation | Author verified & tested | No |
| **Raw Result Calculations ($r, \text{AUROC}, d$)** | Python / SciPy Scripts | Deterministic statistical computation | Author verified against raw outputs | No |
| **Manuscript Text (LaTeX/PDF)** | None (Human) | Author original text | Author | Disclosure included in Title Page per IEEE guidelines |
| **Research Blog HTML (`writing/.../index.html`)** | Gemini / Antigravity Agent | Responsive Web layout, KaTeX markup, SVG chart generation | Author verified | N/A (Blog publication artifact) |
| **SVG Diagrams (`hero-concept.svg`, etc.)** | Python Script (`generate_figures.py`) | Programmatic SVG rendering from JSON data | Author verified | N/A |

---

## 3. Policy Certification

This audit certifies that all primary scientific findings, data points, and hypotheses represent genuine human research by Sham Satish Thakare. AI systems were used solely as engineering and communication tools for web layout construction, figure scripting, and formatting verification.
