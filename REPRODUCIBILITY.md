# Portfolio Master Reproducibility Guide

**Author**: Sham Satish Thakare  
**Date**: August 2026  
**Target Reviewers**: JMLR, TMLR, IEEE TDSC, IEEE TPDS, IEEE TCC, ACM TOPS, USENIX Security, PhD Admissions Committees.

---

## Environment & Prerequisites (`ENVIRONMENT.md`)

* **Operating System**: macOS (Apple Silicon ARM64 / x86_64) or Linux (Ubuntu 22.04 LTS / 24.04 LTS).
* **Python Runtime**: Python 3.12+ / 3.13+ managed via `uv` 0.12+.
* **Core Dependencies**: `torch`, `transformers`, `numpy`, `scipy`, `pandas`, `pytest`, `fastapi`, `pydantic`.
* **Hardware Requirements**:
  - Minimum: 8 CPU cores, 16 GB RAM, 10 GB disk space.
  - Recommended: 10+ CPU cores, 32 GB RAM, MPS/CUDA acceleration.

---

## One-Command Reproduction Protocol

To reproduce the experimental results and figures for any active project:

### 1. AdaptiveRL-Forge (`adaptive-rl-forge`)
```bash
cd /Users/shamthakare/.gemini/antigravity/scratch/adaptive-rl-forge
uv run python scripts/run_real_empirical_pipeline.py --seeds 42,43,44,45,46
uv run pytest tests/ -v
```

### 2. EnclaveShield (`enclaveshield`)
```bash
cd /Users/shamthakare/.gemini/antigravity/scratch/enclaveshield
uv run python scripts/run_enclave_bench.py --seeds 42,43,44,45,46
uv run pytest tests/ -v
```

### 3. QuorumShift (`quorumshift`)
```bash
cd /Users/shamthakare/.gemini/antigravity/scratch/quorumshift
uv run python scripts/run_consensus_bench.py --seeds 42,43,44,45,46
uv run pytest tests/ -v
```

### 4. Secure Cloud Infrastructure Platform (`secure-cloud-infrastructure-platform`)
```bash
cd /Users/shamthakare/.gemini/antigravity/scratch/secure-cloud-infrastructure-platform
uv run python scripts/run_policy_verification.py --seeds 42,43,44,45,46
uv run pytest tests/ -v
```

### 5. TraceMind (`tracemind`)
```bash
cd /Users/shamthakare/.gemini/antigravity/scratch/tracemind
uv run python scripts/run_causalops_bench.py --seeds 42,43,44,45,46
uv run pytest tests/ -v
```

---

## Artifact Checksums & Integrity Validation

All raw benchmark run metrics are saved in standard `json` / `jsonl` / `csv` format under `artifacts/runs/`.
Checksums can be verified via:
```bash
shasum -a 256 artifacts/runs/*.json
```
