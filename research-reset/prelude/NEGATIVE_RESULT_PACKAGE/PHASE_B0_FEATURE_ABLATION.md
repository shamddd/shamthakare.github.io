# PHASE B0 FEATURE ABLATION REPORT (MODELS M0 THROUGH M5)

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

## 1. ABLATION HIERARCHY EVALUATION (LOMFO-CV)

| Model Name | Features Included | Overall MAE | Spearman $\rho$ | Kendall $\tau$ | Sign Accuracy |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Model M0** | Behavioral Baselines ($B$) | `0.0081` | `0.322` | `0.182` | `0.92` |
| **Model M1** | Behavioral + Headroom ($BH$) | `0.0090` | `-0.028` | `0.030` | `0.92` |
| **Model M2** | $BH$ + Reward Probe | `0.0090` | `-0.028` | `0.030` | `0.92` |
| **Model M3** | $BH$ + Representation Geom. | `0.0101` | `0.049` | `0.061` | `0.92` |
| **Model M4** | $BH$ + Gradient Diagnostics | `0.0090` | `-0.028` | `0.030` | `0.92` |
| **Model M5** | $BH$ + All Internal ($I$) | `0.0101` | `0.049` | `0.061` | `0.92` |

## 2. PRIMARY COMPARISON (M5 VS M1)
* **Primary Incremental $\Delta$MAE ($M_1 - M_5$)**: `-0.0011`
* **Per-Family $\Delta$MAE**:
  - SmolLM2: `-0.0018`
  - Pythia: `-0.0004`
  - Qwen: `-0.0010`
