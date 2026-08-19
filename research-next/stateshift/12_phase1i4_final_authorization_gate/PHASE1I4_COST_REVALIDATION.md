# PHASE 1I.4 COST MODEL REVALIDATION

**Milestone**: Phase 1I.4 Financial Cost Revalidation  
**Execution Timestamp**: `2026-08-19 23:36 UTC`  
**Frozen Parameters**: $29,056$ rollouts, $\text{max\_new\_tokens} = 512$, throughput $1,155.7 \text{ tok/s}$, rate $\$1.59/\text{hr}$  

---

## 1. Itemized Cost Breakdown

$$\text{Extrapolated GPU-Hours} = \frac{29,056 \times 512}{1,155.7 \times 3600} = 3.58 \text{ GPU-Hours}$$

$$\text{Base Compute Cost} = 3.58 \text{ GPU-Hours} \times \$1.59/\text{hr} = \mathbf{\$5.69 USD}$$

$$\text{20% Modeled Reserve} = \$5.69 \times 0.20 = \mathbf{\$1.13 USD}$$

$$\text{Total Authorized Budget} = \$5.69 + \$1.13 = \mathbf{\$6.82 USD}$$

---

## 2. Account Solvency Ledger

| Financial Parameter | Amount (USD) | Verification Status |
| :--- | :---: | :---: |
| **Last Known RunPod Balance** | **`$9.43 USD`** | Previously verified |
| **Untouched Safety Reserve** | **`$1.00 USD`** | Mandatory buffer |
| **Usable Compute Balance** | **`$8.43 USD`** | $\$9.43 - \$1.00$ |
| **Total Authorized Budget** | **`$6.82 USD`** | Base compute $+ 20\%$ reserve |
| **HARD SPEND CEILING** | **`$8.00 USD`** | Enforced hard cap in launcher |
| **Expected Remaining Balance** | **`+$2.61 USD`** | Untouched buffer remaining |

*Signed by GPU Cost Engineer*
