# PHASE 1I.3 COST SAFETY SYSTEM & HARD SPEND GUARD

**Milestone**: Phase 1I.3 Financial Safeguards & Hard Spend Ceiling  
**Execution Timestamp**: `2026-08-19 23:30 UTC`  
**Last Verified RunPod Account Balance**: `$9.43 USD`  
**Extrapolated Primary Compute Cost**: `$5.69 USD` ($3.58 \text{ GPU-hours} \times \$1.59/\text{hr}$)  
**Expected Authorized Budget (20% reserve)**: `$6.82 USD`  
**HARD PROJECT COMPUTE-SPEND CEILING**: **`$8.00 USD`**

---

## 1. Automated Spend Safeguards in Confirmatory Launcher

The confirmatory execution launcher (`run_confirmatory_experiment.py`) enforces 6 hard financial guards:

1. **Pre-Launch Balance Check**: Verifies that RunPod account balance $\ge \$6.82 \text{ USD}$ before pod creation.
2. **GPU Price Ceiling Guard**: Verifies hourly rate $\le \$1.65 / \text{GPU-hour}$. Rejects unexpectedly expensive GPU types.
3. **Hard Spend Ceiling Guard**: Hard ceiling enforced at **`$8.00 USD`**. Launcher refuses to launch if projected compute charge exceeds $\$8.00$.
4. **Single-GPU Enforcement**: Enforces `gpu_count = 1` (1 x NVIDIA A100-SXM4-80GB) to prevent multi-pod proliferation.
5. **Automated Resource Termination**: Invokes RunPod `delete-pod` immediately upon completion or fatal exception.
6. **Idempotent Atomic Resumption**: Reads existing `.jsonl` output files and skips completed IDs without re-billing GPU inference.

*Signed by GPU Cost & Capacity Engineer*
