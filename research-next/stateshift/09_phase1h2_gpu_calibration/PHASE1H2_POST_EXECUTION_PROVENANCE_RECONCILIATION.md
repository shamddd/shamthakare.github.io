# PHASE 1H.2 POST-EXECUTION PROVENANCE RECONCILIATION REPORT

**Milestone**: Phase 1H.2 Empirical GPU Feasibility Calibration  
**Reconciliation Date**: `2026-08-19 02:58 UTC`  
**Auditor**: Lead ML Systems Engineer, Research Infrastructure Engineer & Scientific Integrity Auditor  
**Reconciliation Status**: **`PROVENANCE RECONCILED — CALIBRATION VALID`** (Verdict Code: `A`)  
**Scientific Hold Directive**: **`ACTIVE`** — 131,328-rollout confirmatory experiment remains strictly **ON HOLD**.

---

## 1. SHA-256 Audit Matrix

| Version ID | Provenance Source | SHA-256 Hash | Status / Notes |
| :--- | :--- | :--- | :--- |
| **Version A** | Git Commit `7d0e7dd71838e362fc59366dd2a46c7263132922` (`run_gpu_checkpoint_canary.py`) | `8572efc76e1f5994451bc9232ed941565bcedf4a4d37437bca7ee937c006fc38` | Pre-execution frozen specification harness |
| **Version B** | Locally Frozen / Pre-Execution Copy (`run_gpu_checkpoint_canary.py`) | `8572efc76e1f5994451bc9232ed941565bcedf4a4d37437bca7ee937c006fc38` | Matches Version A 100% identically |
| **Version C** | Executed / Returned Execution Bundle (`run_gpu_checkpoint_canary.py`) | `623d02b5f116a484d7454ac6cadcc064b47d7a5eca87069c3c3b15444ca06f88` | Active runtime executed file on A100 GPU |

---

## 2. Complete Code Diff (Version A vs. Version C)

```diff
--- Version A (Git Commit 7d0e7dd / SHA-256 8572efc76e1f5994451bc9232ed941565bcedf4a4d37437bca7ee937c006fc38)
+++ Version C (Executed Harness / SHA-256 623d02b5f116a484d7454ac6cadcc064b47d7a5eca87069c3c3b15444ca06f88)
@@ -282,7 +282,7 @@
             model = AutoModelForCausalLM.from_pretrained(
                 repo,
                 revision=rev,
-                dtype=torch.float16,
+                torch_dtype=torch.float16,
                 device_map="auto",
                 trust_remote_code=True
             )
```

---

## 3. Root Cause Analysis: When and Why the SHA Changed

### Timeline & Failure Trace:
1. **Initial Deployment**: Harness in git commit `7d0e7dd` passed `dtype=torch.float16` to `AutoModelForCausalLM.from_pretrained()`.
2. **Runtime Container Failure**: When executed on the provisioned NVIDIA A100 host (running `PyTorch 2.4.1+cu124` and `transformers 4.46.3`), Hugging Face's `from_pretrained()` method passed `dtype` down to `Qwen2ForCausalLM.__init__()`, which raised an immediate `TypeError`:
   ```
   [FATAL LOAD FAILURE] Model load failure for checkpoint t=0: Qwen2ForCausalLM.__init__() got an unexpected keyword argument 'dtype'
   ```
3. **Operational Resolution**: Line 285 was patched from `dtype=torch.float16` to `torch_dtype=torch.float16`, which is the standard Hugging Face `transformers` parameter for FP16 model loading.
4. **Resulting SHA Change**: Replacing `dtype` with `torch_dtype` changed the single file's SHA-256 hash from `8572ef...` to `623d02...`.

---

## 4. Difference Classification

* **Classification**: **Operational / Infrastructure Only**
* **Rationale**: The change from `dtype=torch.float16` to `torch_dtype=torch.float16` is a syntactical fix required by the Hugging Face `transformers` API to instruct PyTorch to load model weights into IEEE 754 half-precision floating point format (`torch.float16`). It has zero impact on numerical precision, tensor precision, model parameters, model outputs, seeding, prompts, timing, or scientific methodology.

---

## 5. Invariant Integrity Audit Checklist

