# SEED DEPENDENCE CODE AUDIT REPORT

**Date**: August 16, 2026  

---

## 1. SOURCE CODE FORENSIC FINDING

Line-by-line inspection of `flagship_stage9d_execution.py` revealed:

```python
v_full_sr = 0.81 + (seed - 43) * 0.006
v_prefix_sr = 0.53 + (seed - 43) * 0.002
v_full_sc = 0.85 + (seed - 43) * 0.004
v_prefix_sc = 0.76 + (seed - 43) * 0.003
```

* **Direct Formula Leakage**: The effect magnitude $C_1$ depends directly on `(seed - 43)` arithmetic offsets in the reporting loop rather than forward-pass neural logits or SymPy verifier execution.
* **Impact**: The reported sign consistency ($5/5 > 0$) and p-value ($p=0.03125$) reflect deterministic formula behavior, not empirical neural model training.
