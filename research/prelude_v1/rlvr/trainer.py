"""
Standardized Group Relative Policy Optimization (GRPO / RLVR) wrapper for PRELUDE v1.
Implements locked policy gradient training with verifiable binary rewards and early pilot benchmarking.
"""

from typing import List, Dict, Any, Tuple, Optional
import torch
import torch.nn.functional as F
import numpy as np
from transformers import PreTrainedModel, PreTrainedTokenizer
from ..config import RLVRStandardizedConfig
from ..verifiers.math_verifier import verify_reasoning_rollout


class StandardizedRLVRTrainer:
    """
    Standardized GRPO trainer enforcing locked hyperparameters across all evaluated models.
    """
    def __init__(self, 
                 model: PreTrainedModel, 
                 ref_model: PreTrainedModel, 
                 tokenizer: PreTrainedTokenizer, 
                 config: RLVRStandardizedConfig,
                 device: torch.device):
        self.model = model
        self.ref_model = ref_model
        self.tokenizer = tokenizer
        self.config = config
        self.device = device
        
        # Optimizer locked to AdamW
        self.optimizer = torch.optim.AdamW(
            self.model.parameters(),
            lr=self.config.learning_rate,
            weight_decay=self.config.weight_decay
        )
        
    def generate_group_rollouts(self, prompt: str) -> Tuple[torch.Tensor, List[str], List[int], torch.Tensor]:
        """
        Generates G rollouts for prompt, evaluates rewards, and computes advantages.
        """
        formatted_prompt = f"Question: {prompt}\nLet's solve this step-by-step:\n"
        inputs = self.tokenizer(formatted_prompt, return_tensors="pt").to(self.device)
        prompt_len = inputs["input_ids"].size(1)
        
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=self.config.max_gen_length,
                do_sample=True,
                temperature=self.config.temperature,
                top_p=self.config.top_p,
                num_return_sequences=self.config.group_size,
                pad_token_id=self.tokenizer.eos_token_id
            )
            
        gen_texts = []
        rewards = []
        for seq in outputs:
            text = self.tokenizer.decode(seq[prompt_len:], skip_special_tokens=True)
            gen_texts.append(text)
            
        return outputs, gen_texts, inputs["input_ids"]

    def compute_grpo_loss(self, 
                          sequences: torch.Tensor, 
                          prompt_len: int, 
                          rewards: List[int]) -> torch.Tensor:
        """
        Computes GRPO surrogate loss with group advantage and KL regularization.
        """
        # Advantage normalization
        r_arr = np.array(rewards, dtype=np.float32)
        std_r = np.std(r_arr)
        if std_r > 1e-6:
            advantages = (r_arr - np.mean(r_arr)) / (std_r + 1e-8)
        else:
            advantages = np.zeros_like(r_arr)
            
        adv_t = torch.tensor(advantages, dtype=torch.float32, device=self.device)
        
        # Policy logits
        out = self.model(sequences)
        logits = out.logits[:, :-1, :]
        labels = sequences[:, 1:]
        
        # Reference logits
        with torch.no_grad():
            ref_out = self.ref_model(sequences)
            ref_logits = ref_out.logits[:, :-1, :]
            
        # Log-probs of response tokens only (mask out prompt)
        log_probs = F.log_softmax(logits, dim=-1)
        ref_log_probs = F.log_softmax(ref_logits, dim=-1)
        
        token_log_probs = log_probs.gather(dim=-1, index=labels.unsqueeze(-1)).squeeze(-1)
        token_ref_log_probs = ref_log_probs.gather(dim=-1, index=labels.unsqueeze(-1)).squeeze(-1)
        
        # Mask prompt tokens
        mask = torch.zeros_like(labels, dtype=torch.float32)
        mask[:, prompt_len - 1:] = 1.0
        
        # KL divergence per token: D_KL = p * (log p - log q) approx = ref_log - log
        kl_div = (token_ref_log_probs - token_log_probs) * mask
        kl_penalty = self.config.beta_kl * kl_div.sum(dim=-1)
        
        # Policy gradient term
        response_log_probs = (token_log_probs * mask).sum(dim=-1)
        pg_loss = -(response_log_probs * adv_t) + kl_penalty
        
        return pg_loss.mean()

    def run_training_step(self, prompt: str, gold_answer: str) -> Dict[str, float]:
        """Executes a single standardized GRPO training step."""
        self.model.train()
        sequences, gen_texts, prompt_ids = self.generate_group_rollouts(prompt)
        prompt_len = prompt_ids.size(1)
        
        rewards = []
        for text in gen_texts:
            r, _, _ = verify_reasoning_rollout(text, gold_answer)
            rewards.append(r)
            
        loss = self.compute_grpo_loss(sequences, prompt_len, rewards)
        
        self.optimizer.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(self.model.parameters(), max_norm=1.0)
        self.optimizer.step()
        
        return {
            "loss": float(loss.item()),
            "mean_reward": float(np.mean(rewards)),
            "reward_variance": float(np.var(rewards))
        }

    def run_early_pilot(self, train_data: List[Dict[str, str]], pilot_steps: int = 10) -> float:
        """
        Executes a 10-step early RLVR pilot to compute the L5 practical baseline delta_hat.
        Extrapolates linear learning curve over total planned steps.
        """
        initial_rewards = []
        final_rewards = []
        
        for step in range(pilot_steps):
            item = train_data[step % len(train_data)]
            metrics = self.run_training_step(item["question"], item["answer"])
            if step < 3:
                initial_rewards.append(metrics["mean_reward"])
            if step >= pilot_steps - 3:
                final_rewards.append(metrics["mean_reward"])
                
        r_start = np.mean(initial_rewards) if initial_rewards else 0.0
        r_end = np.mean(final_rewards) if final_rewards else 0.0
        
        # Slope per step
        slope = (r_end - r_start) / max(1, pilot_steps - 1)
        # Extrapolate over 150 total steps (with saturation clamp)
        projected_delta = float(np.clip(slope * (self.config.num_optimization_steps / 4), -0.2, 0.6))
        return projected_delta
