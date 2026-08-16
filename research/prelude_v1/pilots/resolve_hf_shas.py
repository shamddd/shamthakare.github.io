import sys
from huggingface_hub import HfApi

api = HfApi()

m1 = "Qwen/Qwen2.5-Math-1.5B"
m2 = "Qwen/Qwen2.5-Math-1.5B-Instruct"

try:
    info1 = api.model_info(m1)
    sha1 = info1.sha
    print(f"{m1} resolved SHA: {sha1}")
except Exception as e:
    print(f"Error resolving {m1}: {e}")

try:
    info2 = api.model_info(m2)
    sha2 = info2.sha
    print(f"{m2} resolved SHA: {sha2}")
except Exception as e:
    print(f"Error resolving {m2}: {e}")
