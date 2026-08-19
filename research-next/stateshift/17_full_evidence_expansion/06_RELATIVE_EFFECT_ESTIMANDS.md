# PHASE 2 STAGE A — RELATIVE EFFECT ESTIMANDS SPECIFICATION

**Milestone**: Prospective Relative Effect Estimand Definitions  

---

## 1. Primary Empirical Contrast (Immutable Baseline)

The primary frozen estimand remains the absolute difference-in-differences contrast on the probability scale:

$$\Gamma_{256} = (\mu_{R,256} - \mu_{R,0}) - (\mu_{C,256} - \mu_{C,0}) = +0.1176 \quad (+11.76 \text{ percentage points})$$

---

## 2. Secondary Relative Estimands

1. **Endpoint Relative Risk ($RR_{256}$)**:
   $$RR_{256} = \frac{\mu_{R,256}}{\mu_{C,256}} = \frac{0.7039}{0.5921} = \mathbf{1.1888} \quad (95\% \text{ CI } [1.1420, 1.2375])$$
   *Interpretation*: Target-transition success at step 256 is $1.189 \times$ higher in Recovery than Control ($18.88\%$ relative risk increase).

2. **Ratio of Condition Gains ($\text{RRG}$)**:
   $$\text{RRG} = \frac{\Delta_R}{\Delta_C} = \frac{0.3205}{0.2029} = \mathbf{1.5796} \quad (95\% \text{ CI } [1.4120, 1.7750])$$
   *Interpretation*: The absolute gain in Recovery target-transition success is $1.58 \times$ larger than the gain in matched Control.

3. **Log-Odds State-by-Checkpoint Interaction ($\text{OR}_{\text{DD}}$)**:
   $$\text{OR}_{\text{DD}} = \frac{\text{Odds}(R,256) / \text{Odds}(R,0)}{\text{Odds}(C,256) / \text{Odds}(C,0)} = \frac{(0.7039 / 0.2961) / (0.3834 / 0.6166)}{(0.5921 / 0.4079) / (0.3892 / 0.6108)} = \mathbf{1.6745}$$

*Signed by Lead Statistical Methodologist & Technical Editor*
