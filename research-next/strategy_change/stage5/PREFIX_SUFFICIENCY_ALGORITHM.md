# PREFIX SUFFICIENCY ENUMERATION ALGORITHM ($PS_k$)

**Date**: August 16, 2026  

---

## 1. ALGORITHM SPECIFICATION

Let $\mathcal{H}_k(x)$ be the finite, completely enumerated set of legal length-$k$ environment histories for problem $x$.

$$PS_k(x) = \max_{h \in \mathcal{H}_k(x)} \mathbb{P}_{\pi_{\text{base}}}\left(\text{Success} \,\Big|\, do(H_k = h)\right)$$

Algorithm enumerates all valid $h \in \mathcal{H}_k(x)$ and evaluates base model continuation success under exact environment steering.
