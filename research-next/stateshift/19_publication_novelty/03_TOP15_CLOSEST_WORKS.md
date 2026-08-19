# PHASE 3A — TOP 15 CLOSEST PRIOR WORKS AUDIT & DISTINCTIONS

**Milestone**: In-Depth Comparison with Top 15 Closest Scholarly Publications  

---

## 1. DeepSeekMath (Shao et al., 2024)
* **Focus**: Introduces Group Relative Policy Optimization (GRPO) for math RL.
* **StateShift Distinction**: DeepSeekMath reports overall benchmark accuracy. StateShift measures the state-selective interaction ($\Gamma_{256} = +0.1176$) comparing matched Recovery vs Control baseline states.

## 2. DeepSeek-R1 (DeepSeek-AI, 2025)
* **Focus**: Demonstrates emergent long CoT reasoning capabilities via pure RL.
* **StateShift Distinction**: DeepSeek-R1 evaluates raw accuracy and CoT length. StateShift isolates target-transition capability under controlled locally invalid perturbations.

## 3. DeepScaler (Luo et al., 2025)
* **Focus**: Fine-tunes Qwen2.5-7B using long-context RLVR.
* **StateShift Distinction**: DeepScaler provides the underlying checkpoint series. StateShift evaluates state-selective recovery contrast and natural error incidence ($\text{NEI}=18.19\%$, $\text{NRR}=30.93\%$).

## 4. Training LLMs to Self-Correct (Kumar et al., 2024)
* **Focus**: Evaluates intrinsic self-correction under specific SFT/RL pipelines.
* **StateShift Distinction**: Kumar et al. evaluate prompted self-correction. StateShift Study B measures unprompted natural post-error recovery conditional on verified endogenous error events.

## 5. Can LLMs Really Self-Correct Without Feedback? (Huang et al., 2023)
* **Focus**: Argues LLMs cannot self-correct reasoning without external feedback.
* **StateShift Distinction**: Huang et al. evaluate prompted self-correction retries. StateShift Study B measures autonomous recovery in single unperturbed rollouts.

## 6. Large Language Models Cannot Self-Correct Reasoning Yet (Stechly et al., 2024)
* **Focus**: Demonstrates performance drops under self-critique.
* **StateShift Distinction**: Stechly et al. focus on critique-prompted decoding. StateShift evaluates free unperturbed decoding recovery.

## 7. Let Us Verify Step by Step (Lightman et al., 2023)
* **Focus**: Introduces step-level PRMs for verification.
* **StateShift Distinction**: Lightman et al. use PRMs to guide search. StateShift uses deterministic step verification to evaluate transition probability shifts.

## 8. Solving Math Problems with Process-Based Feedback (Uesato et al., 2022)
* **Focus**: Compares outcome vs process supervision.
* **StateShift Distinction**: Uesato et al. evaluate training reward signals. StateShift evaluates state-by-checkpoint interaction.

## 9. Qwen2.5 Technical Report (Yang et al., 2024)
* **Focus**: Base architecture and pretraining details for Qwen2.5.
* **StateShift Distinction**: Pretraining baseline provider.

## 10. Training Verifiers to Solve Math Word Problems (Cobbe et al., 2021)
* **Focus**: Verifier-guided rejection sampling on GSM8K.
* **StateShift Distinction**: Cobbe et al. use verifiers for reranking. StateShift measures internal autonomous recovery without reranking.

## 11. Self-Refine (Madaan et al., 2023) & 12. Reflexion (Shinn et al., 2023)
* **Focus**: Multi-turn verbal feedback and critique loops.
* **StateShift Distinction**: Requires external multi-turn critique prompts. StateShift evaluates single-turn unperturbed decoding.

## 13. STaR (Zelikman et al., 2022)
* **Focus**: Rationale bootstrapping via self-taught reasoner loop.
* **StateShift Distinction**: Focuses on post-training dataset filtering.

## 14. Chain-of-Thought Prompting (Wei et al., 2022) & 15. Zero-Shot Reasoners (Kojima et al., 2022)
* **Focus**: Initial CoT prompting paradigm.
* **StateShift Distinction**: Foundational prompting literature.

*Signed by Principal ML Research Scientist & Systematic Literature Review Lead*
