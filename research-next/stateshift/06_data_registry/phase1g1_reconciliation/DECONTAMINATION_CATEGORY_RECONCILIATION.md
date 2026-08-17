# DECONTAMINATION CATEGORY EXCLUSIVITY & PRECEDENCE RECONCILIATION

**Total MATH-500 Benchmark Items**: `500`  
**Primary Exclusion Criteria**: `EXACT_DUPLICATE` OR `NEAR_DUPLICATE_HIGH_CONFIDENCE` OR `STRUCTURAL_NUMERIC_VARIANT`  

---

## 1. Raw Non-Exclusive Flag Counts

| Flag Name | Raw Non-Exclusive Count ($N$) | Percentage of MATH-500 (%) | Description |
| :--- | :---: | :---: | :--- |
| **`flag_exact`** | `3` | `0.6%` | Exact normalized SHA-256 text collision |
| **`flag_near_high`** | `14` | `2.8%` | Token 3-gram Jaccard $\ge 0.85$ or Edit Ratio $\ge 0.88$ |
| **`flag_struct_num`** | `12` | `2.4%` | Numeric-erased structural collision with modified parameters |
| **`flag_possible`** | `70` | `14.0%` | Moderate similarity ($0.60 \le \text{Jaccard} < 0.85$) |

---

## 2. Category Overlap Matrix

| Category | `exact` | `near_high` | `struct_num` | `possible` |
| :--- | :---: | :---: | :---: | :---: |
| **`exact`** | `3` | `0` | `0` | `0` |
| **`near_high`** | `0` | `14` | `0` | `0` |
| **`struct_num`** | `0` | `0` | `12` | `0` |
| **`possible`** | `0` | `0` | `0` | `70` |

---

## 3. Classification Precedence Rule & Pool Size Reconciliation

To ensure single-category assignment without double-counting, the following immutable **Precedence Cascade** is applied:

1. **`EXACT_DUPLICATE`** (Priority 1): Assigned if `flag_exact == True`.
2. **`STRUCTURAL_NUMERIC_VARIANT`** (Priority 2): Assigned if `flag_struct_num == True` and `flag_exact == False`.
3. **`NEAR_DUPLICATE_HIGH_CONFIDENCE`** (Priority 3): Assigned if `flag_near_high == True` and `flag_exact == False` and `flag_struct_num == False`.
4. **`POSSIBLE_RELATED`** (Priority 4): Assigned if `flag_possible == True` and not excluded by Priorities 1–3.
5. **`NO_MEANINGFUL_MATCH`** (Priority 5): Assigned if no flags are raised.

### Mechanical Verification
- **Total Unique Excluded Problems**: `29` ($3 \text{ exact} + 12 \text{ struct} + 14 \text{ near-high} = 29$ mutually exclusive categories under precedence rule).
- **Primary Conservative Pool Calculation**: $500 - 29 = \mathbf{471}$.
- **Verification Status**: **CONFIRMED EXACT MATCH (N=471)**.

---
