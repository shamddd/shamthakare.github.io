# PHASE 6 ARM IDENTIFICATION AND CONTROL DESIGN ANALYSIS

**Project**: StateShift Scientific Rebuild — Phase 6  
**Author**: Sham Satish Thakare  

---

## 1. Seven-Arm Counterfactual Protocol Specification

To achieve complete causal identification separating **target-specific recovery** from **generic math error tolerance** and **math-domain context robustness**, Phase 6 adopts a 7-arm counterfactual control design:

| Arm Code | Arm Description | Injected Prefix Specification | Primary Causal Contrast | Diagnostic Purpose |
| :---: | :--- | :--- | :--- | :--- |
| **Arm R** | **Target Invalid Step** | Verifier-confirmed invalid step for target problem. | Base for $\Gamma_t^{\text{spec}}$ | Measures recovery under target error state. |
| **Arm C** | **Matched Valid Step** | Length- and step-matched valid step for target problem. | Contrast $\Gamma_t^{R:C}$ | Primary baseline for diff-in-diff contrast. |
| **Arm S** | **Shuffled Step** | Reordered tokens of target invalid step. | Contrast $\Gamma_t^{R:S}$ | Controls for token noise robustness. |
| **Arm A1** | **Same-Problem Alt Error** | Alternate invalid step for target problem. | Contrast $\Gamma_t^{R:A1}$ | Tests error-instance specificity. |
| **Arm A2** | **Other-Problem Math Error**| Invalid math step from a different problem. | Contrast $\Gamma_t^{R:A2}$ | Controls generic math error tolerance. |
| **Arm P** | **Valid Irrelevant Math** | Valid math step from a different problem. | Contrast $\Gamma_t^{R:P}$ | Controls math-domain context robustness. |
| **Arm D** | **Direct Benchmark** | Zero prefix (raw prompt only). | Contrast $G_t^D$ | Estimates aggregate benchmark gain ($\text{Acc}_t$). |

---

## 2. Decision on 7-Arm Expansion

$$\mathbf{Arm\ Decision:\ ADD\_P\_ARM\_AND\_A2\_ARM\ (7\text{-}Arm\ Full\ Design)}$$

### Scientific Justification:
* **Arm P (Valid Irrelevant Math)** separates mathematical domain context from semantic problem relevance.
* **Arm A2 (Other-Problem Error)** separates target-specific error recovery from generic tolerance of erroneous math text.
* **Compute Feasibility**: On $N_{\text{conf}}=254$ held-out problems at $K=16$ rollouts per arm across 2 endpoints ($t=0, 256$), total required rollouts $= 254 \times 16 \times 7 \times 2 = \mathbf{56,896\ rollouts}$. Fully executable within available compute.

*Signed by Methodological Lead & Principal Investigator*
