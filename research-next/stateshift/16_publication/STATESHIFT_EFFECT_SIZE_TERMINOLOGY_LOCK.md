# STATESHIFT CANONICAL EFFECT-SIZE TERMINOLOGY LOCK

**Milestone**: Phase 1L.0 Publication Terminology Freeze  
**Lock Timestamp**: `2026-08-20 01:43 UTC`  
**Auditor**: Principal ML Research Scientist, Lead Statistical Methodologist, Scientific Integrity Auditor & Technical Editor  

---

## 1. Primary Estimand & Canonical Terminology

* **Primary Estimand Symbol**: $\Gamma_{256} = (\mu_{R,256} - \mu_{R,0}) - (\mu_{C,256} - \mu_{C,0})$
* **Primary Estimand Value**: $\Gamma_{256} = \mathbf{+0.1176}$
* **Primary 95% Bootstrap Confidence Interval ($B=10,000$)**: **`[+0.0955, +0.1400]`** ($p < 0.0001$)
* **Canonical Unit**: **Percentage Points** (Probability difference scale: $0.1176 \to 11.76$ percentage points).

### Authoritative Manuscript Wording:
> "From checkpoint $t=0$ to $t=256$, target-transition success increased by 11.76 percentage points more in the Recovery condition than in the matched Control condition ($\Gamma_{256} = 0.1176$, 95% bootstrap CI $[0.0955, 0.1400]$)."

### Alternative Concise Wording:
> "We observed a positive 11.76-percentage-point difference-in-differences interaction in target-transition success ($\Gamma_{256} = 0.1176$, 95% CI $[0.0955, 0.1400]$)."

---

## 2. Strict Contamination Sensitivity Estimand & Canonical Terminology

* **Strict Estimand Symbol**: $\Gamma_{256,\text{Strict}}$ ($N_{\text{Strict}} = 388$)
* **Strict Estimand Value**: $\Gamma_{256,\text{Strict}} = \mathbf{+0.1160}$
* **Strict 95% Bootstrap Confidence Interval**: **`[+0.0913, +0.1408]`** ($p < 0.0001$)

### Authoritative Strict Wording:
> "The strict contamination-filtered sensitivity analysis produced an 11.60-percentage-point interaction estimate ($\Gamma_{256,\text{Strict}} = 0.1160$; 95% CI $[0.0913, 0.1408]$)."

---

## 3. Explicitly Prohibited Terminology

The following expressions are scientifically imprecise (incorrectly treating an absolute probability difference as a relative percentage ratio) and are **STRICTLY PROHIBITED** in all manuscript text:

❌ `"+11.76% acceleration"`  
❌ `"11.76% recovery acceleration"`  
❌ `"+11.76% state-selective recovery acceleration"`  
❌ `"11.76 percent improvement"`  
❌ `"11.76% greater recovery"`  
❌ `"11.60% acceleration"`  
❌ `"11.60% improvement"`  

*Signed by Principal ML Research Scientist, Lead Statistical Methodologist, Scientific Integrity Auditor & Technical Editor*
