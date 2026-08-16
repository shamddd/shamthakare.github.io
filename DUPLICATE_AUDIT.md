# Duplicate Audit & Single Canonical Identity Ledger

**Candidate**: Sham Thakare (Sham Satish Thakare)  
**Advisory Role**: Research Integrity Auditor & Bibliometrics Specialist  

---

## 1. Audit Principles

1. **One Canonical Record**: Each distinct scientific contribution has exactly one canonical record (`WORK-01` through `WORK-06`).
2. **Version Linking**: Different versions of the same work (arXiv preprint, conference paper, GitHub repository, code release) are linked to the canonical record and NOT treated as separate research papers.
3. **Legacy Script Quarantining**: Exploratory software repositories (`Reinforcement-learning`) are categorized strictly as `Software Project / Archived` and excluded from paper indexes.

---

## 2. Cross-Repository & Publication Deduplication Matrix

```
========================================================================================================================
CANONICAL WORK ID  REPOSITORIES & MANUSCRIPTS INCLUDED                          DEDUPLICATION STATUS & ACTION
========================================================================================================================
WORK-01            - adaptive-rl-forge (Repo)                                  CLEAN. Single canonical identity.
                   - JMLR Paper (paper/jmlr/main.tex)                          JMLR submission intact.
WORK-02            - enclaveshield (Repo)                                     CLEAN. Single canonical identity.
                   - EnclaveShield Preprint (paper/enclaveshield_manuscript.tex)
WORK-03            - quorumshift (Repo)                                       CLEAN. Single canonical identity.
                   - AdaptiveReplica (CV: Distributed Storage Simulator)
WORK-04            - tracemind (Repo)                                         CLEAN. Single canonical identity.
                   - TraceMind (CV: Intelligent Cloud Observability Platform)
WORK-05            - secure-cloud-infrastructure-platform (Repo)             CLEAN. Research artifact prototype.
WORK-06            - medirush (Repo)                                          CLEAN. Preserved publication prep.
========================================================================================================================
```

---

## 3. Quarantined / Excluded Non-Paper Repositories

- `Reinforcement-learning`: Archived legacy learning scripts (2022). Action: Treat strictly as software code; do not list on Google Scholar.
- `github-portfolio-audit`: Internal audit tool directory. Action: Exclude from publication lists.
