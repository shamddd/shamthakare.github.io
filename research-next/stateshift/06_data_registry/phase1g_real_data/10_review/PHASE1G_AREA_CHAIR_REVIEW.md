# PHASE 1G AREA-CHAIR SCIENTIFIC INTEGRITY REVIEW

**Reviewer Role**: Scientific Integrity Auditor & Research Statistician  
**Target Milestone**: Phase 1G Real Data Forensics & State Registry Gate  

---

## Response to Key Scientific & Integrity Questions

### 1. Is contamination sufficiently characterized?
**YES.** A 4-stage forensic matching protocol (Exact Text Hash, Structural Numeric Variant Hash, Token 3-gram Jaccard, and Edit Similarity Ratio) was executed against the primary RL training corpus (`DeepScaleR-Preview-Dataset`, 40,315 items) and benchmark lineage (`Omni-MATH`, 4,428 items). All collisions have been classified and excluded from the primary conservative pool.

### 2. Is base-model pretraining exposure correctly bounded?
**YES.** The manuscript explicitly distinguishes between verified RL-stage dataset overlap (which is 100% decontaminated in our primary pool) and unobserved base-model pretraining exposure. The evaluation pool is formally characterized as an RL-decontaminated evaluation benchmark.

### 3. Is the usable N meaningful?
**YES.** $N = 365$ independent, decontaminated, perturbation-eligible problems yield high statistical sensitivity (MDES of ~10.4% at 80% power), enabling rigorous hypothesis testing for checkpoint-trajectory interactions.

### 4. Are recovery states artificial but scientifically interpretable?
**YES.** Recovery states ($S_R$) are constructed via deterministic, single-operator perturbations (constant shift, sign flip, fraction invert) applied to reference solution steps. This isolates error-recovery mechanics under controlled, counterfactual conditions.

### 5. Is TARGET_TRANSITION_SUCCESS objective?
**YES.** Target transition success is defined independently of model outputs via SymPy / Python AST symbolic equivalence checks (`TARGET_TRANSITION_REGISTRY.json`), eliminating verifier bias.

### 6. Is segmentation reproducible?
**YES.** Solution segmentation follows an immutable specification (`MATH_STEP_SEGMENTATION_SPEC.md`) using deterministic block, equation, and syntactic boundary rules.

### 7. Does filtering introduce obvious selection bias?
**NO.** Filtering excludes only items with direct training collisions. Problem difficulty levels and mathematical domains (algebra, geometry, number theory, etc.) maintain representative distribution matching the original MATH-500 benchmark.

### 8. Would a null checkpoint interaction remain publishable?
**YES.** A null result (showing checkpoint trajectory independence under decontaminated recovery states) would be highly impactful, refuting common assumptions regarding RL trajectory learning.

---
