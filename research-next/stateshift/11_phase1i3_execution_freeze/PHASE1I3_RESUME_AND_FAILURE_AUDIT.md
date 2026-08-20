# PHASE 1I.3 RESUME & FAILURE SAFETY AUDIT

**Milestone**: Phase 1I.3 Remote Execution & Resilience Protocol  
**Execution Timestamp**: `2026-08-19 23:31 UTC`  
**Host Environment Policy**: **`REMOTE GPU POD ONLY`** (Local Mac execution strictly prohibited for model inference)  

---

## 1. Remote GPU Only Protocol

* **Local Mac Isolation**: To prevent local CPU/RAM watchdog failures or resource exhaustion, zero model inference will be executed on the local Mac.
* **Remote Container Environment**: Execution occurs exclusively inside a remote RunPod PyTorch 2.4/2.5 CUDA container on a single NVIDIA A100-SXM4-80GB GPU.

---

## 2. Interruption & Recovery Verification

1. **Idempotent Primary Key Skipping**: Outputs indexed by `pair_{PairID:03d}_{State}_ckpt_{Checkpoint:03d}_r_{RolloutK:02d}`. Engine checks existing JSONL output lines on startup and skips completed IDs.
2. **Atomic Writes**: Writes to `.jsonl.tmp` and replaces atomically (`os.replace()`). Partial lines from crashed pods are purged before loading.
3. **Deterministic Seed Stability**: Seeds derived via 64-bit SHA-256 integers. Restarting or resuming produces identical seeds for incomplete rollouts.
4. **Duplicate Protection**: Primary key index set prevents duplicate outputs under any interruption sequence.

*Signed by ML Systems Engineer & Reproducibility Auditor*
