# MATH REFERENCE SOLUTION STEP SEGMENTATION SPECIFICATION

**Protocol**: StateShift Deterministic Reference Solution Parser  
**Target Benchmark**: MATH-500 Decontaminated Primary Pool ($N=471$)  

---

## 1. Boundary Grammar & Segmentation Rules

1. **Paragraph/Block Boundary**: Split on double newlines `\n\n`.
2. **Displayed Equation Boundary**: Split at `\[ ... \]` block boundaries.
3. **Derivation Keyword Boundary**: Split prior to explicit sentence-initial markers (`First,`, `Next,`, `Then,`, `Thus,`, `Hence,`, `Therefore,`, `We have,`, `So,`, `Finally,`).
4. **Prose Boundary**: Do NOT split prose fragments inside inline math expressions `$ ... $`.

---

## 2. Operation Type Taxonomy

- `EQUATION_DERIVATION`: Step containing explicit equality `$A = B$` or logical implication.
- `ALGEBRAIC_SIMPLIFICATION`: Step performing term reduction or arithmetic evaluation.
- `SUBSTITUTION`: Step plugging numerical or variable values into target equations.
- `CONCEPTUAL_PROSE`: Explanatory reasoning sentence describing solution logic.
- `FINAL_ANSWER`: Concluding sentence containing `\\boxed{...}` or final value wrapper.

---

## 3. Yield Statistics

- **Total Primary Pool Problems Analyzed**: `471`
- **Total Segmented Steps**: `2362`
- **Mean Steps Per Problem**: `5.01`
- **Problems with $\ge 2$ Valid Steps**: `404` (`85.8%`)

---
