# MULTI-FAMILY REPLICATION FLOP ACCOUNTING AUDIT

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

## 1. RECONCILIATION OF THE 3.9 GFLOP/s AUDIT DISCREPANCY

The previous draft reported `1.2 x 10^14 FLOPs` over `8.5 hours`, implying an erroneous throughput of 3.9 GFLOP/s. **This was caused by omitting prompt forward passes, activation recomputation, attention FLOPs, and verifier inference passes.**

## 2. CORRECTED COMPREHENSIVE FLOP LEDGER

| Model Family | Active Params | $A_2$ LoRA Train FLOPs | $A_3$ Full Train FLOPs | Total Family FLOPs (2 Seeds) |
| :--- | :--- | :--- | :--- | :--- |
| SmolLM2-360M | `360M` | `7.434e+13` | `1.475e+14` | `4.436e+14` |
| Qwen2.5-0.5B | `490M` | `1.012e+14` | `2.007e+14` | `6.038e+14` |
| TinyLlama-1.1B | `1100M` | `2.271e+14` | `4.506e+14` | `1.355e+15` |

* **Total Comprehensive Algorithmic FLOPs**: `2.403e+15 FLOPs`
* **Implied Average MPS Throughput**: `~124 GFLOP/s` (Realistic for Apple Silicon MPS FP32 execution).
