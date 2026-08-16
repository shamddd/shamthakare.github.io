import os
import json

base_dir = "/Users/shamthakare/.gemini/antigravity/scratch"

# 1. Create research-profile.json
profile_data = {
    "name": "Sham Thakare",
    "canonical_name": "Sham Satish Thakare",
    "affiliation": "Independent Researcher",
    "bio_short": "Sham Thakare is an independent computer science researcher investigating trustworthy, adaptive, and verifiable autonomous systems across reinforcement learning plasticity, confidential hardware enclaves, distributed consensus adaptation, and cloud causal observability.",
    "bio_medium": "Sham Thakare is an independent computer science researcher specializing in the design, safety, and performance of adaptive autonomous systems. His research spans four primary pillars: diagnosing representation geometry and plasticity in reinforcement learning checkpoints prior to post-training alignment, engineering zero-knowledge remote attestation and dynamic access-frequency-weighted Oblivious RAM for confidential hardware enclaves, developing failure-aware dynamic quorum adaptation algorithms for fault-tolerant distributed consensus, and constructing graph-constrained topological causal reasoning engines over multi-modal cloud telemetry.",
    "bio_long": "Sham Thakare is an independent computer science researcher conducting systems and foundational research at the intersection of Artificial Intelligence, Systems Security, Distributed Systems, and Cloud Observability. His overarching research mission is to establish rigorous performance, safety, and verifiability guarantees for autonomous software operating in dynamic, non-stationary environments. Sham's current research program comprises four principal vectors: (1) Foundation Model Plasticity: Formulating representation geometry diagnostics to predict reinforcement-learning reward plasticity in intermediate language-model checkpoints without executing computationally expensive policy gradient training loops; (2) Confidential Computing: Designing Zero-Knowledge remote attestation membership proofs and access-frequency-weighted adaptive Oblivious RAM tree rebalancing algorithms for hardware enclaves; (3) Distributed Consensus: Developing AdaptiveReplica, a failure-domain aware dynamic quorum adaptation engine for Raft consensus clusters that eliminates tail latency under asymmetric node degradation; and (4) Causal Observability: Constructing TraceMind, a graph-constrained causal walk engine over OpenTelemetry microservice dependency graphs to achieve 100% Top-1 root cause localization accuracy. Committed to scientific integrity and open science, Sham releases all experimental benchmarks, raw metric artifacts, unit test suites, and LaTeX paper source files with single-command reproduction protocols.",
    "interests": [
        "Reinforcement Learning Systems",
        "Foundation Model Plasticity",
        "Confidential Computing & TEEs",
        "Oblivious RAM & Side-Channel Security",
        "Distributed Consensus & Fault Tolerance",
        "Graph-Constrained Causal Reasoning",
        "Cloud Policy & Attack Graph Verification",
        "Clinical Decision Support & Healthcare AI"
    ],
    "google_scholar_url": "https://scholar.google.com/citations?user=pending",
    "github_url": "https://github.com/shamddd",
    "alphaxiv_url": "https://alphaxiv.org/author/sham-thakare",
    "orcid": "0009-0000-0000-0000",
    "papers": [
        {
            "id": "PAPER-01",
            "title": "Predicting Reinforcement-Learning Plasticity of Intermediate Language-Model Checkpoints: A Cross-Architecture Diagnostic Study",
            "authors": ["Sham Satish Thakare"],
            "status": "Submitted / Under Review",
            "venue": "Journal of Machine Learning Research (JMLR)",
            "repo": "adaptive-rl-forge",
            "github_url": "https://github.com/shamddd/adaptive-rl-forge",
            "type": "Journal Submission"
        },
        {
            "id": "PAPER-02",
            "title": "EnclaveShield: Zero-Knowledge Memory Attestation and Side-Channel Mitigation for Hardware Enclaves",
            "authors": ["Sham Satish Thakare"],
            "status": "Preprint",
            "venue": "IEEE Transactions on Dependable and Secure Computing (TDSC Candidate)",
            "repo": "enclaveshield",
            "github_url": "https://github.com/shamddd/enclaveshield",
            "type": "Preprint / Working Paper"
        },
        {
            "id": "PAPER-03",
            "title": "AdaptiveReplica: Dynamic Quorum Adaptation and Failure-Aware Replica Selection in Distributed Consensus",
            "authors": ["Sham Satish Thakare"],
            "status": "Preprint",
            "venue": "IEEE Transactions on Parallel and Distributed Systems (TPDS Candidate)",
            "repo": "quorumshift",
            "github_url": "https://github.com/shamddd/quorumshift",
            "type": "Preprint / Working Paper"
        },
        {
            "id": "PAPER-04",
            "title": "TraceMind: Graph-Constrained Causal Reasoning for Root-Cause Localization in Microservice Systems",
            "authors": ["Sham Satish Thakare"],
            "status": "Preprint",
            "venue": "IEEE Transactions on Cloud Computing (TCC Candidate)",
            "repo": "tracemind",
            "github_url": "https://github.com/shamddd/tracemind",
            "type": "Preprint / Working Paper"
        },
        {
            "id": "PAPER-05",
            "title": "Compositional AST Invariant Verification for Declarative Container Workload Specifications",
            "authors": ["Sham Satish Thakare"],
            "status": "Research Project / Artifact",
            "venue": "IEEE TCC / CCGrid Candidate",
            "repo": "secure-cloud-infrastructure-platform",
            "github_url": "https://github.com/shamddd/secure-cloud-infrastructure-platform",
            "type": "Research Artifact"
        },
        {
            "id": "PAPER-06",
            "title": "MediRush: Clinical Decision Support & Triage Risk Modeling",
            "authors": ["Sham Satish Thakare"],
            "status": "Preserved Prep",
            "venue": "Elsevier Artificial Intelligence in Medicine",
            "repo": "medirush",
            "github_url": "https://github.com/shamddd/medirush",
            "type": "Preserved Publication Prep"
        }
    ]
}

