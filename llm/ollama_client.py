import requests
from config import OLLAMA_MODEL
from llm.base import BaseLLM

class OllamaClient(BaseLLM):

    def generate(self, system_prompt: str, user_prompt: str) -> dict:

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": f"{system_prompt}\n\n{user_prompt}",
                "stream": False,
                "format": "json"
            }
        )

        response.raise_for_status()

        return response.json()["response"]
