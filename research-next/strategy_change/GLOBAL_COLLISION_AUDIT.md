# GLOBAL LITERATURE COLLISION AUDIT & PRIOR ART BOUNDARIES

**Date**: August 16, 2026  

---

## 1. DETAILED COLLISION ANALYSIS

1. **Echo Chamber (Zhao et al., COLM 2025)**: Supports $H_{\text{REWEIGHT}}$ by showing RL amplifies pre-existing modes.
2. **Prefix-RL (Rocha Filho et al., ICLR 2026)**: Establishes that early-token prefix optimization achieves $\approx 80\%$ of full RLVR gains on standard benchmarks.
3. **Wei & Kim (2026, "Learning to Backtrack")**: Proves theoretically that RLVR enables efficient backtracking over SFT on stylized state spaces.

---

## 2. THE SURVIVING SCIENTIFIC GAP

$$\boxed{\text{The Empirical Regime-Change Boundary: Class A (Prefix-Decidable) vs Class B (Recovery-Required)}}$$

While Wei & Kim (2026) show *theoretical* backtracking benefits and Rocha Filho et al. (2026) show *empirical* prefix-only sufficiency, **no prior work has empirically tested whether Prefix-RL fails on Class B (mid-trajectory recovery) while Full RLVR succeeds**. This isolates the exact boundary where RL transitions from strategy reweighting to structural policy change.
