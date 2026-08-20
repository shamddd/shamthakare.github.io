# PHASE 1I RESUME & CRASH RECOVERY ARCHITECTURE AUDIT

**Milestone**: Phase 1I Infrastructure Resilience Audit  
**Execution Timestamp**: `2026-08-19 22:16 UTC`  
**Persistence Format**: Atomic JSON Lines (`.jsonl`) with `.tmp` staging & atomic rename  
**Recovery Audit Verdict**: **`PASSED — ATOMIC, IDEMPOTENT & RESUMABLE`**

---

## 1. Globally Unique Primary Keys

Every rollout record is indexed by a primary key formatted as:

$$\text{RolloutID} = \text{pair\_\{PairID:03d\}\_\{State\}\_ckpt\_\{Checkpoint:03d\}\_r\_\{RolloutK:02d\}}$$

Example: `pair_042_recovery_ckpt_128_r_07`

---

## 2. Crash Recovery Protocol

1. **Pre-Run State Inspection**: On engine startup, the execution harness reads all existing completed `.jsonl` output files and populates an in-memory set `completed_ids = {r['rollout_id'] for r in records}`.
2. **Idempotent Skipping**: Any rollout job whose `rollout_id` is present in `completed_ids` is immediately skipped without GPU inference.
3. **Atomic Disk Persistence**: When a batch of rollouts completes, records are appended to a temporary file (`.jsonl.tmp`) and atomically flushed/synced before updating the primary output file (`os.replace()`).
4. **Interruption Tolerance**: If a pod crashes mid-generation, unpersisted rollouts are automatically re-executed on restart with their exact original deterministic seed. Completed rollouts are never duplicated or overwritten.

*Signed by Research Infrastructure & Reproducibility Engineer*
