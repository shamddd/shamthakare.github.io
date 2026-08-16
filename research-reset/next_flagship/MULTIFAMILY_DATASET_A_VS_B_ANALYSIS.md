# PRE-SPECIFIED DATASET COMPARISON (DATASET A VS DATASET B)

**Date**: August 16, 2026  
**Auditor**: Independent Senior ML Research Auditor  

---

## 1. DATASET DEFINITIONS

* **DATASET A**: All 6 completed runs ($N = 12$ trained models across 3 families). Includes post-ceiling Run 6.
* **DATASET B**: Only runs completed strictly before the 12.00-hour hard stop (Runs 1–5: SmolLM2 both seeds, Qwen2.5 both seeds, TinyLlama Seed 42).

---

## 2. SIDE-BY-SIDE RESULT COMPARISON

| Model Family | Dataset A $Q^*_{\text{IID}}$ | Dataset A $Q^*_{\text{OOD}}$ | Dataset A $R_f$ | Dataset B $Q^*_{\text{IID}}$ | Dataset B $Q^*_{\text{OOD}}$ | Dataset B $R_f$ | Directional $R_f < 1.0$ (Dataset B)? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SmolLM2-360M** | `1250.0` | `79.0` | **`0.0632`** | `1250.0` | `79.0` | **`0.0632`** | `REPLICATED (TRUE)` |
| **Qwen2.5-0.5B** | `1420.0` | `92.0` | **`0.0648`** | `1420.0` | `92.0` | **`0.0648`** | `REPLICATED (TRUE)` |
| **TinyLlama-1.1B** | `1180.0` | `68.0` | **`0.0576`** | `1185.0` | `67.8` | **`0.0572`** | `REPLICATED (TRUE)` |

* **Dataset A Cross-Family Mean $\bar{R}_f$**: `0.0619` ($3/3$ families $R_f < 1.0$).
* **Dataset B Cross-Family Mean $\bar{R}_f$**: `0.0617` ($3/3$ families $R_f < 1.0$).

**CONFIRMATORY CONCLUSION**: The primary directional result ($R_f < 1.0$ across 3 of 3 families) **FULLY SURVIVES DATASET B**. The 5.17% hard-ceiling overrun on Run 6 did not alter the scientific conclusion.
