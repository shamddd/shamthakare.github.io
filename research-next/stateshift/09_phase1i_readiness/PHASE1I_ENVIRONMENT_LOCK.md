# PHASE 1I ENVIRONMENT LOCK & REPRODUCIBILITY DOCUMENTATION

**Milestone**: Phase 1I Prerequisites Lock  
**Execution Timestamp**: `2026-08-19 22:14 UTC`  
**Git Commit SHA**: `7d0e7dd71838e362fc59366dd2a46c7263132922`  
**Working Tree Status**: Dirty (Local calibration scripts & report artifacts present)  

---

## 1. Frozen Infrastructure Stack

* **Operating System**: Linux (Ubuntu 22.04 LTS / RunPod PyTorch 2.4.0 Container Image)
* **Python Runtime**: `3.11.10`
* **PyTorch Core**: `2.5.1+cu124` (or `2.4.1+cu124`)
* **CUDA Driver / Runtime**: `CUDA 12.4` / Driver version matching NVIDIA A100-SXM4-80GB
* **Hugging Face Transformers**: `4.46.3`
* **vLLM Engine**: `0.7.0`
* **Accelerator Hardware**: `NVIDIA A100-SXM4-80GB` (Compute Capability 8.0)

---

## 2. Frozen Model & Tokenizer Configurations

* **Base Model Repo**: `Qwen/Qwen2.5-7B` (Revision: `d149729398750b98c0af14eb82c78cfe92750796`)
* **Fine-Tuned Checkpoints (t=32..256)**: `UWNSL/Qwen2.5-7B-deepscaler_4k_step_*`
* **Execution Dtype**: `torch.float16`
* **Tensor Parallel Size**: `1`
* **Pipeline Parallel Size**: `1`
* **vLLM Memory Utilization**: `0.90` (71.33 GiB allocated to vLLM, 55.65 GiB reserved for KV Cache)
* **Max Model Sequence Length**: `4096` tokens
* **Recommended Concurrency Level**: `C = 16`

*Signed by Reproducibility & Research Infrastructure Engineer*
