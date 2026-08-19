# PHASE 1K FINAL STAGE-1 DESIGN RECOMMENDATION & DECISION MATRIX

**Milestone**: Phase 1K Stage-1 Final Design Recommendation  
**Execution Timestamp**: `2026-08-20 01:13 UTC`  
**Current RunPod Account Balance**: `$3.74 USD`  

---

## 1. Stage-1 Decision Matrix Across Candidate $K$ Values

| Candidate Design | $N$ | Intermediate Checkpoints | Rollouts per Cell ($K$) | Total Additional Rollouts | Extrapolated GPU-Hours | Base Compute Cost | Total Budget (incl 20% reserve) | Fits in $3.74 Balance? | Remaining Balance | Trajectory Resolution | Decision Verdict |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Candidate A ($K=16$)** | 454 | 7 | 16 | 101,696 | 12.51 h | $19.90 | $23.88 | **NO** | -$20.14 | HIGH | **UNFUNDED** |
| **Candidate B ($K=8$)** | 454 | 7 | 8 | 50,848 | 6.26 h | $9.95 | $11.94 | **NO** | -$8.20 | HIGH | **UNFUNDED** |
| **Candidate C ($K=6$)** | 454 | 7 | 6 | 38,136 | 4.69 h | $7.46 | $8.95 | **NO** | -$5.21 | HIGH | **UNFUNDED** |
| **Candidate D ($K=4$)** | 454 | 7 | 4 | 25,424 | 3.13 h | $4.97 | $5.97 | **NO** | -$2.23 | HIGH | **UNFUNDED** |
| **Candidate E ($K=2$)** | **454** | **7** | **2** | **12,712** | **1.56 h** | **$2.49** | **$2.98** | **YES** | **+$0.76 USD** | **HIGH** | **RECOMMENDED** |

---

## 2. Stage-1 Final Recommendation Summary

```
========================================================================================
RECOMMENDED SECONDARY TRAJECTORY DESIGN:
Candidate E (N=454, 7 Intermediate Checkpoints, K=2, 12,712 Rollouts)

SCIENTIFIC RATIONALE:
1. Preserves N=454 population problem units across all 7 intermediate checkpoints.
2. Achieves high emergence timing resolution and medium/high trajectory shape 
   resolution across 9 total trajectory points (t=0, 32..224, 256).
3. Base compute cost of $2.49 USD (Total budget $2.98 USD) fits 100% inside the 
   existing $3.74 USD account balance, leaving a $0.76 USD reserve buffer!

ZERO ADDITIONAL DEPOSIT REQUIRED.
========================================================================================
```

*Signed by Principal ML Research Scientist, Lead Statistical Methodologist & GPU Cost Engineer*
