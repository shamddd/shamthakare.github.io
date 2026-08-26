# PHASE 6 CONFIRMATORY POPULATION PROVENANCE

**Project**: StateShift Scientific Rebuild — Phase 6  
**Author**: Sham Satish Thakare  

---

## 1. Evaluation Population Partition Strategy

To guarantee that Phase 6 confirmatory outcomes are evaluated on a genuinely untouched population, we establish a strict, immutable problem partition:

```
                              [MATH-500 Dataset (N=500)]
                                           │
         ┌─────────────────────────────────┴─────────────────────────────────┐
         ▼                                                                   ▼
Retrospective Discovery Set                                Untouched Prospective Confirmatory Set
    (N_disc = 200)                                                  (N_conf = 254)
[Used in Retrospective Study 1]                                 [FROZEN FOR PHASE 6 CONFIRMATORY]
```

### Partition Specifications:

| Partition Cohort | Problem Count ($N$) | Purpose | Provenance History | Status for Phase 6 |
| :--- | :---: | :--- | :--- | :--- |
| **Discovery Cohort** | $N=200$ | Retrospective phenomenon discovery | Examined in historical Study 1 / Study B | **`EXCLUDED FROM CONFIRMATORY`** |
| **Confirmatory Cohort** | $N=254$ | **Prospective Hypothesis Confirmation** | **Zero prior outcome inspection** | **`PRIMARY CONFIRMATORY POPULATION`** |
| **Dev / Pilot Cohort** | $N=46$ | Pipeline testing & prefix validation | Partitioned separately | **`DEV / PILOT ONLY`** |

---

## 2. Cryptographic Provenance Registry

The list of 254 untouched confirmatory problem IDs has been serialized to `artifacts/stateshift_v2/provenance/untouched_confirmatory_registry.json`.

$$\mathbf{Registry\ SHA256:\ e7f9208a19b4c02e5d718429188d304210e4785f096238ab8240a1b947c610e2}$$

*Signed by Data Integrity Officer & Principal Investigator*
