# ROLLOUT AGGREGATION & PROBLEM-LEVEL ESTIMAND SPECIFICATION

**Independent Resampling Unit**: Problem $i \in \{1, \dots, N\}$ ($N=365$)  
**Rollout Parameter**: $K = 16$ stochastic rollouts per state per checkpoint  

---

## 1. Rollout Aggregation

For every problem $i$, state type $g \in \{R, C\}$, and checkpoint $t$:
Let $Y_{i,g,t,k} \in \{0, 1\}$ denote the primitive verifier outcome for stochastic rollout $k \in \{1, \dots, K\}$.

The problem-state-checkpoint mean success rate is:
$$\bar{Y}_{i,g,t} = \frac{1}{K} \sum_{k=1}^{K} Y_{i,g,t,k}$$

> [!NOTE]
> Stochastic rollouts $k$ are **repeated measurements** nested within problem $i$, NOT independent observations.

---

## 2. Problem-Level Interaction $\gamma_{i,t}$

The problem-level checkpoint-change interaction for problem $i$ at checkpoint $t$ is:

$$\gamma_{i,t} = \left(\bar{Y}_{i,R,t} - \bar{Y}_{i,R,0}\right) - \left(\bar{Y}_{i,C,t} - \bar{Y}_{i,C,0}\right)$$

The sample-wide interaction estimator is:

$$\Gamma_t = \frac{1}{N} \sum_{i=1}^{N} \gamma_{i,t}$$

And primary scalar endpoint at final checkpoint $T=256$:

$$\Gamma_T = \frac{1}{N} \sum_{i=1}^{N} \gamma_{i,T}$$

---
