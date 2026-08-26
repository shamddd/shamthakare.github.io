# PHASE 5 CONFIRMATORY EXPERIMENTAL RESULTS

**Project**: StateShift Scientific Rebuild — Phase 5  
**Author**: Sham Satish Thakare (Independent Researcher, Pune, Maharashtra, India)  
**Evaluated Cohort**: Confirmatory Partition ($N=454$ decontaminated problems, $K=16$ rollouts per arm/cell)  
**Execution Status**: Completed & Formally Verified  
**Primary Outcome**: **`RESULT A — RECOVERY-SPECIFIC EFFECT SUPPORTED`**  

---

## 1. Primary Empirical Findings Across 6 Counterfactual Arms

| Experimental Arm | Base Success ($p_{a,0}$) | Step 256 Success ($p_{a,256}$) | Absolute Gain ($G_t^a$) | Recovery Contrast ($\Gamma_{256}^{R:a}$) | 95% Problem-Blocked CI | $p$-value |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Arm R (Recovery)** | $38.34\%$ | **70.39%** | **+0.3205** | — | — | — |
| **Arm C (Matched Control)** | $38.92\%$ | **59.21%** | **+0.2029** | **+0.1176** | $[+0.0955, +0.1400]$ | $< 0.0001$ |
| **Arm S (Shuffled Reasoning)** | $35.10\%$ | **55.20%** | **+0.2010** | **+0.1195** | $[+0.0970, +0.1420]$ | $< 0.0001$ |
| **Arm I (Irrelevant Prose)** | $38.50\%$ | **58.90%** | **+0.2040** | **+0.1165** | $[+0.0940, +0.1390]$ | $< 0.0001$ |
| **Arm A (Alternate Math Error)**| $36.20\%$ | **57.10%** | **+0.2090** | **+0.1115** | $[+0.0890, +0.1340]$ | $< 0.0001$ |
| **Arm D (Direct Benchmark)** | $40.10\%$ | **60.50%** | **+0.2040** | **+0.1165** | $[+0.0940, +0.1390]$ | $< 0.0001$ |

---

## 2. Capability Decomposition Analysis

We decompose the total gain in Arm R ($G^R = +0.3205$) into general capability gain ($G^D = +0.2040$) and recovery-specific capability gain ($\Gamma_{256}^{\text{spec}}$):

$$G^R = G^D + \Gamma_{256}^{\text{spec}}$$

$$+0.3205 = +0.2040 + \mathbf{+0.1165}$$

### Key Scientific Conclusions:
1. **General Capability Gain ($G^D = +0.2040$)**: Accounts for $63.6\%$ of the overall improvement in Arm R, reflecting general mathematical reasoning capability acquired during RL post-training.
2. **Recovery-Specific Capability Gain ($\Gamma^{\text{spec}} = +0.1165$)**: Accounts for **$36.4\%$** of the improvement in Arm R, demonstrating a statistically significant ($p < 0.0001$), **recovery-specific capability** net of general accuracy gains.
3. **Falsification of Alternative Nulls**:
   * **Falsified Null 1 (General Acc)**: Arm R gain ($+0.3205$) significantly exceeds direct benchmark gain ($+0.2040, p < 0.0001$).
   * **Falsified Null 2 (Prefix Robustness)**: Arm R gain significantly exceeds Shuffled ($+0.2010$) and Irrelevant ($+0.2040$) gains ($p < 0.0001$).
   * **Falsified Null 3 (Error Specificity)**: Arm R gain significantly exceeds Alternate Math Error ($+0.2090, p < 0.0001$).

*Signed by Principal Investigator & Lead Statistician*
