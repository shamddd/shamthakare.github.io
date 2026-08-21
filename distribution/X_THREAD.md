# X / Twitter Research Thread (6 Posts)

---

### Post 1 / 6
When does an internal uncertainty metric measure true model uncertainty—and when is it simply measuring sequence completion length?

In RLVR for mathematical reasoning (GRPO), weighting advantages by token predictive entropy is often assumed to suppress incorrect derivations.

Here is what we found: 🧵

---

### Post 2 / 6
1/ Sequence Length Confounding: On GSM8K ($N = 100$ prompt clusters), token predictive entropy was positively correlated with completion token length ($r = 0.486, 95\%\text{ CI } [+0.318, +0.627]$).

Longer multi-step reasoning traces naturally accumulate higher token entropy than short single-step recall.

---

### Post 3 / 6
2/ Partial Correlation Collapse: Controlling for sequence length decreased the association between token entropy and mathematical error from $r = -0.214$ to $r_{\text{partial}} = -0.092$ ($p = 0.365$).

Token entropy operates primarily as a proxy for sequence length rather than correctness.

---

### Post 4 / 6
3/ Compute Graph Audit: Auditing `Qwen2.5-0.5B-Instruct` revealed 0 active `nn.Dropout` modules ($p=0.0$).

Nominal MC-dropout passes yielded deterministic passes ($\text{Var}(\log P) = 0.0$), producing policy update vectors collinear to standard GRPO ($\cos(\Delta\theta) = 1.000000$).

---

### Post 5 / 6
4/ Preregistered RL Benchmark ($N = 3$ Seeds): Scaling advantages by self-consistency consensus (CA-GRPO) yielded Pass@1 of $80.00\% \pm 0.00\%$ across 3 seeds—showing zero observed advantage over standard outcome-supervised GRPO ($80.00\% \pm 0.00\%, d = 0.00$).

---

### Post 6 / 6
5/ Full technical research note with visual interactive explorables, figure provenance, working paper PDF, and open-source code repository:

Article: https://shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity/  
PDF: https://shamddd.github.io/shamthakare.github.io/pdfs/ear-grpo-reasoning.pdf  
Code: https://github.com/shamddd/ear_grpo_reasoning  
