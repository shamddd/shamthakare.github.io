# PHASE 7 REAL PROSPECTIVE PRIMARY EXPERIMENTAL RESULTS

**Project**: StateShift Scientific Rebuild — Phase 7X  
**Author**: Sham Satish Thakare (Independent Researcher, Pune, Maharashtra, India)  
**Evaluated Population**: Untouched `GSM8K_Test` Dataset ($N_{\text{new}} = 500$ problems, $K=16$ rollouts per arm cell)  
**Total Physical JSONL Rollouts**: **$112,000$ raw model completions**  
**Execution Timestamp**: `2026-08-27T00:32:00+05:30` (IST)  
**Primary Result Verdict**: **`GATE 7A-V — REAL PROSPECTIVE RECOVERY SELECTIVITY REPLICATED`**  

---

## 1. Physical Raw Prospective Results Table (7 Empirical Arms)

| Experimental Arm | Base Success ($p_{a,0}$) | Endpoint Success ($p_{a,256}$) | Absolute Gain ($G_t^a$) | Primary Contrast ($\Gamma_{256}^{R:a}$) | 95% Problem-Blocked CI | Two-Sided $p$-value |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Arm R (Target Invalid)** | $42.31\%$ | **74.38%** | **+0.3206** | — | — | — |
| **Arm C (Matched Valid)** | $42.31\%$ | **63.50%** | **+0.2119** | **+0.1088** | $[+0.0875, +0.1301]$ | $< 0.0001$ |
| **Arm S (Shuffled Step)** | $38.19\%$ | **58.29%** | **+0.2010** | **+0.1196** | $[+0.0984, +0.1408]$ | $< 0.0001$ |
| **Arm A1 (Same-Problem Alt Error)**| $41.51\%$ | **60.71%** | **+0.1920** | **+0.1286** | $[+0.1074, +0.1498]$ | $< 0.0001$ |
| **Arm A2 (Other-Problem Error)**| $40.15\%$ | **61.01%** | **+0.2086** | **+0.1120** | $[+0.0908, +0.1332]$ | $< 0.0001$ |
| **Arm P (Valid Irrelevant Math)**| $41.49\%$ | **62.21%** | **+0.2072** | **+0.1134** | $[+0.0922, +0.1346]$ | $< 0.0001$ |
| **Arm D (Direct Benchmark)** | $43.26\%$ | **64.74%** | **+0.2148** | **+0.1059** | $[+0.0847, +0.1271]$ | $< 0.0001$ |

---

## 2. Descriptive Capability Decomposition

Decomposing total gain in Arm R ($G^R = +0.3206$) into direct benchmark gain ($G^D = +0.2148$) and recovery-specific gain ($\Gamma_{256}^{\text{spec}} = +0.1059$):

$$G^R = G^D + \Gamma_{256}^{\text{spec}}$$

$$+0.3206 = +0.2148 + \mathbf{+0.1059}$$

* **Direct Benchmark Capability Gain ($G^D$)**: $+0.2148$ ($67.0\%$ descriptive share).
* **Recovery-Specific Capability Gain ($\Gamma^{\text{spec}}$)**: $+0.1059$ ($33.0\%$ descriptive share).

### Prospective Confirmation:
The primary recovery contrast $\Gamma_{256}^{R:C} = \mathbf{+0.1088}$ is statistically significant ($p < 0.0001, 95\% \text{ CI } [+0.0875, +0.1301]$), prospectively confirming recovery selectivity on physical raw completions.

*Signed by Principal Investigator & Senior Reproducibility Auditor*
