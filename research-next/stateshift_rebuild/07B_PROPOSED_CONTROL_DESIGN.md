# PROPOSED COUNTERFACTUAL CONTROL DESIGN

**Project**: StateShift Scientific Rebuild  
**Author**: Sham Satish Thakare  

---

## 1. Six-Arm Counterfactual Control Protocol

To rigorously separate **state-conditioned recovery** from generic **prefix robustness**, the rebuilt StateShift framework introduces a 6-arm counterfactual prefix control protocol:

```
                                  [Problem Prompt]
                                         │
        ┌───────────────────┬────────────┼────────────┬───────────────────┐
        ▼                   ▼            ▼            ▼                   ▼
    Condition R        Condition C   Condition S   Condition I        Condition Direct
  [Invalid Step]      [Valid Step]   [Shuffled]   [Irrelevant]         [No Prefix]
```

### Protocol Specifications:

| Condition Arm | Injected Prefix Description | Primary Target | Diagnostic Purpose |
| :--- | :--- | :--- | :--- |
| **Arm 1: Recovery ($R$)** | Injected prefix containing a verifier-confirmed invalid step. | Measure $\mu_{R,t}$ | Core recovery capability under invalid reasoning state. |
| **Arm 2: Matched Control ($C$)** | Length- and step-matched valid intermediate reasoning step. | Measure $\mu_{C,t}$ | Primary baseline for calculating difference-in-differences $\Gamma_t$. |
| **Arm 3: Shuffled Prefix ($S$)** | Shuffled tokens of the invalid reasoning step. | Measure $\mu_{S,t}$ | **Tests Null 2**: Distinguishes structural error recovery from token noise robustness. |
| **Arm 4: Irrelevant Prefix ($I$)** | Length-matched neutral English prose (non-math). | Measure $\mu_{I,t}$ | **Tests Null 6**: Controls for context length distraction. |
| **Arm 5: Alternate Error ($A$)** | Syntactically valid but semantically unrelated math error. | Measure $\mu_{A,t}$ | Tests error-type specificity. |
| **Arm 6: Direct Decoding ($D$)** | Zero prefix (raw prompt only). | Measure $\mu_{D,t}$ | Standard unprompted benchmark accuracy ($\text{Acc}_t$). |

---

## 2. Mathematical Diagnostic Estimands

1. **Primary Interaction Contrast ($\Gamma_t$)**:

$$\Gamma_t = (\mu_{R,t} - \mu_{R,0}) - (\mu_{C,t} - \mu_{C,0})$$

2. **Recovery Specificity Contrast ($\Delta \Gamma_t^{\text{spec}}$)**:

$$\Delta \Gamma_t^{\text{spec}} = (\mu_{R,t} - \mu_{R,0}) - (\mu_{S,t} - \mu_{S,0})$$

> **Falsification Invariant**: If $\Delta \Gamma_t^{\text{spec}} > 0$ with statistical significance ($p < 0.01$), the model's gain is **recovery-specific** and cannot be explained by generic prefix noise robustness.

*Signed by Lead Experimentalist & Statistical Methodologist*
