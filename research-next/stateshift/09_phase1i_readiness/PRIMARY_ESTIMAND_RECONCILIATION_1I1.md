# STATESHIFT PRIMARY CONFIRMATORY ESTIMAND RECONCILIATION

**Milestone**: Phase 1I.1 Confirmatory Estimand Restoration  
**Execution Timestamp**: `2026-08-19 22:53 UTC`  
**Preregistration Protocol Reference**: StateShift Master Preregistration  
**Estimand Status**: **`RESTORED & FROZEN — AUTHORITATIVE PRIMARY ENDPOINT LOCKED`**

---

## 1. Primary Binary Outcome Definition

For problem instance $i \in \{1, \dots, N\}$, recovery intervention state $g \in \{R, C\}$ ($R = \text{Recovery Intervention}$, $C = \text{Control}$), checkpoint step $t \in \{0, 32, 64, 96, 128, 160, 192, 224, 256\}$, and stochastic rollout index $k \in \{1, \dots, K\}$ ($K=16$):

$$Y_{i,g,t,k} = \text{TARGET\_TRANSITION\_SUCCESS}_{i,g,t,k} \in \{0, 1\}$$

Where:
* $Y_{i,g,t,k} = 1$ if the rollout successfully transitions from an incorrect/perturbed state to the correct ground-truth mathematical solution target.
* $Y_{i,g,t,k} = 0$ otherwise.

---

## 2. Sample Aggregation & Interaction Estimand

1. **Problem-Level Checkpoint State Sample Mean**:
$$\bar{Y}_{i,g,t} = \frac{1}{K} \sum_{k=1}^{K} Y_{i,g,t,k}$$

2. **Problem-Level Checkpoint-Change Interaction Difference-in-Differences**:
$$\gamma_{i,t} = \left(\bar{Y}_{i,R,t} - \bar{Y}_{i,R,0}\right) - \left(\bar{Y}_{i,C,t} - \bar{Y}_{i,C,0}\right)$$

3. **Sample Average Estimand Trajectory**:
$$\Gamma_t = \frac{1}{N} \sum_{i=1}^{N} \gamma_{i,t}$$

---

## 3. Authoritative Primary Confirmatory Endpoint

The single primary hypothesis test of the StateShift study is evaluated strictly at the terminal fine-tuning checkpoint $T = 256$:

$$\Gamma_T = (\mu_{R,T} - \mu_{R,0}) - (\mu_{C,C,T} - \mu_{C,0}) \quad \text{at } T = 256$$

Where:
$$\mu_{g,t} = \frac{1}{N} \sum_{i=1}^{N} \bar{Y}_{i,g,t}$$

### Protocol Invariances:
* **Primary Endpoint**: $\Gamma_T$ at $T=256$.
* **Secondary / Descriptive Endpoints**: Intermediate checkpoint trajectory values $\Gamma_t$ for $t \in \{32, 64, 96, 128, 160, 192, 224\}$ are **secondary and descriptive**.
* **Prohibited Modifications**: Logit trajectories, omnibus chi-squared tests across all checkpoints, or 9 separate primary hypothesis tests are **strictly prohibited** from replacing $\Gamma_T$.

*Signed by Principal ML Research Scientist & Lead Statistical Methodologist*
