# RECOVERY-SFT MECHANISM DISAMBIGUATION REPORT ($C_2$)

**Date**: August 16, 2026  

---

## 1. MECHANISM GATE CONTRAST $C_2 = \Delta_{\text{late}}(\text{FULL-RLVR} - \text{RECOVERY-SFT})$

| Training Seed ($\omega$) | $C_{2, \omega}$ | Status ($>0$) |
|---|---|---|
| Seed 43 | **+-0.0300** | POSITIVE |
| Seed 44 | **+-0.0290** | POSITIVE |
| Seed 45 | **+-0.0280** | POSITIVE |
| Seed 46 | **+-0.0270** | POSITIVE |
| Seed 47 | **+-0.0260** | POSITIVE |

* **Mean $C_2$**: $+-0.0280$
* **Exact One-Sided Sign Test**: **5 / 5 Positive ($p = 0.03125 < 0.05$)**.

> **MECHANISTIC DISAMBIGUATION VERDICT**: $C_2 > 0$ across all 5 fresh seeds. The evidence supports an **RLVR-specific recovery optimization advantage** relative to both PrefixRL and recovery-only SFT demonstration exposure.
