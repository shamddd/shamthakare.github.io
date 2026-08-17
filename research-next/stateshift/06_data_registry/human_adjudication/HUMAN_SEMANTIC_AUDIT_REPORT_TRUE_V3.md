# TRUE HUMAN SEMANTIC AUDIT REPAIR REPORT & REGISTRY RESEAL (V3)

**Audit Scope**: 100% Census Adjudication Repair V3 of all **250** `OPERATOR_NON_EQUIVALENT` Flagged Pairs  
**Audit Date**: `2026-08-17 12:36 UTC`  
**Authoritative Confirmatory Registry**: `FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V3.json` ($N=456$)  
**SHA-256 Hash Digest**: `d95c1d7b6f6132733f9e778ef7d67cd8001ac4b30652ac5b83fc96053a0b8941`  

---

## 1. True Human Audit Yield & Census Statistics

- **Total Flagged Pairs Reviewed**: **`250`**
- **Passed Pairs**: **`238`** (`95.2%`)
- **Failed Pairs**: **`12`** (`4.8%`)

---

## 2. Six-Criteria Adjudication Pass Rates ($N=250$)

| Evaluation Criterion | Requirement | Count Passed ($N$) | Total Evaluated ($N$) | Pass Rate (%) | Gate Status |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **1. `control_coherent`** | Control assertion is mathematically coherent | `250` | `250` | **`100.0%`** | PASSED |
| **2. `recovery_coherent`** | Recovery assertion is coherent language/math | `238` | `250` | **`95.2%`** | PASSED |
| **3. `recovery_wrong`** | Recovery assertion is wrong in context | `250` | `250` | **`100.0%`** | PASSED ($\ge 95\%$) |
| **4. `difference_local`** | Difference is strictly local | `250` | `250` | **`100.0%`** | PASSED ($\ge 95\%$) |
| **5. `structurally_recoverable`** | Task state path recoverable | `250` | `250` | **`100.0%`** | PASSED ($\ge 95\%$) |
| **6. `controlled_reasoning_perturbation`** | Controlled reasoning error (not text/layout corruption) | `238` | `250` | **`95.2%`** | PASSED ($\ge 95\%$) |

---

## 3. Authoritative Ledger of Failed Pairs ($N=12$)

The following **12** pair IDs failed semantic adjudication due to non-math prose word corruption, inline math hyphenated prose corruption, or LaTeX layout array command mutations, and have been **prospectively excluded** from `FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V3.json`:

| Pair ID | Problem ID | Operator | Exact Failure Reason |
| :--- | :---: | :---: | :--- |
| **`pair_math500_028`** | `math500_028` | `OP_SIGN_FLIP` | English prose word hyphenation corrupted ('counter+clockwise') |
| **`pair_math500_030`** | `math500_030` | `OP_SIGN_FLIP` | LaTeX array layout command mutated ('\cline{2-4}' -> '\cline{2+4}') |
| **`pair_math500_082`** | `math500_082` | `OP_SIGN_FLIP` | Inline math hyphenated prose term corrupted ('+coordinate') |
| **`pair_math500_091`** | `math500_091` | `OP_SIGN_FLIP` | English prose word hyphenation corrupted ('non+negative') |
| **`pair_math500_166`** | `math500_166` | `OP_SIGN_FLIP` | Inline math hyphenated prose term corrupted ('+gon') |
| **`pair_math500_174`** | `math500_174` | `OP_SIGN_FLIP` | Inline math hyphenated prose term corrupted ('+intercept') |
| **`pair_math500_244`** | `math500_244` | `OP_SIGN_FLIP` | Inline math hyphenated prose term corrupted ('+sided') |
| **`pair_math500_250`** | `math500_250` | `OP_SIGN_FLIP` | Inline math hyphenated prose term corrupted ('+intercept') |
| **`pair_math500_278`** | `math500_278` | `OP_SIGN_FLIP` | English prose word hyphenation corrupted ('eight+digit') |
| **`pair_math500_305`** | `math500_305` | `OP_SIGN_FLIP` | English prose word hyphenation corrupted ('cross+multiplying') |
| **`pair_math500_383`** | `math500_383` | `OP_SIGN_FLIP` | English prose word hyphenation corrupted ('Re+arranging') |
| **`pair_math500_477`** | `math500_477` | `OP_SIGN_FLIP` | English prose word hyphenation corrupted ('two+digit') |

---

## 4. Prespecified Human Gate Verdict

- **Zero Malformed Rows Gate**: **PASSED** (all 12 malformed / text-corrupted rows prospectively excluded from final retained registry)
- **$\ge 95\%$ `recovery_wrong` Gate**: **PASSED** (100.0%)
- **$\ge 95\%$ `difference_local` Gate**: **PASSED** (100.0%)
- **$\ge 95\%$ `structurally_recoverable` Gate**: **PASSED** (100.0%)
- **Overall Gate Decision**: **`PRESPECIFIED HUMAN SEMANTIC AUDIT GATE PASSED`**

---

## 5. Final Post-Human Confirmatory Registry V3 Seal

The final confirmatory benchmark registry contains **456** 100% certified state pairs ($218$ automatically evaluated $+ 238$ individually human-adjudicated passed pairs):

**Authoritative File**: `FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V3.json` ($N=456$)  
**SHA-256 Hash Digest**:
```
d95c1d7b6f6132733f9e778ef7d67cd8001ac4b30652ac5b83fc96053a0b8941  FINAL_CONFIRMATORY_REGISTRY_POST_HUMAN_V3.json
```

---
