# PHASE 1I REVISED COST & WALL-CLOCK EXECUTION PLAN

**Milestone**: Phase 1I Preregistered Confirmatory Execution Infrastructure Plan  
**Execution Timestamp**: `2026-08-19 16:33 UTC`  
**Auditor**: Lead Research Infrastructure Engineer & Scientific Integrity Auditor  
**Scope**: 456 item pairs $\times$ 2 states $\times$ 9 checkpoints $\times$ 16 rollouts = **131,328 rollouts**  
**Recommended Engine**: `vLLM Continuous Batching Engine (C=16)`  
**Overall Readiness Verdict**: **`1. READY FOR CONFIRMATORY EXECUTION (ON HUMAN AUTHORIZATION HOLD)`**

---

## 1. Revised Cost & Wall-Clock Estimates ($N=131,328$ Rollouts)

With the recommended **`vLLM Continuous Batching Engine (C=16)`** (1,155.7 tok/s throughput on A100 SXM), total compute for the preregistered 512-token expected scenario drops from **`371.07 GPU-Hours`** down to **`16.16 TOTAL GPU-Hours`**.

### Comprehensive Hardware & Parallelization Matrix (512-Tok Expected Scenario)

| Hardware Setup | Provider / Tier | Rate ($/GPU-hr) | Concurrency per GPU | Wall-Clock Execution Time | Total Extrapolated Compute | Total Compute Cost | Feasibility Threshold ($\le 250$h) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1 x A100-SXM4-80GB** | RunPod Secure | $1.59 | $C=16$ | **16.16 Hours** | **16.16 GPU-Hours** | **$25.70 USD** | **GO** |
| **2 x A100-SXM4-80GB** | RunPod Secure | $1.59 | $C=16$ | **8.08 Hours** | **16.16 GPU-Hours** | **$25.70 USD** | **GO** |
| **4 x A100-SXM4-80GB** | RunPod Secure | $1.59 | $C=16$ | **4.04 Hours** | **16.16 GPU-Hours** | **$25.70 USD** | **GO** |
| **8 x A100-SXM4-80GB** | RunPod Secure | $1.59 | $C=16$ | **2.02 Hours** | **16.16 GPU-Hours** | **$25.70 USD** | **GO** |

---

## 2. Extended Output Scenarios under Recommended Engine

| Output Length Scenario | Avg Generated Tokens | Total Generated Tokens | Extrapolated Total GPU-Hours | 1-GPU Wall Clock | 4-GPU Wall Clock | Total Compute Cost ($1.59/hr) | Peak VRAM | Verdict |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Preregistered Expected** | 512 tok | 67,240,000 tok | **16.16 GPU-Hours** | 16.16 h | 4.04 h | **$25.70 USD** | 70.13 GB | **GO** |
| **Extended Reasoning** | 1,024 tok | 134,480,000 tok | **31.78 GPU-Hours** | 31.78 h | 7.95 h | **$50.52 USD** | 70.13 GB | **GO** |
| **Worst-Case Long Context**| 2,048 tok | 268,960,000 tok | **63.72 GPU-Hours** | 63.72 h | 15.93 h | **$101.31 USD** | 70.13 GB | **GO** |

---

## 3. Recommended Execution Deployment Plan

1. **Provisioning**: Provision 1 x A100-SXM4-80GB (or 2 x A100 for 8-hour completion).
2. **Engine**: Deploy `vLLM` v0.7.0 with `gpu_memory_utilization=0.90` and $C=16$.
3. **Budget Impact**: Consumes **`~$25.70 USD`** of GPU compute (additional deposit required since current account balance is $9.43 USD).
4. **Governance Directive**: **DO NOT launch automatically.** Wait for explicit human user authorization.

*Signed by Lead Research Infrastructure Engineer & Scientific Integrity Auditor*
