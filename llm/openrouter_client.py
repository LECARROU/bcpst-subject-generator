import requests
from config import OPENROUTER_API_KEY, OPENROUTER_MODEL
from llm.base import BaseLLM

class OpenRouterClient(BaseLLM):

    def generate(self, system_prompt: str, user_prompt: str) -> dict:

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": OPENROUTER_MODEL,
                "temperature": 0.1,
                "response_format": {"type": "json_object"},
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            }
        )

        response.raise_for_status()

        return response.json()["choices"][0]["message"]["content"]
    
