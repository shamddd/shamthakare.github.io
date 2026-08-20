# PRESERVED SCOPED RESULT RECORD: EXPERIMENT E0

**Date**: August 16, 2026  
**SHA-256 Manifest**: `E0_MANIFEST_SHA256.json`  

---

## 1. IMMUTABLE CONFIRMATORY EXPERIMENTAL RECORD ($E_0$)

Experiment $E_0$ is preserved as an immutable empirical observation:

* **Scope**: Evaluated strictly within the synthetic `ModComp` compositional reasoning environment.
* **Model Families**: 3 independently pretrained instruction/chat-tuned families (`SmolLM2-360M-Instruct`, `Qwen2.5-0.5B-Instruct`, `TinyLlama-1.1B-Chat-v1.0`).
* **Training Seeds**: 2 RL training seeds per model family.
* **Empirical Search Cap**: Best-of-$N$ evaluated empirically up to $N \le 32$.
* **Protocol Compliance & Dual Reporting**:
  - **Dataset A**: All six completed training runs; 3 model families $\times$ 2 seeds/family (includes the +5.17% overrun on Run 6 at 12.62 MPS-hours).
  - **Dataset B**: Five runs completed within the preregistered 12.00 MPS-hour ceiling; 3 model families represented (2 seeds for SmolLM2, 2 seeds for Qwen2.5, 1 seed for TinyLlama).
* **Observed Effect**: Directional criterion $R_f < 1.0$ observed across all three families ($R_{\text{SmolLM2}} = 0.0632$, $R_{\text{Qwen}} = 0.0648$, $R_{\text{TinyLlama}} = 0.0576$, Geometric Mean $\bar{R}_f = 0.0618$).

### Mandatory Scoped Reporting Language:
> *"Within the tested synthetic compositional reasoning environment and three evaluated instruction/chat-tuned model families..."*
