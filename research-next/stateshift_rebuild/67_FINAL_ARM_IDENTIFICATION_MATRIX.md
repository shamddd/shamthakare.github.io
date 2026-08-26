# PHASE 7 COUNTERFACTUAL ARM IDENTIFICATION MATRIX

**Project**: StateShift Scientific Rebuild — Phase 7A  
**Author**: Sham Satish Thakare  

---

## 1. Seven-Arm Counterfactual Protocol Specification

To establish complete causal identification on the new `GSM8K` test dataset ($N_{\text{new}}=500$ untouched problems), Phase 7 adopts a 7-arm counterfactual control design:

| Arm Code | Arm Description | Injected Prefix Specification | Primary Causal Contrast | Diagnostic Purpose |
| :---: | :--- | :--- | :--- | :--- |
| **Arm R** | **Target Invalid Step** | Verifier-confirmed invalid step for target GSM8K problem. | Base for $\Gamma_t^{\text{spec}}$ | Measures recovery under target error state. |
| **Arm C** | **Matched Valid Step** | Length- and step-matched valid step for target problem. | Contrast $\Gamma_t^{R:C}$ | Primary baseline for diff-in-diff contrast. |
| **Arm S** | **Shuffled Step** | Reordered tokens of target invalid step. | Contrast $\Gamma_t^{R:S}$ | Controls for token noise robustness. |
| **Arm A1** | **Same-Problem Alt Error** | Alternate invalid step for target problem. | Contrast $\Gamma_t^{R:A1}$ | Tests error-instance specificity. |
| **Arm A2** | **Other-Problem Math Error**| Invalid math step from a different GSM8K problem. | Contrast $\Gamma_t^{R:A2}$ | Controls generic math error tolerance. |
| **Arm P** | **Valid Irrelevant Math** | Valid math step from a different GSM8K problem. | Contrast $\Gamma_t^{R:P}$ | Controls math-domain context robustness. |
| **Arm D** | **Direct Benchmark** | Zero prefix (raw prompt only). | Contrast $G_t^D$ | Estimates aggregate benchmark gain ($\text{Acc}_t$). |

---

## 2. Empirical Verification Mandate

Every single cell ($500 \text{ problems} \times 16 \text{ rollouts} \times 7 \text{ arms} \times 2 \text{ checkpoints} = \mathbf{112,000\ rollouts}$) will be empirically generated from raw LLM inference runs. Zero values will be simulated, derived, or imputed.

*Signed by Methodological Lead & Principal Investigator*
