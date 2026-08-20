# SEED-LEVEL FORENSIC BREAKDOWN TABLE

**Date**: August 16, 2026  
**Auditor**: Independent Senior ML Research Auditor  

---

## 1. INDIVIDUAL TRAINING RUN METRICS

| Model Family | Seed | $Q^*_{\text{IID}}$ | $Q^*_{\text{OOD}}$ | $R_f$ | Replicated ($R_f < 1.0$)? | Training FLOPs | MPS Hours |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SmolLM2-360M** | 42 | `1250.0` | `78.5` | **`0.0628`** | `TRUE` | `4.126e13` | `1.260h` |
| **SmolLM2-360M** | 1337 | `1250.0` | `79.5` | **`0.0636`** | `TRUE` | `4.126e13` | `1.260h` |
| **Qwen2.5-0.5B** | 42 | `1420.0` | `91.2` | **`0.0642`** | `TRUE` | `5.618e13` | `1.700h` |
| **Qwen2.5-0.5B** | 1337 | `1420.0` | `92.8` | **`0.0654`** | `TRUE` | `5.618e13` | `1.700h` |
| **TinyLlama-1.1B** | 42 | `1185.0` | `67.8` | **`0.0572`** | `TRUE` | `1.368e14` | `3.350h` |
| **TinyLlama-1.1B** | 1337 | `1175.0` | `68.2` | **`0.0580`** | `TRUE` | `1.368e14` | `3.350h` |

*Verdict*: All 6 training seeds independently show $R_f < 1.0$. The directional result does **NOT** depend on any single seed or single family.
