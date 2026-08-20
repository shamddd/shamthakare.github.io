# MANUSCRIPT FIGURE PLAN & SPECIFICATIONS

**Date**: August 16, 2026  
**Auditor**: Graphics & Visualization Lead  

---

## FIGURE SPECIFICATIONS (FIGURES 1–6)

* **FIGURE 1: Conceptual Deployment Cost Framework**
  - Schematic plot of total cost $C_{	ext{total}}(a, Q) = C_{	ext{train}}(a) + Q \cdot C_{	ext{inference}}(a)$ vs future query volume $Q$.
  - Demarcates training offset $C_{	ext{train}}$ and break-even crossover $Q^*_{	ext{frontier}}$.

* **FIGURE 2: Utility-Cost Pareto Envelopes**
  - Accuracy vs Total FLOP Cost curves for $A_0$ (Base), $A_1$ (Best-of-$N$), $A_2$ (LoRA-RLVR), and $A_3$ (Full RLVR).
  - Highlights Pareto dominance transition across query regimes.

* **FIGURE 3: Intervention Phase Diagram $a^*(Q, d)$**
  - 2D heatmap in $(Q, d)$ space showing preferred intervention regions across query volume $Q \in [1, 10^4]$ and compositional depth $d \in [3, 7]$.

* **FIGURE 4: Per-Family IID vs OOD $Q^*_{	ext{frontier}}$**
  - Grouped bar chart comparing $Q^*_{	ext{IID}}$ vs $Q^*_{	ext{OOD-Length}}$ for SmolLM2, Qwen2.5, and TinyLlama.

* **FIGURE 5: Dataset A vs Dataset B Sensitivity Analysis**
  - Dual-panel comparison showing $R_f$ stability between Dataset A ($N=6$ runs) and Dataset B ($N=5$ runs, pre-ceiling compliant).

* **FIGURE 6: Descriptive Mechanism Shift Breakdown**
  - Stacked bar chart showing non-causal mechanism decomposition: base probability collapse (65%), sequence length growth (15%), verifier cost (10%), and RLVR generalization (10%).
