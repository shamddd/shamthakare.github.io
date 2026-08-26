# PHASE 6 GENUINE PROSPECTIVE EXPERIMENTAL PROTOCOL (FROZEN)

**Project**: StateShift Scientific Rebuild — Phase 6  
**Author**: Sham Satish Thakare (Independent Researcher, Pune, Maharashtra, India)  
**Protocol Version**: `v3.0-prospective-confirmatory`  
**Git Safety Anchor**: `51ca0a71d50fbdd673eb5d594bf987678fd304dc`  
**Freeze Tag**: `stateshift-v3-prospective-frozen`  
**Freeze Timestamp**: `2026-08-27T00:03:00+05:30` (IST)  

---

## 1. Frozen Primary Research Question & Estimand

* **Primary Research Question**:
  > *"During ordinary reasoning-oriented RL post-training, does robustness to a problem-matched invalid reasoning context improve disproportionately relative to robustness to matched valid, semantically disrupted, alternate mathematical error, unrelated mathematical, and direct decoding contexts?"*

* **Primary Estimand ($\Gamma_{256}^{R:C}$)**:

$$\Gamma_{256}^{R:C} = (p_{R,256} - p_{R,0}) - (p_{C,256} - p_{C,0})$$

* **Key Secondary Contrasts**:
  * $\Gamma_{256}^{R:S} = (p_{R,256} - p_{R,0}) - (p_{S,256} - p_{S,0})$
  * $\Gamma_{256}^{R:A1} = (p_{R,256} - p_{R,0}) - (p_{A1,256} - p_{A1,0})$
  * $\Gamma_{256}^{R:A2} = (p_{R,256} - p_{R,0}) - (p_{A2,256} - p_{A2,0})$
  * $\Gamma_{256}^{R:P} = (p_{R,256} - p_{R,0}) - (p_{P,256} - p_{P,0})$

---

## 2. Experimental Design Specifications

* **Model Lineage**: `UWNSL/Qwen2.5-7B-deepscaler` (Base: $t=0$, Endpoint: $t=256$).
* **Evaluation Population**: Untouched Prospective Confirmatory Cohort ($N_{\text{conf}} = 254$ held-out problems).
* **Rollout Depth**: $K = 16$ rollouts per arm/cell.
* **Intervention Arms**: 7 Arms ($R, C, S, A_1, A_2, P, D$).
* **Total Confirmatory Rollouts**: $254 \times 16 \times 7 \times 2 = \mathbf{56,896\ rollouts}$.
* **Primary Statistical Inference**: Problem-blocked hierarchical mixed-effects logistic regression and problem-blocked bootstrap ($B=10,000$).

---

## 3. Cryptographic Provenance Manifest

| Artifact File | Expected Path | SHA-256 Checksum Hash |
| :--- | :--- | :--- |
| **Untouched Registry** | `artifacts/stateshift_v2/provenance/untouched_confirmatory_registry.json` | `e7f9208a19b4c02e5d718429188d304210e4785f096238ab8240a1b947c610e2` |
| **Protocol Document** | `research-next/stateshift_rebuild/42_PHASE6_PROSPECTIVE_PROTOCOL.md` | `a3b8910c4f82...` |

*Signed by Principal Investigator & Lead Statistician*
