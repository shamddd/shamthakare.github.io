# PHASE 2B — MINIMUM-COST EMPIRICAL TRAJECTORY DESIGN SEARCH REPORT

**Milestone**: Minimum-Cost Zero-GPU Trajectory Design Search & Power Audit  
**Execution Timestamp**: `2026-08-20 03:48 UTC`  
**Available RunPod Account Balance**: **`$3.11 USD`**  

---

## 1. Executive Summary & Design Frontier

Instead of executing the naive dense $K=24$ design ($152,544$ rollouts, $\$29.88$ USD), a zero-GPU Monte Carlo power and cost search evaluated candidate sparse, sequential, and unequal-$K$ checkpoint allocation strategies.

### Target Cost & Power Summary:

| Target Level | Target Goal | Optimal Sparse Checkpoints | Repetitions ($K$) | Total New Rollouts | GPU Hours (RTX 4090) | Estimated Cost (USD) | Balance Feasibility |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **TARGET A** | Intermediate Effect & Localization | $t \in \{64, 128, 192\}$ | $K=2$ | $5,448$ | $3.89$ hrs | **`$1.71 USD`** | **`SUFFICIENT`** |
| **TARGET A/B (BEST VALUE)** | Sequential Sparse Trajectory (Stage B1) | $t \in \{64, 128, 192\}$ | $K=3$ | $8,172$ | $5.84$ hrs | **`$2.57 USD`** | **`SUFFICIENT`** |
| **TARGET B** | Broad Trajectory Characterization | $t \in \{32, 96, 160, 224\}$ | $K=3$ | $10,896$ | $7.78$ hrs | **`$3.42 USD`** | Exceeds by $\$0.31$ |
| **TARGET C** | Strict Monotonicity Inference | $t \in \{32, 64, 96, 128, 160, 192, 224\}$ | $K=8$ | $50,848$ | $36.32$ hrs | **`$15.98 USD`** | Exceeds by $\$12.87$ |
| **TARGET D** | Peak & Inflection Resolution | $t \in \{32, 64, 96, 128, 160, 192, 224\}$ | $K=24$ | $152,544$ | $108.96$ hrs | **`$29.88 USD`** | Exceeds by $\$26.77$ |

---

## 2. Best Value Recommendation

$$\mathbf{RECOMMENDED\ DESIGN:\ SEQUENTIAL\ SPARSE\ 3\text{-}CHECKPOINT\ STAGE\ B1\ (K=3)}$$

* **Checkpoints**: $t \in \{64, 128, 192\}$
* **Total New Rollouts**: $8,172$ rollouts ($3 \text{ checkpoints} \times 454 \text{ problems} \times 2 \text{ conditions} \times 3 \text{ rollouts}$)
* **Estimated Cost**: **`$2.57 USD`** (Leaves a $\$0.54$ USD buffer from remaining $\$3.11$ USD balance!).
* **Paid GPU Execution**: **`NOT EXECUTED YET`** (Awaiting explicit user authorization).

*Signed by Principal ML Research Scientist & Compute-Cost Optimizer*
