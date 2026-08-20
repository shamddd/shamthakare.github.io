# IEEE BIGDATA 2026 REPRODUCIBILITY & ARTIFACT CHECKLIST

**Paper Title**: A State-Matched Framework for Evaluating Recovery Behavior in Language-Model Reasoning  
**Author**: Sham Satish Thakare (Independent Researcher, Pune, Maharashtra, India)  

---

## 1. CLAIMS & EVIDENCE ALIGNMENT

- [x] **Primary Empirical Claim**: Under the state-matched protocol ($N=400$), $D_{\text{recovery}} = -0.1100$ with 95% descriptive bootstrap CI $[-0.240, +0.030]$.
- [x] **No Causal Claims**: The paper explicitly avoids claiming causal mechanisms, instruction tuning harms, or model superiority.
- [x] **Reproducibility Guarantee**: Every reported statistic is mechanically recomputed from sealed `RAW_NEURAL_ROLLOUTS.jsonl`.

---

## 2. ARTIFACT PROVENANCE

| Artifact Description | File Path | SHA-256 Digest |
| :--- | :--- | :--- |
| **Sealed Raw Rollout Evidence** | `09_genuine_execution_v1/RAW_NEURAL_ROLLOUTS.jsonl` | `51b5a157d9e44102caeb86d0b356f558aa7499f6bad3634f668f0dd1ed76b1b4` |
| **Preexecution Lock V1** | `09_genuine_execution_v1/GENUINE_V1_PREEXECUTION_LOCK.json` | `d3b14589e7c9f801bc21503fbde1103f6fbc265e31765acbb1816bc8d8fecf10` |
| **Publication Certificate V2** | `09_genuine_execution_v1/PUBLICATION_EMPIRICAL_CERTIFICATE_V2.json` | `3f3291ab1a1290374e2ee9aebebe7a9bdc5fa62ec26ae5800d3fb0a9ca3b8ef4` |
| **Git Commit Seal** | `8228f1c0` | `8228f1c02d658a788f306822ebf4c9500646a5dd` |

---

## 3. INDEPENDENT RECONSTRUCTION

The raw JSONL record can be independently audited without importing framework internals:

```bash
python3 recovery_eval/execution/verify_raw_provenance.py
python3 recovery_eval/execution/verify_analysis_independent.py
```
Both independent verification scripts return **100% PASS**.
