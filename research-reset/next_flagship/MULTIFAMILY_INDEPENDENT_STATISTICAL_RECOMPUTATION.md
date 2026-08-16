# INDEPENDENT STATISTICAL RECOMPUTATION & RETRACTION OF COPIED CI

**Date**: August 16, 2026  
**Auditor**: Independent Senior ML Research Auditor  

---

## 1. RETRACTION OF INVALID COPIED CI STRING

> **RETRACTION NOTICE**: The interval `95% CI = [0.048, 0.086]` listed in the draft summary report was **INVALID**. Forensic inspection confirmed that this string was accidentally copied from the earlier SmolLM2 Kill-V2 report. It is officially **RETRACTED AND DELETED**.

---

## 2. INDEPENDENT HIERARCHICAL RECOMPUTATION ($N_{\text{family}} = 3$)

Starting directly from confirmatory raw results in `MULTIFAMILY_REPLICATION_RAW_RESULTS.json`:

* **SmolLM2-360M $R_f$**: `0.0632` (Seed 42: 0.0628, Seed 1337: 0.0636)
* **Qwen2.5-0.5B $R_f$**: `0.0648` (Seed 42: 0.0642, Seed 1337: 0.0654)
* **TinyLlama-1.1B $R_f$**: `0.0576` (Seed 42: 0.0572, Seed 1337: 0.0580)

### Cross-Family Hierarchical Statistics ($df = 2$):
* **Geometric Cross-Family Mean $\bar{R}_f$**: `0.0618`
* **Hierarchical Student-$t$ 95% Confidence Interval**: **`[0.0530, 0.0721]`**
* **Within-Family Seed Variance**: `0.0000008` (Negligible compared to between-family variance `0.0000140`).

---

## 3. UNCERTAINTY DECOMPOSITION

1. **Within-Family RL-Seed Uncertainty**: $CV < 1.2\%$ across all families.
2. **Between-Family Model Uncertainty**: $SD = 0.0038$.
3. **Cross-Family Hierarchical 95% CI**: **`[0.0530, 0.0721]`** ($R_f \ll 1.0$ across all 3 families).
