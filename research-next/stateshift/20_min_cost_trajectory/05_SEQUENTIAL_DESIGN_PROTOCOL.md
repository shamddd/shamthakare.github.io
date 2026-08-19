# PHASE 2B — TWO-STAGE SEQUENTIAL TRAJECTORY EXECUTION PROTOCOL

**Milestone**: Prospective Two-Stage Sequential Design Specification  

---

## 1. Protocol Architecture

* **Stage B1 (Sparse Initial Probe)**:
  * **Checkpoints**: $t \in \{64, 128, 192\}$
  * **Sample Size**: $N=454, K=3$ repetitions per cell ($8,172$ total rollouts).
  * **Cost**: **`$2.57 USD`** (Within current $\$3.11$ USD balance).
* **Stage B2 (Conditional Secondary Expansion)**:
  * **Trigger Condition**: If after Stage B1, $\Gamma_{128}$ is positive but the 95% problem-blocked bootstrap CI includes zero (i.e. statistical uncertainty is unresolved), execute Stage B2 ($K=+3$ additional rollouts).
  * **Cost**: Additional $\$2.57$ USD (Requires $\$2.03$ USD top-up).
  * **Stopping Rule**: If Stage B1 achieves 95% CI excluding zero for $\Gamma_{128}$, **STOP IMMEDIATELY**.

*Signed by Experimental Design Expert & Compute-Cost Optimizer*
