from setuptools import setup, find_packages

setup(
    name="recovery_eval",
    version="1.0.0",
    description="State-Matched and Provenance-Aware Evaluation Framework for Language-Model Reasoning Diagnostics",
    author="Sham Satish Thakare",
    author_email="shamthakare3000@gmail.com",
    package_dir={"": "research-next/ieee_bigdata_2026"},
    packages=find_packages(where="research-next/ieee_bigdata_2026"),
    python_requires=">=3.11",
    entry_points={
        "console_scripts": [
            "recovery-eval=recovery_eval.cli.main:main",
        ],
    },
)
