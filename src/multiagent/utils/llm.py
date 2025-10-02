# src/multiagent/utils/llm.py
import os
from transformers import pipeline


class LLM:
    """Класс для работы с LLM через Hugging Face transformers."""

    def __init__(self):
        model = os.getenv("HF_MODEL", "gpt5") 
        self.generator = pipeline("text-generation", model=model)

    def ask(self, query: str, max_tokens: int = 200) -> str:
        response = self.generator(query, max_length=max_tokens, num_return_sequences=1)
        return response[0]["generated_text"].strip()


# глобальный инстанс
llm = LLM()