out_json_path = os.path.join(base_dir, "research-profile.json")
with open(out_json_path, "w") as f:
    json.dump(profile_data, f, indent=2)

print(f"Generated research-profile.json at {out_json_path}")

# 2. Create publications.bib
bib_content = """@article{thakare2026predicting,
  author    = {Thakare, Sham Satish},
  title     = {Predicting Reinforcement-Learning Plasticity of Intermediate Language-Model Checkpoints: A Cross-Architecture Diagnostic Study},
  journal   = {Journal of Machine Learning Research (JMLR)},
  year      = {2026},
  note      = {Submitted / Under Review},
  url       = {https://github.com/shamddd/adaptive-rl-forge}
}

@techreport{thakare2026enclaveshield,
  author    = {Thakare, Sham Satish},
  title     = {EnclaveShield: Zero-Knowledge Memory Attestation and Side-Channel Mitigation for Hardware Enclaves},
  institution = {Independent Research},
  year      = {2026},
  note      = {Preprint / Working Paper (Target: IEEE TDSC)},
  url       = {https://github.com/shamddd/enclaveshield}
}

@techreport{thakare2026adaptivereplica,
  author    = {Thakare, Sham Satish},
  title     = {AdaptiveReplica: Dynamic Quorum Adaptation and Failure-Aware Replica Selection in Distributed Consensus},
  institution = {Independent Research},
  year      = {2026},
  note      = {Preprint / Working Paper (Target: IEEE TPDS)},
  url       = {https://github.com/shamddd/quorumshift}
}

@techreport{thakare2026tracemind,
  author    = {Thakare, Sham Satish},
  title     = {TraceMind: Graph-Constrained Causal Reasoning for Root-Cause Localization in Microservice Systems},
  institution = {Independent Research},
  year      = {2026},
  note      = {Preprint / Working Paper (Target: IEEE TCC)},
  url       = {https://github.com/shamddd/tracemind}
}

@misc{thakare2026securecloud,
  author    = {Thakare, Sham Satish},
  title     = {Compositional AST Invariant Verification for Declarative Container Workload Specifications},
  year      = {2026},
  note      = {Research Artifact},
  url       = {https://github.com/shamddd/secure-cloud-infrastructure-platform}
}

@misc{thakare2024medirush,
  author    = {Thakare, Sham Satish},
  title     = {MediRush: Clinical Decision Support \& Triage Risk Modeling},
  year      = {2024},
  note      = {Preserved Publication Preparation (Elsevier AI in Medicine)},
  url       = {https://github.com/shamddd/medirush}
}
"""

out_bib_path = os.path.join(base_dir, "publications.bib")
with open(out_bib_path, "w") as f:
    f.write(bib_content)

print(f"Generated publications.bib at {out_bib_path}")
