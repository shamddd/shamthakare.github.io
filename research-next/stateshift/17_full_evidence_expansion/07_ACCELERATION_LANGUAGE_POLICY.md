# PHASE 2 STAGE A — ACCELERATION & RATE-OF-CHANGE LANGUAGE POLICY

**Milestone**: Prospective Terminology Policy for Rate-of-Change Quantities  

---

## 1. Absolute Rule on Primary Effect $\Gamma_{256}$

* **PROHIBITED WORDING**: $\Gamma_{256} = +0.1176$ MUST NEVER be referred to as "acceleration", "rate of change", or "relative percentage improvement".
* **CANONICAL WORDING**: $\Gamma_{256} = +0.1176$ is strictly an **`absolute 11.76-percentage-point difference-in-differences interaction on the probability scale`**.

---

## 2. Permitted Rate-of-Change Definitions (If Trajectory Data Exist)

If Phase 2 Stage B trajectory evaluation is executed, rate-of-change quantities are permitted ONLY under the following explicit discrete mathematical definitions:

1. **Discrete Rate of Change ($D_t$)**: $D_t = \Gamma_t - \Gamma_{t-32}$ (First difference across adjacent training steps).
2. **Discrete Second Difference ($A_t$)**: $A_t = D_t - D_{t-32}$ (Discrete change in rate of change across training steps).

*Allowed Terminology*: "Discrete second difference across training steps" or "change in interaction rate across checkpoints".

*Signed by Technical Editor & Scientific Integrity Auditor*
