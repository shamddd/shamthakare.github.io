# STATESHIFT REPRODUCIBILITY GUIDE

**Project**: StateShift  
**Author**: Sham Satish Thakare (Independent Researcher)  

---

## 1. Zero-GPU Reproduction Commands

StateShift provides pure Python commands to reproduce all statistical analyses, confidence intervals, order-restricted tests, tables, and figures from frozen empirical JSONL data (zero GPU required):

```bash
# 1. Run full statistical reproduction
python scripts/reproduce_analysis.py

# 2. Verify publication artifact assertions
python scripts/verify_artifacts.py

# 3. Run complete unit test suite
PYTHONPATH=. pytest tests/
```

---

## 2. Expected Results Verification

When running `python scripts/verify_artifacts.py`, the suite asserts the following frozen scientific results:

* **Primary Interaction ($\Gamma_{256}$)**: $+0.1176$ ($95\%$ problem-blocked bootstrap CI $[+0.0955, +0.1400]$).
* **Strict Subgroup ($\Gamma_{256,\text{Strict}}$)**: $+0.1160$ ($95\%$ CI $[+0.0913, +0.1408]$).
* **Nine-Point Trajectory Vector**: $[0.0000, +0.0333, +0.0337, +0.0774, +0.0748, +0.0598, +0.0976, +0.0950, +0.1176]$.
* **Earliest Detectable Checkpoint**: $t=32$ ($\Gamma_{32} = +0.0333$, multiplicity-adjusted 95% CI $[+0.0011, +0.0655]$).
* **Natural Error Incidence ($\text{NEI}$)**: $18.19\%$ ($582/3200$).
* **Natural Post-Error Recovery ($\text{NRR}$)**: $30.93\%$ ($180/582$, 95% CI $[27.19\%, 34.82\%]$).

*Signed by Reproducibility Auditor*
