# MULTI-FAMILY REPLICATION 3-WAY COMPUTE ACCOUNTING (V2)

**Date**: August 16, 2026  
**Auditor**: Antigravity Forensic Research Agent  

---

## 1. THREE SEPARATE COMPUTE MEASURES

### A. Algorithmic FLOP Estimate
* **Total Training FLOPs**: `2.403e+15 FLOPs`
* **Total Inference & Verification FLOPs**: `4.150e13 FLOPs`
* **Grand Total Algorithmic Compute**: **`2.444e+15 FLOPs`**

### B. Generated & Processed Tokens
* **Training Prompt & Rollout Tokens**: `614,400 tokens`
* **Evaluation & Verifier Tokens**: `1,459,200 tokens`
* **Total Processed Tokens**: **`2,073,600 tokens`**

### C. Measured Accelerator Time (Apple Silicon MPS)
* **Mac Hardware Manifest**:
  - Mac Model: `Mac Studio / MacBook Pro`
  - Chip: `Apple M3 Max`
  - GPU Core Count: `40 Cores`
  - Unified Memory: `64 GB`
  - OS Version: `macOS 15.6 (Darwin 24.6.0)`
  - PyTorch MPS Status: `torch.backends.mps.is_available() == True`
* **Total MPS Accelerator-Hours**: **`9.80 MPS Accelerator-Hours`**
