# PROSPECTIVE EMPIRICAL VALIDATION PROTOCOL

**Date**: August 16, 2026  

---

## 1. PROTOCOL SUMMARY

1. **Purpose**: Framework validation of `recovery_eval` software pipeline.
2. **Models**: `Qwen/Qwen2.5-Math-1.5B` vs `Qwen/Qwen2.5-Math-1.5B-Instruct`.
3. **Data**: 20 fresh GSM8K test split items (`gsm8k_test_000`..`019`).
4. **Covariates**: 7 prospective structural covariates.
5. **Generation**: 5 rollouts/state, $T=0.7$, $p=0.9$, max 256 tokens.
6. **Pretraining Disclaimer**: *"Evaluation items were prospectively isolated from project development; pretraining contamination of public benchmarks cannot be ruled out."*
