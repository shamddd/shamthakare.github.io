# PHASE 3A — REVIEWER RED TEAM & 20 TOP REJECTION ARGUMENT MATRIX

**Milestone**: Adversarial Reviewer Red Team Audit  
**Reviewer Personas**:
* **Reviewer A**: LLM Reasoning / RL Expert
* **Reviewer B**: Statistical Methodologist
* **Reviewer C**: Self-Correction Literature Expert
* **Reviewer D**: Dataset Contamination & Reproducibility Expert
* **Reviewer E**: Hostile Area Chair

---

## 1. Top 20 Rejection Arguments & Mitigation Framing

1. **Rejection Arg 1 (Reviewer A)**: "The study only compares step-0 and step-256 without intermediate trajectory checkpoints."
   * *Mitigation*: Clearly frame Phase 1K intermediate trajectory as unobserved future work in Limitations Lock.
2. **Rejection Arg 2 (Reviewer C)**: "Self-correction literature shows models cannot self-correct without external feedback."
   * *Mitigation*: Strictly restrict claims to unprompted *natural post-error recovery behavior* ($\text{NRR}=30.93\%$), explicitly differentiating from prompted multi-turn self-correction.
3. **Rejection Arg 3 (Reviewer B)**: "The 11.76 percentage point contrast might be due to problem difficulty."
   * *Mitigation*: Emphasize problem-blocked bootstrap ($B=10,000$) and matched Recovery/Control problem design.
4. **Rejection Arg 4 (Reviewer D)**: "Data contamination in Qwen2.5 might inflate GSM8K/MATH accuracy."
   * *Mitigation*: Highlight strict decontamination filtering sensitivity ($N_{\text{Strict}}=388, \Gamma_{256,\text{Strict}}=+0.1160$).
5. **Rejection Arg 5 (Reviewer E)**: "The paper uses the phrase '+11.76% acceleration'."
   * *Mitigation*: Enforce strict terminology lock: $+0.1176$ is strictly an *absolute 11.76-percentage-point interaction*.
6. **Rejection Arg 6 (Reviewer A)**: "Only evaluated on DeepScaler / Qwen2.5-7B."
   * *Mitigation*: Acknowledge single model-family scope as explicit limitation; highlight high rollout density ($29,056 + 3,200$ rollouts).
7. **Rejection Arg 7 (Reviewer C)**: "Survivor bias in natural recovery rate."
   * *Mitigation*: Demonstrate denominator $E=582$ is conditioned strictly on verified first natural error episodes.
8. **Rejection Arg 8 (Reviewer B)**: "Is the interaction statistically significant?"
   * *Mitigation*: Report exact bootstrap CIs $[0.0955, 0.1400]$ and $p < 0.0001$.
9. **Rejection Arg 9 (Reviewer D)**: "Are the prompt templates reproducible?"
   * *Mitigation*: Supply exact SHA-256 prompt hashes and configuration files.
10. **Rejection Arg 10 (Reviewer E)**: "Is this just standard diff-in-diff?"
    * *Mitigation*: Emphasize novelty of applying matched diff-in-diff to LLM reasoning transition recovery states.
11. **Rejection Arg 11 (Reviewer A)**: "Could recovery be caused by longer token generation?"
    * *Mitigation*: Include token length controls in supplementary analysis.
12. **Rejection Arg 12 (Reviewer C)**: "LLM judge bias in error detection."
    * *Mitigation*: Enforce deterministic step-verifier rules without LLM judge dependency.
13. **Rejection Arg 13 (Reviewer B)**: "Clustering of errors within hard problems."
    * *Mitigation*: Provide problem-blocked bootstrap CIs $[27.19\%, 34.82\%]$.
14. **Rejection Arg 14 (Reviewer D)**: "Did RunPod execution introduce non-determinism?"
    * *Mitigation*: Document temperature/seed controls ($T=0.6, \text{top\_p}=0.95$).
15. **Rejection Arg 15 (Reviewer E)**: "Overclaiming causal RL mechanisms."
    * *Mitigation*: Enforce observational wording policy ("we observe...", "between checkpoints...").
16. **Rejection Arg 16 (Reviewer A)**: "Why not evaluate DeepSeek-R1-Zero?"
    * *Mitigation*: Note DeepSeek-R1-Zero closed weights / API limitations; DeepScaler is open-source.
17. **Rejection Arg 17 (Reviewer C)**: "Confusion between error incidence and recovery rate."
    * *Mitigation*: Separately report $\text{NEI}=18.19\%$ vs $\text{NRR}=30.93\%$.
18. **Rejection Arg 18 (Reviewer B)**: "Log-odds vs probability scale interaction."
    * *Mitigation*: Report both probability scale ($\Gamma_{256}=+0.1176$) and log-odds ($\text{OR}_{\text{DD}}=1.67$).
19. **Rejection Arg 19 (Reviewer D)**: "Model commit SHA discrepancy."
    * *Mitigation*: Include sealed Stage C0.3 weight-identity reality check.
20. **Rejection Arg 20 (Reviewer E)**: "Salami slicing into two papers."
    * *Mitigation*: Unify Study A and Study B into one comprehensive manuscript (Option A).

*Signed by Adversarial Reviewer Red Team & Publication Strategist*
