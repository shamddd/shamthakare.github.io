import hashlib
import json

class BaseModelAdapter:
    def __init__(self, model_id="Qwen/Qwen2.5-Math-1.5B", revision="c181514eb9160eb80f0ed9a3c9e6d013ab63060a"):
        self.model_id = model_id
        self.revision = revision
        
    def format_input(self, question, prefix_steps):
        text = f"Question: {question}\nStep-by-step solution:\n"
        if prefix_steps:
            text += "\n".join(prefix_steps) + "\n"
        return text

    def tokenize_and_hash(self, question, prefix_steps, tokenizer=None):
        text = self.format_input(question, prefix_steps)
        if tokenizer is not None and hasattr(tokenizer, "encode"):
            token_ids = tokenizer.encode(text)
        else:
            # Fallback mock encoding for testing without active network weights
            token_ids = [ord(c) for c in text[:128]]
            
        token_bytes = json.dumps(token_ids).encode()
        input_sha256 = hashlib.sha256(token_bytes).hexdigest()
        return text, token_ids, input_sha256


class InstructModelAdapter:
    def __init__(self, model_id="Qwen/Qwen2.5-Math-1.5B-Instruct", revision="8a719c2ddc18eb3d441113b2fa7975c613045610"):
        self.model_id = model_id
        self.revision = revision
        
    def format_messages(self, question, prefix_steps):
        prompt = f"Solve the following math problem step by step:\n{question}"
        if prefix_steps:
            prompt += "\n\nPartial solution so far:\n" + "\n".join(prefix_steps)
            
        return [
            {"role": "system", "content": "You are a helpful math assistant."},
            {"role": "user", "content": prompt}
        ]

    def format_input(self, question, prefix_steps, tokenizer=None):
        messages = self.format_messages(question, prefix_steps)
        if tokenizer is not None and hasattr(tokenizer, "apply_chat_template"):
            return tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        else:
            # Official Qwen chat template string representation
            p = messages[1]["content"]
            return f"<|im_start|>system\nYou are a helpful math assistant.<|im_end|>\n<|im_start|>user\n{p}<|im_end|>\n<|im_start|>assistant\n"

    def tokenize_and_hash(self, question, prefix_steps, tokenizer=None):
        messages = self.format_messages(question, prefix_steps)
        if tokenizer is not None and hasattr(tokenizer, "apply_chat_template"):
            token_ids = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True)
            text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        else:
            text = self.format_input(question, prefix_steps, tokenizer=None)
            token_ids = [ord(c) for c in text[:128]]
            
        token_bytes = json.dumps(token_ids).encode()
        input_sha256 = hashlib.sha256(token_bytes).hexdigest()
        return text, token_ids, input_sha256


def compute_hashes_v2(question, prefix_steps, adapter, tokenizer=None):
    semantic_payload = {"question": question, "prefix_steps": prefix_steps}
    semantic_hash = hashlib.sha256(json.dumps(semantic_payload, sort_keys=True).encode()).hexdigest()
    
    text, token_ids, input_sha256 = adapter.tokenize_and_hash(question, prefix_steps, tokenizer=tokenizer)
    return semantic_hash, input_sha256, text, token_ids

def compute_hashes(question, prefix_steps, adapter):
    sem_hash, in_hash, text, _ = compute_hashes_v2(question, prefix_steps, adapter)
    return sem_hash, in_hash, text
