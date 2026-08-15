# NATURAL DUPLICATE & BENCHMARK CONTAMINATION AUDIT

**Date**: August 16, 2026  

---

## 1. BENCHMARK SPLIT AND CONTAMINATION CONTROLS

1. **Item Independence**: 30 unique items from official `train` splits of GSM8K, MATH, MBPP.
2. **Overlap Audit**: Computed $N$-gram overlap ($N=8$) against test splits. Zero test-set items included.
3. **Duplicate Filter**: Deduplicated exact or near-duplicate problem prompts (min edit distance $> 30\%$).
