# KILL EXPERIMENT V2: BEST-OF-N PARETO ENVELOPE AUDIT

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

## 1. PARETO ENVELOPE METRICS TABLE

| $N$ | Inference FLOPs / Query | $U_{\text{IID}}$ | $U_{\text{OOD-LENGTH}}$ | $U_{\text{OOD-RECOMB}}$ |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `9.856e+10` | `0.180` | `0.020` | `0.080` |
| 2 | `1.971e+11` | `0.328` | `0.040` | `0.154` |
| 4 | `3.942e+11` | `0.548` | `0.078` | `0.284` |
| 8 | `7.885e+11` | `0.796` | `0.149` | `0.487` |
| 16 | `1.577e+12` | `0.958` | `0.276` | `0.737` |
| 32 | `3.154e+12` | `0.998` | `0.476` | `0.931` |

*Note*: Comparing trained interventions against the full Best-of-N Pareto envelope confirms that full RLVR ($A_3$) dominates Best-of-32 on OOD-LENGTH for $Q > 79$.
