# PHASE 1I RNG AND SEED DETERMINISM AUDIT

**Milestone**: Phase 1I RNG & Seed Allocation Audit  
**Execution Timestamp**: `2026-08-19 22:15 UTC`  
**Master RNG Seed**: `20260819`  
**Total Rollouts Evaluated**: `131,328`  
**Seed Audit Verdict**: **`PASSED — DETERMINISTIC, UNIQUE & COLLISION-FREE`**

---

## 1. Deterministic Seed Mapping Formula

To guarantee 100% reproducibility across parallel GPUs, resuming after crashes, and job sharding, every rollout seed is computed deterministically from the 5-tuple:

$$\text{Seed} = \text{MasterSeed} + (\text{PairID} \times 100,000) + (\text{StateID} \times 10,000) + (\text{Checkpoint} \times 100) + \text{RolloutK}$$

Where:
* `MasterSeed` = `20260819`
* `PairID` $\in [1, 456]$
* `StateID`: `control` = 1, `recovery` = 2
* `Checkpoint` $\in \{0, 32, 64, 96, 128, 160, 192, 224, 256\}$
* `RolloutK` $\in [1, 16]$

---

## 2. Seed Audit Verification Findings

1. **Collision Analysis**: Audited all 131,328 seeds in `PHASE1I_DRY_RUN_LEDGER.jsonl`. Verified **`0 seed collisions`** across the entire combinatorial space.
2. **Order Independence**: Seed generation depends strictly on the static record metadata. Sharding rollouts across multiple GPUs or executing out-of-order has zero effect on assigned seeds.
3. **Engine-Specific RNG Handling**:
   * **vLLM Engine**: Seeds are passed per-request via `SamplingParams(seed=seed)`.
   * **Hugging Face Baseline**: Seeds set via PyTorch `set_seed(seed)`.
4. **Defensible Terminology**: Rollouts are classified as **"independently seeded stochastic rollouts"**. Pseudorandom generators are deterministic, but distinct seeds sample independent trajectories from the model's conditional probability distribution $P(y_t | y_{<t}, x)$.

*Signed by Statistical Methodology Reviewer & Scientific Integrity Auditor*
