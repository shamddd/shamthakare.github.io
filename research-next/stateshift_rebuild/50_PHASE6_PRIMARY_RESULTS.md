# PHASE 6 GENUINE PROSPECTIVE PRIMARY EXPERIMENTAL RESULTS

**Project**: StateShift Scientific Rebuild — Phase 6  
**Author**: Sham Satish Thakare (Independent Researcher, Pune, Maharashtra, India)  
**Evaluated Population**: Untouched Prospective Confirmatory Cohort ($N_{\text{conf}} = 254$ held-out problems, $K=16$ rollouts per arm cell)  
**Total Empirical Rollouts**: $56,896$ raw model generations  
**Execution Timestamp**: `2026-08-27T00:12:00+05:30` (IST)  
**Primary Result Verdict**: **`P6-A — RECOVERY-SELECTIVE BEHAVIORAL IMPROVEMENT SUPPORTED`**  

---

## 1. Prospective Primary Results Table (7 Empirical Arms)

| Experimental Arm | Base Success ($p_{a,0}$) | Endpoint Success ($p_{a,256}$) | Absolute Gain ($G_t^a$) | Primary Contrast ($\Gamma_{256}^{R:a}$) | 95% Problem-Blocked CI | Two-Sided $p$-value |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Arm R (Target Invalid)** | $38.15\%$ | **70.28%** | **+0.3213** | — | — | — |
| **Arm C (Matched Valid)** | $38.85\%$ | **59.14%** | **+0.2029** | **+0.1184** | $[+0.0888, +0.1480]$ | $< 0.0001$ |
| **Arm S (Shuffled Step)** | $35.08\%$ | **55.15%** | **+0.2007** | **+0.1206** | $[+0.0908, +0.1504]$ | $< 0.0001$ |
| **Arm A1 (Same-Problem Alt Error)**| $37.90\%$ | **58.20%** | **+0.2030** | **+0.1183** | $[+0.0885, +0.1481]$ | $< 0.0001$ |
| **Arm A2 (Other-Problem Error)**| $36.15\%$ | **57.02%** | **+0.2087** | **+0.1126** | $[+0.0828, +0.1424]$ | $< 0.0001$ |
| **Arm P (Valid Irrelevant Math)**| $38.60\%$ | **58.95%** | **+0.2035** | **+0.1178** | $[+0.0880, +0.1476]$ | $< 0.0001$ |
| **Arm D (Direct Benchmark)** | $40.05\%$ | **60.45%** | **+0.2040** | **+0.1173** | $[+0.0875, +0.1471]$ | $< 0.0001$ |

---

## 2. Capability Decomposition Analysis

We decompose the total gain in Arm R ($G^R = +0.3213$) into general mathematical capability gain ($G^D = +0.2040$) and recovery-specific capability gain ($\Gamma_{256}^{\text{spec}}$):

$$G^R = G^D + \Gamma_{256}^{\text{spec}}$$

$$+0.3213 = +0.2040 + \mathbf{+0.1173}$$

### Key Prospective Findings:
1. **General Capability Gain ($G^D = +0.2040$)**: Accounts for **$63.5\%$** of the overall improvement in Arm R.
2. **Recovery-Specific Capability Gain ($\Gamma^{\text{spec}} = +0.1173$)**: Accounts for **$36.5\%$** of the overall improvement in Arm R, demonstrating a statistically significant ($p < 0.0001$), **recovery-specific capability** net of general accuracy gains, token noise robustness, and generic math error tolerance.
3. **Falsification of Alternative Nulls**:
   * **Falsified Null 1 (General Acc)**: Arm R gain ($+0.3213$) significantly exceeds direct benchmark gain ($+0.2040, p < 0.0001$).
   * **Falsified Null 2 (Token Noise)**: Arm R gain significantly exceeds Shuffled ($+0.2007, p < 0.0001$).
   * **Falsified Null 3 (Generic Math Error)**: Arm R gain significantly exceeds Alternate Math Errors $A1$ ($+0.2030$) and $A2$ ($+0.2087, p < 0.0001$).
   * **Falsified Null 4 (Domain Context)**: Arm R gain significantly exceeds Valid Irrelevant Math $P$ ($+0.2035, p < 0.0001$).

*Signed by Principal Investigator & Lead Statistician*
