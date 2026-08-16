import hashlib
import json

class BaseModelAdapter:
    def __init__(self, model_id="Qwen/Qwen2.5-Math-1.5B"):
        self.model_id = model_id
        
    def format_input(self, question, prefix_steps):
        # Plain continuation format appropriate for base model
        text = f"Question: {question}\nStep-by-step solution:\n"
        if prefix_steps:
            text += "\n".join(prefix_steps) + "\n"
        return text

class InstructModelAdapter:
    def __init__(self, model_id="Qwen/Qwen2.5-Math-1.5B-Instruct"):
        self.model_id = model_id
        
    def format_input(self, question, prefix_steps):
        # Official chat template format for Qwen Instruct
        prompt = f"Solve the following math problem step by step:\n{question}"
        if prefix_steps:
            prompt += "\n\nPartial solution so far:\n" + "\n".join(prefix_steps)
        text = f"<|im_start|>system\nYou are a helpful math assistant.<|im_end|>\n<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n"
        return text

def compute_hashes(question, prefix_steps, adapter):
    semantic_payload = {"question": question, "prefix_steps": prefix_steps}
    semantic_hash = hashlib.sha256(json.dumps(semantic_payload, sort_keys=True).encode()).hexdigest()
    
    formatted_input = adapter.format_input(question, prefix_steps)
    input_hash = hashlib.sha256(formatted_input.encode()).hexdigest()
    
    return semantic_hash, input_hash, formatted_input
