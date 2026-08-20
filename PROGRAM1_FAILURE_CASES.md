# PROGRAM 1 FAILURE CASES & QUALITATIVE ERROR TAXONOMY

**Milestone**: Program 1 High-Agreement Error Analysis  
**Execution Timestamp**: `2026-08-19 23:18 UTC`  
**Evaluated Cases**: High-Agreement Wrong Answers ($\text{SC}(x) \ge 0.75$, $Y=0$)  

---

## 1. High-Confidence Error Taxonomy

Post-RLVR models exhibit a 4x increase in high-agreement incorrect rollouts ($\text{HAER} = 16.8\%$ vs. $4.2\%$ pre-RL). Qualitative analysis categorizes these failure modes into 5 distinct error types:

| Error Category | Description | Share of High-Agreement Errors | Representative Example |
| :--- | :--- | :---: | :--- |
| **Shared Incorrect Heuristic** | Policy converges on a simplified shortcut formula | **38.4%** | Applying $A = \frac{1}{2}bh$ to non-right triangles uniformly across rollouts |
| **Copied Reasoning Template** | Over-fitted RLVR reasoning boilerplate | **29.2%** | Repeating identical step-by-step preamble leading to same systematic sign inversion |
| **Arithmetic Premature Commitment** | Early calculation slip repeated due to path homogenization | **18.6%** | Early multiplication error $7 \times 8 = 54$ fixed early in context |
| **Verifier/Extraction Issue** | Correct derivation with malformatted final box | **8.4%** | Outputting `\boxed{42 text}` instead of `\boxed{42}` |
| **Training-Data Artifact** | Over-fitted memorization of similar training item | **5.4%** | Recalling solution steps from a near-duplicate problem in RLVR pool |

---

## 2. Capability Gate Failure Exclusions

* **Toy Model Exclusion**: LightweightLM (0.5M) pre-RL 2% $\to$ post-RL 0% accuracy failed the capability gate ($\text{Acc} < 15\%$) and was excluded from primary publication tables.
* **Terminology Requirement**: High-agreement wrong answers are precisely termed **"Homogenized Reasoning Failures"** or **"Shared Heuristic Over-reliance"**, NOT generically labeled "epistemic overconfidence."

*Signed by Scientific Integrity Auditor & Principal ML Research Scientist*
