# RECOVERY SEMANTIC QUALITY AUDIT REPORT

**Target Registry**: `FINAL_PROSPECTIVE_STATE_REGISTRY_V3.json` ($N=468$)  
**Audit Protocol**: 100% Mechanical Semantic Quality Filter & LaTeX Boundary Checker  

---

## 1. Mechanical Audit Yield & Quality Summary

- **Total Registry Pairs Audited**: `468`
- **Pairs Passing All Semantic Quality Rules**: **`468`** (`100.0%`)
- **Malformed / Corrupted Pairs Identified**: **`0`**
- **LaTeX Delimiter Balance Rate**: `100.0%`
- **Grammatical Interpretability Rate**: `100.0%`

---

## 2. Operator-by-Operator Quality Breakdown

| Operator Name | Registered Pairs ($N$) | Semantic Quality Pass Rate | Primary Transformation Type |
| :--- | :---: | :---: | :--- |
| **`OP_FRACTION_FLIP`** | `94` | **100%** | Numerator/denominator inversion inside LaTeX `\frac{A}{B}` |
| **`OP_SIGN_FLIP`** | `191` | **100%** | Arithmetic sign inversion ($+ \leftrightarrow -$) in math expression |
| **`OP_CONSTANT_PERTURB`** | `182` | **100%** | Single numerical constant offset ($\pm 1$) inside equation |
| **`OP_TERM_SWAP`** | `1` | **100%** | Expression-aware LHS/RHS swap strictly inside equation delimiters |

---
