# LinkedIn Research Announcement

When does an internal uncertainty metric actually measure model uncertainty—and when is it simply measuring sequence completion length?

In policy gradient post-training for mathematical reasoning (such as GRPO), researchers frequently weight rollout advantages by internal confidence signals—such as token predictive entropy—to suppress unreliable trajectories. The intuitive assumption is that incorrect derivations exhibit higher predictive variance than correct ones.

We audited this assumption across multi-step mathematical derivations on GSM8K ($N = 100$ prompt clusters, 98 degrees of freedom) using `Qwen2.5-0.5B-Instruct`.

Here is what the empirical evidence showed:

1. **Length Confounding**: Token predictive entropy was positively correlated with completion length ($r = 0.486, 95\%\text{ CI } [+0.318, +0.627]$). Longer, correct multi-step proofs naturally accumulate higher aggregate entropy than short, single-step recall.
2. **Partial Correlation Collapse**: Controlling for completion length decreased the association between token entropy and mathematical error from $r = -0.214$ to $r_{\text{partial}} = -0.092$ ($p = 0.365$, non-significant).
3. **Zero-Dropout Probing**: Auditing the model compute graph revealed 0 active `nn.Dropout` modules, causing nominal MC-dropout passes to yield mathematically deterministic passes ($\text{Var}(\log P) = 0.000000$).
4. **Preregistered RL Benchmark ($N = 3$ Seeds)**: Scaling advantages by self-consistency consensus (CA-GRPO) yielded an observed mean Group Pass@1 of $80.00\% \pm 0.00\%$ across 3 seeds—showing zero observed advantage over standard outcome-supervised GRPO ($80.00\% \pm 0.00\%$, Cohen's $d = 0.00$).

**Boundary**: These experiments evaluate `Qwen2.5-0.5B-Instruct`; they do not establish whether the same behavior holds at larger model scales or across other model families.

I compiled a visual research note detailing the diagnostic experiments, compute graph audits, negative controls, and open-source reproducibility artifacts.

• Interactive Article: https://shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity/  
• Working Paper PDF: https://shamddd.github.io/shamthakare.github.io/pdfs/ear-grpo-reasoning.pdf  
• Reproducible Code: https://github.com/shamddd/ear_grpo_reasoning  

#MachineLearning #ReinforcementLearning #LLM #AIResearch #PostTraining
