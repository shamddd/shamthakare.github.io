import os
import sys
import json
import hashlib
import time
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

class EmpiricalNeuralRolloutRecord:
    def __init__(self, experiment_id, execution_version, rollout_id, attempt_number,
                 problem_id, state_id, recovery_or_control, state_provenance,
                 policy_id, model_repository, model_revision, model_class, parameter_count, trainable_parameter_count,
                 weight_manifest_sha256, tokenizer_revision, device, dtype,
                 canonical_semantic_state_sha256, serialized_input_sha256,
                 input_ids_tensor, output_ids_tensor, tokenizer,
                 generation_seed, temperature, top_p, do_sample, max_new_tokens,
                 start_ns, end_ns, verifier_name, verifier_version, verifier_input, verifier_raw_output,
                 extracted_answer, expected_answer, primitive_success, git_commit, execution_schedule_index):
        
        self.record_type = "empirical_neural"
        self.experiment_id = experiment_id
        self.execution_version = execution_version
        self.rollout_id = rollout_id
        self.attempt_number = attempt_number
        
        self.problem_id = problem_id
        self.state_id = state_id
        self.recovery_or_control = recovery_or_control
        self.state_provenance = state_provenance
        
        self.policy_id = policy_id
        self.model_repository = model_repository
        self.model_revision = model_revision
        self.model_class = model_class
        self.parameter_count = parameter_count
        self.trainable_parameter_count = trainable_parameter_count
        self.model_weight_manifest_sha256 = weight_manifest_sha256
        self.tokenizer_revision = tokenizer_revision
        self.device = str(device)
        self.dtype = str(dtype)
        
        self.canonical_semantic_state_sha256 = canonical_semantic_state_sha256
        self.serialized_input_sha256 = serialized_input_sha256
        
        # Enforce tensor slice derivation for input and generated token IDs
        if hasattr(input_ids_tensor, "tolist"):
            in_list = input_ids_tensor.tolist()[0] if input_ids_tensor.ndim > 1 else input_ids_tensor.tolist()
        else:
            in_list = list(input_ids_tensor)
            
        if hasattr(output_ids_tensor, "tolist"):
            out_list = output_ids_tensor.tolist()[0] if output_ids_tensor.ndim > 1 else output_ids_tensor.tolist()
        else:
            out_list = list(output_ids_tensor)
            
        input_len = len(in_list)
        self.input_token_ids = out_list[:input_len]
        self.input_token_count = len(self.input_token_ids)
        
        self.generated_token_ids = out_list[input_len:]
        self.generated_token_count = len(self.generated_token_ids)
        
        # Enforce tokenizer.decode derivation
        self.generated_text = tokenizer.decode(self.generated_token_ids, skip_special_tokens=True)
        
        self.generation_seed = generation_seed
        self.temperature = temperature
        self.top_p = top_p
        self.do_sample = do_sample
        self.max_new_tokens = max_new_tokens
        
        self.generation_start_monotonic_ns = start_ns
        self.generation_end_monotonic_ns = end_ns
        dur_sec = (end_ns - start_ns) / 1e9
        self.generation_duration_sec = round(dur_sec, 4)
        self.tokens_per_second = round(self.generated_token_count / dur_sec, 2) if dur_sec > 0 else 0.0
        
        self.verifier_name = verifier_name
        self.verifier_version = verifier_version
        self.verifier_input = verifier_input
        self.verifier_raw_output = verifier_raw_output
        self.extracted_answer = extracted_answer
        self.expected_answer = expected_answer
        self.primitive_success = bool(primitive_success)
        
        self.software_git_commit = git_commit
        self.execution_schedule_index = execution_schedule_index

    def to_dict(self):
        return {k: v for k, v in self.__dict__.items()}


class EmpiricalNeuralRunner:
    def __init__(self, model_id, revision, device="mps"):
        self.model_id = model_id
        self.revision = revision
        
        print(f"[*] Loading genuine HuggingFace model {model_id} (revision {revision[:8]})...", flush=True)
        self.tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)
        
        # Select device
        if device == "mps" and torch.backends.mps.is_available():
            self.device = torch.device("mps")
        else:
            self.device = torch.device("cpu")
            
        self.model = AutoModelForCausalLM.from_pretrained(
            model_id,
            revision=revision,
            torch_dtype=torch.float16 if self.device.type == "mps" else torch.float32,
            low_cpu_mem_usage=True
        ).to(self.device)
        
        self.model.eval()
        
        self.model_class = type(self.model).__name__
        self.parameter_count = sum(p.numel() for p in self.model.parameters())
        self.trainable_parameter_count = sum(p.numel() for p in self.model.parameters() if p.requires_grad)
        self.first_param_device = str(next(self.model.parameters()).device)
        self.dtype = str(next(self.model.parameters()).dtype)
        
        # Verify model is real torch module with >1B params
        if not isinstance(self.model, torch.nn.Module):
            raise TypeError("Model is not a valid torch.nn.Module!")
        if self.parameter_count < 1000000000:
            raise ValueError(f"Model parameter count too low: {self.parameter_count}")

    def generate_rollout(self, prompt_text, seed, max_new_tokens=64, temperature=0.7, top_p=0.9):
        torch.manual_seed(seed)
        if self.device.type == "mps":
            torch.mps.manual_seed(seed)
            
        inputs = self.tokenizer(prompt_text, return_tensors="pt").to(self.device)
        input_ids = inputs["input_ids"]
        
        start_ns = time.monotonic_ns()
        
        # ENFORCE SCIENTIFIC PATH: model.generate inside inference_mode
        with torch.inference_mode():
            output_ids = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                top_p=top_p,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id
            )
            
        if self.device.type == "mps":
            torch.mps.synchronize()
            
        end_ns = time.monotonic_ns()
        
        return input_ids, output_ids, start_ns, end_ns
