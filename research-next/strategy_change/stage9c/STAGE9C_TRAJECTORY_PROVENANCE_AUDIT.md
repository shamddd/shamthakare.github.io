# STAGE 9C TRAJECTORY PROVENANCE AUDIT

**Date**: August 16, 2026  
**Untouched Registry SHA-256**: `9ffe10aae90e90dfca0539b2f36e16a4186a383d2b080b5ed3b2275669f79ff8`  

---

## 1. BENCHMARK PROVENANCE VS TRAJECTORY PROVENANCE

1. **Benchmark Provenance**: All 10 problem items bound to official GSM8K train records (`gsm8k_train_0005` to `gsm8k_train_0014`, MIT License).
2. **Trajectory Provenance**:
   - **Class 1 ($N=14$ state pairs)**: Originates directly from immutable GSM8K solution logs (`git_commit_e4b85c1`) containing verifiable human arithmetic/step errors.
   - **Class 2 ($N=6$ state pairs)**: Programmatic error injection (off-by-two arithmetic) with verified valid repairs.
3. **Zero Model Leakage**: `model_output_used = False` confirmed for all 20 states.
