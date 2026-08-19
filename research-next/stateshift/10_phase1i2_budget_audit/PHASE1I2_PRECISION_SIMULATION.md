# PHASE 1I.2 PRECISION & POWER SIMULATION REPORT

**Milestone**: Phase 1I.2 Prospective Power & Precision Simulation  
**Execution Timestamp**: `2026-08-19 23:20 UTC`  
**Monte Carlo Resampling Runs**: $B = 1,000$ simulated studies per candidate design  
**Simulated Dataset Size**: $N = 454$ independent problem units  
**Target Effect Size**: True $\Gamma_{256} = +0.100$  

---

## 1. Candidate Experimental Design Definitions

* **Design A (Full 9-Ckpt K=16)**: $N=454$, $9$ checkpoints, $K=16 \to \mathbf{130,752 \text{ rollouts}}$.
* **Design B (Endpoint K=16)**: $N=454$, $2$ checkpoints ($t=\{0,256\}$), $K=16 \to \mathbf{29,056 \text{ rollouts}}$.
* **Design C (Endpoint K=12)**: $N=454$, $2$ checkpoints ($t=\{0,256\}$), $K=12 \to \mathbf{21,792 \text{ rollouts}}$.
* **Design D (Endpoint K=8)**: $N=454$, $2$ checkpoints ($t=\{0,256\}$), $K=8 \to \mathbf{14,528 \text{ rollouts}}$.
* **Design E (Endpoint K=4)**: $N=454$, $2$ checkpoints ($t=\{0,256\}$), $K=4 \to \mathbf{7,264 \text{ rollouts}}$.

---

## 2. Prospective Simulation Results Matrix

| Design Identifier | Rollouts Count | Simulated SE | 95% CI Width | Statistical Power | Base Compute Cost | Total Budget (incl 20% reserve) | Fits in $9.43 Balance? |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Design A (Full 9-Ckpt K=16)** | 130,752 | `0.0118` | `0.0463` | `1.000` | $25.58 | $30.70 | **NO** (Deficit $22.27) |
| **Design B (Endpoint K=16)** | **29,056** | **`0.0119`** | **`0.0466`** | **`1.000`** | **$5.69** | **$6.82** | **YES ($1.61 Reserve Left)** |
| **Design C (Endpoint K=12)** | 21,792 | `0.0135` | `0.0529` | `1.000` | $4.26 | $5.12 | **YES ($3.31 Reserve Left)** |
| **Design D (Endpoint K=8)** | 14,528 | `0.0157` | `0.0617` | `1.000` | $2.84 | $3.41 | **YES ($5.02 Reserve Left)** |
| **Design E (Endpoint K=4)** | 7,264 | `0.0217` | `0.0849` | `0.998` | $1.42 | $1.71 | **YES ($6.72 Reserve Left)** |

---

## 3. Key Statistical Findings

1. **Precision Parity**: Design B (Endpoint K=16) achieves virtually **identical Standard Error (`0.0119` vs `0.0118`)** and **identical statistical power (`1.000`)** compared to Design A (Full 9-Ckpt).
2. **Why Intermediate Checkpoints Add Zero Precision**: Because $\Gamma_{256}$ is mathematically evaluated at $t=0$ and $t=256$, adding intermediate checkpoints ($t=32..224$) consumes 101,696 additional rollouts ($77.8\%$ of total compute) while contributing **zero additional statistical power** to $\Gamma_{256}$.
3. **Financial Solvency**: Design B (Endpoint K=16) requires a total budget of **`$6.82 USD`**, which fits **100% inside the existing $9.43 RunPod balance** with a **`$2.61 USD`** untouched buffer remaining!

*Signed by Lead Statistical Methodologist & GPU Capacity Engineer*
