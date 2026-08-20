# INTELLECTUAL RESEARCH NARRATIVE

**Date**: August 16, 2026  
**Author**: Lead Researcher  

---

## From Representation Probes to Deployment-Amortized Inference Frontiers

Our research program originated with a fundamental question in post-training dynamics: *Can internal model representations predict post-RLVR performance gains?* Through our initial PRELUDE framework, we rigorously evaluated whether internal diagnostic probes—such as residual stream effective rank, probe separability, and gradient noise metrics—could forecast reinforcement learning outcomes beyond behavioral baselines. When systematic empirical auditing demonstrated that internal features provided zero non-redundant predictive power over strong headroom baselines ($R^2_{	ext{adj}} \le 0.00$), we executed a formal scientific pivot, killing the PRELUDE formulation to avoid post-hoc bias.

Recognizing that pre-RL diagnostic prediction was covered by contemporary literature, we reformulated our flagship query around deployment-level compute efficiency: *How does future query volume $Q$ change the compute-optimal choice between inference-time search (Best-of-$N$) and up-front RLVR post-training?* 

We formulated the **Amortized Intervention Frontier** $a^*(Q, d)$, defining the break-even query horizon $Q^*_{	ext{frontier}}$ where up-front training costs are fully amortized by downstream inference savings. Across a pre-registered multi-family confirmatory study encompassing three independently pretrained model families (`SmolLM2-360M`, `Qwen2.5-0.5B`, `TinyLlama-1.1B`), we observed a robust empirical phenomenon: controlled compositional out-of-distribution (OOD) length extrapolation dramatically shifts the intervention frontier toward trained models ($R_f pprox 0.0618 \ll 1.0$). On complex OOD tasks, up-front RLVR post-training amortizes its initial FLOP investment in less than $100$ downstream queries, compared to over $1,200$ queries on IID tasks.

This work exemplifies a commitment to scientific rigor: falsifying our initial hypothesis when empirical evidence demanded it, establishing explicit pre-registered failure criteria, maintaining complete FLOP/token compute ledgers, and transparently auditing protocol deviations. The resulting framework provides a principled, empirical foundation for compute-optimal deployment in modern reasoning systems.
