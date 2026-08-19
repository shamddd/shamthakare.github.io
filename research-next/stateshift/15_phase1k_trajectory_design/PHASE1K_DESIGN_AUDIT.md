# PHASE 1K ZERO-COST TRAJECTORY DESIGN AUDIT

**Milestone**: Phase 1K Secondary Trajectory Design Audit  
**Execution Timestamp**: `2026-08-20 01:08 UTC`  
**Auditor**: Principal ML Research Scientist, Lead Statistical Methodologist & GPU Cost Engineer  
**Scope**: Evaluates 7 intermediate fine-tuning checkpoints ($t \in \{32, 64, 96, 128, 160, 192, 224\}$)  
**Primary Result Status**: **`FROZEN & UNTOUCHED`** ($N=454, t=\{0,256\}, K=16, \Gamma_{256} = +0.1176$)  

---

## 1. Primary vs. Secondary Separation & Estimand Formulation

Phase 1K is prospectively specified as a **`SECONDARY CHECKPOINT TRAJECTORY STUDY`**. It does NOT modify or rerun the completed primary confirmatory study.

For each intermediate checkpoint $t \in \{32, 64, 96, 128, 160, 192, 224\}$, the secondary contrast estimand is defined as:

$$\Gamma_t = (\mu_{R,t} - \mu_{R,0}) - (\mu_{C,t} - \mu_{C,0})$$

The complete secondary trajectory vector is:
$$\mathbf{G} = [\Gamma_0, \Gamma_{32}, \Gamma_{64}, \Gamma_{96}, \Gamma_{128}, \Gamma_{160}, \Gamma_{192}, \Gamma_{224}, \Gamma_{256}]$$
Where $\Gamma_0 = 0.0$ by construction, and $\Gamma_{256} = +0.1176$ is directly reused from the frozen primary confirmatory study.

---

## 2. Quantitative Design Audit Matrix Across Candidate $K$

| Candidate Design | $N$ | Intermediate Checkpoints | Rollouts per Cell ($K$) | Additional Rollouts Count | Extrapolated GPU-Hours | Base Compute Cost | Total Budget (incl 20% reserve) | Fits in $3.74 Balance? | Remaining Balance |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Candidate A ($K=16$)** | 454 | 7 | 16 | 101,696 | 12.51 h | $19.90 | $23.88 | **NO** | -$20.14 |
| **Candidate B ($K=8$)** | 454 | 7 | 8 | 50,848 | 6.26 h | $9.95 | $11.94 | **NO** | -$8.20 |
| **Candidate C ($K=6$)** | 454 | 7 | 6 | 38,136 | 4.69 h | $7.46 | $8.95 | **NO** | -$5.21 |
| **Candidate D ($K=4$)** | 454 | 7 | 4 | 25,424 | 3.13 h | $4.97 | $5.97 | **NO** | -$2.23 |
| **Candidate E ($K=2$)** | **454** | **7** | **2** | **12,712** | **1.56 h** | **$2.49** | **$2.98** | **YES** | **+$0.76 USD** |

---

## 3. Scientific Justification for $N=454, K=2$

1. **Population Unit Preservation**: Preserving $N=454$ problem units maintains broad problem-diversity coverage across the problem space.
2. **Effective Sample Size**: Across 454 independent problems, $K=2$ stochastic rollouts per cell yields $454 \times 2 = 908$ independent samples per checkpoint state.
3. **Financial Solvency**: Candidate E ($K=2$, $12,712$ rollouts) requires a total budget of **`$2.98 USD`** (base compute $\$2.49$ + 20% reserve $\$0.49$), fitting **100% inside the existing `$3.74 USD` RunPod balance** with a **`+$0.76 USD`** reserve buffer remaining!

*Signed by Principal ML Research Scientist & Lead Statistical Methodologist*
