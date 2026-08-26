# CONSTRUCT VALIDITY AUDIT & CONCEPTUAL TAXONOMY

**Project**: StateShift Scientific Rebuild  
**Author**: Sham Satish Thakare  

---

## 1. Definition of the Observed Experimental Object

The StateShift experiment does **not** directly observe or manipulate internal model activations. Instead, the experimental manipulation consists of:

$$\mathbf{Manipulated\ Object:\ Externally\ Instantiated\ Behavioral\ Reasoning\ Context}$$

Specifically, the model is provided with a prompt appended with an intermediate text completion containing a verifier-confirmed mathematical error (Recovery Condition $R$) or a length- and context-matched valid step (Control Condition $C$). All observed outcomes measure target-transition answer correctness given these externally injected prefixes.

---

## 2. Formal State Taxonomy

To prevent conceptual ambiguity, StateShift establishes a five-tier state taxonomy:

| State Tier | Formal Definition | Observability | Existing StateShift Scope |
| :--- | :--- | :---: | :--- |
| **1. Prompt / Context State ($S_{\text{ctx}}$)** | The sequence of input tokens appended to the problem prompt prior to generation. | **Directly Observed** | **`PRIMARY`**: Manipulated via Recovery ($R$) vs Control ($C$) prefix injection. |
| **2. Behavioral Reasoning State ($S_{\text{beh}}$)** | Operational state inferred from observable text reasoning steps (e.g. valid vs invalid step). | **Directly Inferred** | **`PRIMARY`**: Inferred via deterministic sympy verifier on intermediate steps. |
| **3. Latent / Internal State ($S_{\text{lat}}$)** | Model hidden-state activations ($h_l \in \mathbb{R}^d$) across transformer layers. | **Unobserved** | **`OUT OF SCOPE`**: Not measured in original study. Requires internal probing. |
| **4. Training State ($S_{\text{train}}$)** | Optimization checkpoint position ($t \in \{0..256\}$) along the RL training trajectory. | **Directly Observed** | **`PRIMARY`**: Tracked across 9 discrete DeepScaler model checkpoints. |
| **5. Task / Computational State ($S_{\text{task}}$)** | The underlying mathematical ground-truth state of the problem derivation graph. | **Directly Observed** | **`PRIMARY`**: Verified against ground-truth target boxed answers. |

---

## 3. Formal Recovery Taxonomy

| Recovery Tier | Operational Definition | Empirical Support Status |
| :--- | :--- | :---: |
| **Answer Recovery** | Final target boxed answer is correct following an invalid intermediate prefix. | **`SUPPORTED`** ($\mu_{R,256} = 70.39\%$) |
| **Counterfactual Recovery** | Target-transition success is higher under Recovery condition than under matched Control after subtracting base baseline ($\Gamma_t > 0$). | **`SUPPORTED`** ($\Gamma_{256} = +0.1176$) |
| **Reasoning Recovery** | The generated text continuation returns to a valid mathematical derivation before producing the final answer. | **`PARTIALLY SUPPORTED`** (Requires step-level verifier audit on continuations) |
| **State Recovery** | An internal latent representation transitions back into a success-associated subspace. | **`UNSUPPORTED`** (Zero internal activation data) |
| **Mechanistic Recovery** | Demonstrable causal link between an internal error-detection circuit and correction steering. | **`UNSUPPORTED`** (Zero mechanistic circuit data) |

---

## 4. Five-Level Claim Ladder Audit

To ensure the rebuilt manuscript never makes claims exceeding empirical evidence, all statements are audited against a 5-level claim ladder:

```
Level 5: Post-training alters an internal error-recovery mechanism.  [UNSUPPORTED]
   │
Level 4: Post-training learns a distinct recovery capability.          [PARTIALLY SUPPORTED]
   │
Level 3: Post-training selectively increases recovery from invalid     [SUPPORTED]
         behavioral contexts (Γ_t > 0).
   │
Level 2: Post-training changes output probability following invalid   [SUPPORTED]
         versus valid prefixes.
   │
Level 1: Models can produce correct answers after invalid prefixes.   [SUPPORTED]
```

### Claim Ladder Evaluation:
* **LEVEL 1**: **`SUPPORTED`** — Base model achieves $38.34\%$ success after invalid prefix.
* **LEVEL 2**: **`SUPPORTED`** — Post-training increases $R$ success from $38.34\%$ to $70.39\%$ and $C$ success from $38.92\%$ to $59.21\%$.
* **LEVEL 3**: **`SUPPORTED`** — $\Gamma_{256} = +0.1176$ ($95\%$ CI $[+0.0955, +0.1400], p < 0.0001$).
* **LEVEL 4**: **`PARTIALLY SUPPORTED`** — Requires formal control for Null 1 (general capability gain) to prove recovery-specific learning.
* **LEVEL 5**: **`UNSUPPORTED`** — Forbidden in manuscript text until internal activation probing is executed.

*Signed by Principal Methodologist & Scientific Integrity Auditor*
