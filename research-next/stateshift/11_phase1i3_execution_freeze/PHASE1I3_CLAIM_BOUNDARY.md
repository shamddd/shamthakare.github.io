# STATESHIFT PHASE 1I.3 CLAIM BOUNDARY FREEZE

**Milestone**: Phase 1I.3 Scientific Claim Boundary Enforcement  
**Execution Timestamp**: `2026-08-19 23:27 UTC`  
**Auditor**: Scientific Integrity Auditor & Adversarial Area Chair  

---

## 1. Permitted Primary Scientific Claims

The primary confirmatory experiment ($N=454, t=\{0,256\}, K=16, 29,056 \text{ rollouts}$) authorizes the following primary scientific claims:

1. **Estimand Sign & Magnitude**: Exact point estimate and 95% bootstrap confidence interval for $\Gamma_{256}$.
2. **Differential Recovery Change**: Whether state intervention ($R$) and control ($C$) continuations evolve differently from pre-training base ($t=0$) to terminal fine-tuning ($t=256$).
3. **Matched State $\times$ Checkpoint Interaction**: Significance test of the state-matched contrast $\Gamma_{256}$.
4. **Contamination Robustness**: Strict sensitivity analysis evaluated under $N=388$ (`FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V4_STRICT.json`).

---

## 2. Strictly Prohibited Claims (Without Future Intermediate Execution)

The following claims are **FORMALLY PROHIBITED** from being made in any manuscript or summary without future independent execution of intermediate checkpoints ($t=32..224$):

1. **Monotonicity**: Claiming that error recovery capability increases monotonically across training.
2. **Non-Monotonicity**: Claiming that error recovery capability exhibits non-monotonic trajectory dips.
3. **Transition Timing**: Claiming that recovery capability emerges at a specific intermediate checkpoint (e.g. step 96 or step 128).
4. **Inflection Point**: Claiming specific trajectory inflection points.
5. **Full Trajectory Shape**: Describing the functional shape of intermediate fine-tuning steps.

---

## 3. Preservation of Secondary Experiment

* Intermediate checkpoints ($t \in \{32, 64, 96, 128, 160, 192, 224\}$) are cataloged as `DEFERRED_SECONDARY_TRAJECTORY_EXPERIMENT` (Status: `NOT EXECUTED`).
* Execution of the secondary trajectory experiment is **independent** and will **NOT** automatically trigger based on whether $\Gamma_{256}$ is statistically significant.

*Signed by Scientific Integrity Auditor & Adversarial Area Chair*
