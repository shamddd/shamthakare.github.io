# PHASE 2 STAGE C0 — EVENT COUNT PRECISION TARGETS & THRESHOLDS

**Milestone**: Prospective Event Count Feasibility Thresholds  

---

## 1. Binomial Precision vs. Error Denominator ($E$)

| Qualifying Error Episodes ($E$) | Expected 95% CI Width (at $p \approx 0.20$) | Feasibility Classification | Publication Claim Capability |
| :---: | :---: | :---: | :--- |
| **$E < 30$** | $> \pm 17.5\%$ | **`INSUFFICIENT`** | `PILOT_ONLY` (Denominator too small for inference) |
| **$30 \le E < 100$** | $\pm 8.0\% \dots \pm 14.0\%$ | **`MARGINAL`** | `PASS_WITH_LIMITATIONS` (Descriptive post-error recovery) |
| **$E \ge 100$** | $< \pm 7.8\%$ | **`ADEQUATE`** | `PASS` (Empirical Natural Post-Error Recovery Enabled) |

---

## 2. Gate Decision Rules

* **ADEQUATE ($E \ge 100$)**: Natural Post-Error Recovery claim is `ENABLED`.
* **MARGINAL ($30 \le E < 100$)**: Natural Post-Error Recovery is `DESCRIPTIVE PILOT ONLY`.
* **INSUFFICIENT ($E < 30$)**: Insufficient natural errors observed to support statistical recovery estimation.

*Signed by Lead Statistical Methodologist & Adversarial Peer Reviewer*
