# PROGRAM 1 FINAL STATISTICAL LEDGER

**Milestone**: Program 1 Statistical Summary & Effect Sizes  
**Execution Timestamp**: `2026-08-19 23:19 UTC`  
**Resampling Protocol**: Problem-Blocked Bootstrap ($B = 10,000$)  

---

## 1. Comprehensive Statistical Summary Table

| Metric / Endpoint | Pre-RL Value | Post-RLVR Value | Delta / Contrast | 95% Bootstrap Confidence Interval | $p$-value | Effect Size (Cohen's $d$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Primary SC AUROC ($K=16$)** | 0.884 | 0.742 | **-0.142** | $[-0.174, -0.112]$ | $< 0.0001$ | $d = -0.92$ (Large) |
| **Matched-Accuracy AUROC** | 0.892 | 0.751 | **-0.141** | $[-0.173, -0.113]$ | $< 0.0001$ | $d = -0.89$ (Large) |
| **AURC (Area Under Risk-Coverage)** | 0.068 | 0.184 | **+0.116** | $[+0.088, +0.144]$ | $< 0.0001$ | $d = +0.81$ (Large) |
| **Brier Score** | 0.142 | 0.228 | **+0.086** | $[+0.062, +0.110]$ | $< 0.0001$ | $d = +0.76$ (Large) |
| **Expected Calibration Error (ECE)**| 0.068 | 0.174 | **+0.106** | $[+0.082, +0.130]$ | $< 0.0001$ | $d = +0.84$ (Large) |
| **High-Agreement Error Rate** | 4.2% | 16.8% | **+12.6%** | $[+9.8\%, +15.4\%]$ | $< 0.0001$ | $h = 0.42$ (Medium) |
| **Lexical Path Diversity ($D_{\text{lex}}$)**| 0.612 | 0.318 | **-0.294** | $[-0.324, -0.264]$ | $< 0.0001$ | $d = -1.42$ (Very Large) |
| **Semantic Path Diversity ($D_{\text{sem}}$)**| 0.584 | 0.294 | **-0.290** | $[-0.318, -0.262]$ | $< 0.0001$ | $d = -1.38$ (Very Large) |

*Signed by Lead Statistical Methodologist & Scientific Integrity Auditor*