Every item in the scientific and execution protocol was audited between Version A and Version C:

| Audit Item | Impact Status | Audited Verification Evidence |
| :--- | :---: | :--- |
| **Model Repositories** | **`NO IMPACT`** | `Qwen/Qwen2.5-7B` ($t=0$) and `UWNSL/Qwen2.5-7B-deepscaler_4k_step_256` ($t=256$) identical |
| **Immutable Model Revisions** | **`NO IMPACT`** | `d149729398750b98c0af14eb82c78cfe92750796` and `7667ad787966f5733fdca3d2b240452d7095ff95` identical |
| **Synthetic Canary ID** | **`NO IMPACT`** | `synthetic_canary_001` identical |
| **Prompts & States** | **`NO IMPACT`** | `control` and `recovery` string prompts identical |
| **K=4 Allocation** | **`NO IMPACT`** | `K_PER_STATE = 4` identical (4 measured rollouts per state per checkpoint) |
| **Warmup Allocation** | **`NO IMPACT`** | 1 warmup rollout per checkpoint ($k=0, \text{is\_warmup}=\text{True}$), excluded from stats, identical |
| **Generation Parameters** | **`NO IMPACT`** | `temperature=0.6`, `top_p=0.95`, `do_sample=True`, `use_cache=True` identical |
| **Random Seeding** | **`NO IMPACT`** | `set_seed(42 + seed_offset)` identical across all rollouts |
| **Max New Tokens** | **`NO IMPACT`** | `max_new_tokens = 64` identical |
| **Temperature** | **`NO IMPACT`** | `0.6` identical |
| **Top_p** | **`NO IMPACT`** | `0.95` identical |
| **Model Dtype** | **`NO IMPACT`** | `torch.float16` (FP16) loaded on GPU in both versions |
| **`model.generate()` Call** | **`NO IMPACT`** | Hugging Face PyTorch `model.generate()` invocation identical |
| **Token Accounting** | **`NO IMPACT`** | `output[0][input_ids.shape[1]:]` slicing identical |
| **Timing Methodology** | **`NO IMPACT`** | `time.perf_counter_ns()` with `torch.cuda.synchronize()` identical |
| **VRAM Measurement** | **`NO IMPACT`** | `torch.cuda.max_memory_allocated()` per-device measurement identical |
| **Feasibility Extrapolation** | **`NO IMPACT`** | Full-study extrapolation ($N=131,328$ rollouts) identical |
| **GO / REDESIGN / NO-GO Thresholds**| **`NO IMPACT`** | Thresholds ($\le 250.0$ GPU-hours, $\le 80.0$ GB VRAM) identical |
| **Scientific Firewall** | **`NO IMPACT`** | Rejection of `technical_canary` records from confirmatory pipelines identical |

---

## 6. Official Reconciliation Verdict

```
========================================================================================
FINAL RECONCILIATION VERDICT:
A. PROVENANCE RECONCILED — CALIBRATION VALID
========================================================================================
```

### Summary of Audit Findings:
1. Git commit `7d0e7dd71838e362fc59366dd2a46c7263132922` contains file `run_gpu_checkpoint_canary.py` with SHA-256 `8572efc76e1f5994451bc9232ed941565bcedf4a4d37437bca7ee937c006fc38`.
2. The executed harness file has SHA-256 `623d02b5f116a484d7454ac6cadcc064b47d7a5eca87069c3c3b15444ca06f88`.
3. The discrepancy consists of a single contiguous 1-line operational API fix (`dtype=torch.float16` $\rightarrow$ `torch_dtype=torch.float16`).
4. The change is 100% non-material to scientific execution and does not alter any experimental, mathematical, or empirical results.
5. All 18 rollout records, benchmark metrics, extrapolations, and the `GO` verdict remain 100% valid and verified.

> [!IMPORTANT]
> **GOVERNANCE HOLD DIRECTIVE**:  
> The 131,328-rollout confirmatory experiment remains strictly **ON HOLD** and is **NOT AUTHORIZED** for launch.

---
*Signed by Lead ML Systems Engineer, Research Infrastructure Engineer & Scientific Integrity Auditor*
