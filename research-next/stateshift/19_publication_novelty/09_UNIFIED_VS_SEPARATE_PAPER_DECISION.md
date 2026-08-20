# PHASE 3A — UNIFIED VS SEPARATE PAPER ARCHITECTURE DECISION

**Milestone**: Manuscript Scope & Architecture Decision  

---

## 1. Comparative Architecture Evaluation

* **Option A: Unified StateShift Paper**: Combines Study A (controlled perturbation, $N=454$) and Study B (natural post-error recovery, $N=200, K=16, 3,200$ rollouts) into a single cohesive manuscript.
* **Option B: Primary Paper + Supplementary Pilot**: Study A in main body; Study B in Supplementary Material.
* **Option C: Two Separate Papers**: Split into two distinct publications.

---

## 2. Decision & Justification

$$\mathbf{SELECTED\ ARCHITECTURE:\ OPTION\ A\ (ONE\ UNIFIED\ STATESHIFT\ PAPER)}$$

* **Justification**: Controlled perturbation (Study A) establishes that post-training gains are state-selective ($\Gamma_{256} = +0.1176$). Natural recovery (Study B) confirms that this capability operates in unperturbed rollouts ($\text{NRR}=30.93\%$). Combining them presents a unified, highly defensible story that maximizes publication impact for top-tier venues (NeurIPS / ICML / ICLR).

*Signed by Publication Strategist & Technical Editor*
