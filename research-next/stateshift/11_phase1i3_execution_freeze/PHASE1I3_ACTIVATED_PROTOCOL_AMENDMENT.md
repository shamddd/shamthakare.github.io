# STATESHIFT PHASE 1I.3 ACTIVATED PROTOCOL AMENDMENT

**Milestone**: Phase 1I.3 Prospective Protocol Amendment Activation  
**Activation Timestamp**: `2026-08-19 23:25 UTC`  
**Auditor**: Principal ML Research Scientist, Lead Statistical Methodologist & Scientific Integrity Auditor  
**Pre-Execution Status**: **`ACTIVATED PROSPECTIVELY BEFORE ANY CONFIRMATORY OBSERVATIONS`**  
**Confirmatory Rollouts Executed**: **`0`**  
**Confirmatory Outcomes Observed**: **`0`**  
**Paid GPU Spend**: **`$0`**  

---

## 1. Prospective Amendment Summary

Following a zero-cost design necessity, statistical precision, and budget solvency audit (Phase 1I.2), the primary StateShift confirmatory experiment is formally amended to the endpoint-only design:

| Design Dimension | Original FULL-9CKPT-K16 Design | Amended ENDPOINT-K16 Primary Design |
| :--- | :--- | :--- |
| **Problem Registry ($N$)** | $N = 454$ | **$N = 454$** (Unchanged) |
| **Intervention States** | $\{C, R\}$ (`Control`, `Recovery`) | **$\{C, R\}$** (Unchanged) |
| **Checkpoints ($t$)** | $\{0, 32, 64, 96, 128, 160, 192, 224, 256\}$ ($9$) | **$\{0, 256\}$** ($2$) |
| **Rollouts per Cell ($K$)** | $K = 16$ | **$K = 16$** (Unchanged) |
| **Total Confirmatory Rollouts**| $130,752 \text{ rollouts}$ | **`29,056 rollouts`** |
| **Estimated Base Compute Cost**| $\$25.58 \text{ USD}$ | **`$5.69 USD`** |
| **Total Authorized Budget** | $\$30.70 \text{ USD}$ | **`$6.82 USD`** |

---

## 2. Scientific & Methodological Rationale

1. **Exact Estimand Identification**: Mathematical proof establishes that the primary estimand $\Gamma_{256} = (\mu_{R,256} - \mu_{R,0}) - (\mu_{C,256} - \mu_{C,0})$ depends exclusively on observations at $t=0$ and $t=256$.
2. **Statistical Power Parity**: The amended design achieves **99.2% of Full Design precision** (Simulated SE = `0.0119` vs `0.0118`) while eliminating **77.8% of redundant compute** ($29,056$ rollouts vs $130,752$ rollouts).
3. **Financial Solvency**: Total authorized budget of **`$6.82 USD`** fits 100% inside the existing RunPod account balance ($9.43 \text{ USD}$), leaving a **`$2.61 USD`** untouched safety buffer.
4. **Historical Transparency**: The original FULL-9CKPT-K16 design is preserved in repository history. No historical documents have been rewritten.

*Signed by Principal ML Research Scientist & Lead Statistical Methodologist*
