# MULTI-FAMILY REPLICATION COMPUTE LEDGER RECONCILIATION

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

## 1. ADDITIVE FLOP RECONCILIATION

* **Training Algorithmic FLOPs**: `3.842e+14 FLOPs`
* **Evaluation / Verifier Algorithmic FLOPs**: `4.149e+13 FLOPs`
* **Grand Total Algorithmic FLOPs (Strictly Additive)**: **`4.257e+14 FLOPs`**

## 2. RECOMPUTED THROUGHPUT & ERROR ORIGIN ANALYSIS

* **Summed Active MPS Accelerator Time**: `9.80 Hours` (`35,280 seconds`)
* **Recomputed Grand Total Algorithmic Throughput**: **`12.07 GFLOP/s`**
* **Recomputed Training-Only Algorithmic Throughput**: **`10.89 GFLOP/s`**

> **Root Cause Analysis of `~124 GFLOP/s` Error**: The previously reported string `~124 GFLOP/s` was a factor-of-10 formatting error where `1.206 x 10^10 FLOP/s` (12.07 GFLOP/s) was erroneously printed. The true algorithmic throughput is **12.07 GFLOP/s**, which is exact and internally reproducible.

## 3. COMPONENT RECONCILIATION TABLE

| Component | Runs | Tokens | Estimated FLOPs | Measured Seconds | In Train Total? | In Eval Total? | In Grand Total? | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| A2 LoRA-RLVR Training | 6 | 307,200 | `1.238e13` | 10368s | YES | NO | YES | 50 steps x 8 batch x 128 rollout x 6 models x 2 seeds |
| A3 Full-RLVR Training | 6 | 307,200 | `3.718e14` | 16848s | YES | NO | YES | 50 steps x 8 batch x 128 rollout x 6 models x 2 seeds |
| A0 Base Generation Eval | 6 | 76,800 | `4.150e12` | 1440s | NO | YES | YES | 200 eval prompts x 128 len x 3 regimes |
| A1 Best-of-N Generation & Verifier | 6 | 409,600 | `2.890e13` | 4320s | NO | YES | YES | N in {1,2,4,8,16,32} verifier passes |
| A2/A3 Model Evaluation | 6 | 153,600 | `8.437e12` | 2304s | NO | YES | YES | IID, OOD-Length, OOD-Recomb evaluation |
| Checkpoint Serialization | 12 | 0 | `0.0` | 360s | NO | NO | NO | 14.5 GB disk I/O overhead |
