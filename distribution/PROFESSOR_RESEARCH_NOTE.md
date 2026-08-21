# Professor Research Note Template (Customizable)

Dear Professor [PROFESSOR_LAST_NAME],

I am Sham Satish Thakare, an independent computer science researcher studying reasoning calibration and credit assignment in LLM post-training. I read your recent paper, "[RECENT_PAPER_TITLE]," and noticed our shared interest in [EXACT_RESEARCH_CONNECTION].

I recently completed a diagnostic study investigating whether internal uncertainty estimators (such as token predictive entropy and MC-dropout) act as valid confidence proxies or sequence length proxies during RLVR post-training.

Benchmarking across GSM8K ($N = 100$ prompt clusters), token entropy correlated with completion length ($r = 0.486$), and controlling for length decreased the error association to $r_{\text{partial}} = -0.092$ ($p = 0.365$). In a preregistered 5-way controlled RL setup across $N=3$ training seeds, consistency-weighted advantage scaling produced zero observed performance delta ($d = 0.00$) over standard outcome-supervised GRPO.

Given your work on [EXACT_RESEARCH_CONNECTION], I thought this empirical failure mode might be relevant to your group's post-training experiments.

• Visual Research Essay: https://shamddd.github.io/shamthakare.github.io/writing/when-confidence-confounds-reasoning-complexity/  
• Working Paper PDF: https://shamddd.github.io/shamthakare.github.io/pdfs/ear-grpo-reasoning.pdf  
• Code Repository: https://github.com/shamddd/ear_grpo_reasoning  

Best regards,  
Sham Satish Thakare  
shamthakare3000@gmail.com  
https://shamddd.github.io/shamthakare.github.io/  
