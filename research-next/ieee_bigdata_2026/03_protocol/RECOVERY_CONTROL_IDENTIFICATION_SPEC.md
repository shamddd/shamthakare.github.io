# RECOVERY & CONTROL STATE IDENTIFICATION SPECIFICATION

**Date**: August 16, 2026  

---

## 1. FORMAL STATE DEFINITIONS

* **Recovery State ($S_R$)**: A reasoning trajectory prefix state $s = (q, t_1, \dots, t_k)$ following an incorrect reasoning step ($t_k$ marked invalid by verifier) where a valid corrective continuation path remains mathematically accessible.
* **Control State ($S_C$)**: A reasoning trajectory prefix state $s = (q, t_1, \dots, t_k)$ originating from an unperturbed, valid step ($t_k$ marked valid by verifier) from the same `reasoning_operation_type` and matched structural complexity class.

## 2. PROVENANCE TAXONOMY

* `CONTROLLED_PERTURBATION_RECOVERY`: Recovery state constructed via verified perturbation of reference solution step.
* `REFERENCE_CONTROL`: Unperturbed reference solution step state.
