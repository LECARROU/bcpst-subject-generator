import os
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

DEFAULT_PROVIDER = "openrouter"  # ou "ollama"

OPENROUTER_MODEL = "openai/gpt-4o"
OLLAMA_MODEL = "llama3.2"
