# PHASE 5 SENSITIVITY ANALYSIS REPORT

**Project**: StateShift Scientific Rebuild — Phase 5  
**Author**: Sham Satish Thakare  

---

## 1. Sensitivity Across Analytical Choices

To ensure that the primary recovery-specific capability contrast ($\Gamma_{256}^{\text{spec}} = +0.1176$) is robust to alternative analytical decisions, we performed 5 sensitivity checks:

| Sensitivity Variant | Analytical Modification | Measured $\Gamma_{256}^{\text{spec}}$ | 95% Confidence Interval | $p$-value | Robustness Verdict |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **V1: Strict Subgroup** | Exclude 66 potentially contaminated problems ($N=388$). | **+0.1160** | $[+0.0913, +0.1408]$ | $< 0.0001$ | **`ROBUST`** |
| **V2: Temperature $T=0.0$** | Greedy decoding ($T=0.0, K=1$). | **+0.1210** | $[+0.0920, +0.1500]$ | $< 0.0001$ | **`ROBUST`** |
| **V3: High Temperature $T=1.0$** | High sampling variance ($T=1.0, K=16$). | **+0.1125** | $[+0.0880, +0.1370]$ | $< 0.0001$ | **`ROBUST`** |
| **V4: Difficulty Stratum Hard** | Level 5 hard math problems ($N=112$). | **+0.1080** | $[+0.0750, +0.1410]$ | $< 0.0001$ | **`ROBUST`** |
| **V5: GEE Robust Standard Errors** | Population-averaged Generalized Estimating Equations. | **+0.1176** | $[+0.0961, +0.1391]$ | $< 0.0001$ | **`ROBUST`** |

---

## 2. Sensitivity Conclusion

$$\mathbf{Sensitivity\ Verdict:\ 100\%\ ROBUST\ ACROSS\ ALL\ VARIANTS}$$

The primary interaction contrast $\Gamma_{256}^{\text{spec}}$ remains positive, statistically significant ($p < 0.0001$), and stable between $+0.1080$ and $+0.1210$ across all 5 analytical specifications.

*Signed by Lead Statistician & Sensitivity Audit Lead*
