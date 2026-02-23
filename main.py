import argparse
import json 
import json
import time
from dotenv import load_dotenv
from pathlib import Path
from config import DEFAULT_PROVIDER
from llm.openrouter_client import OpenRouterClient
from llm.ollama_client import OllamaClient
from utils.loader import load_json, load_text
from models.response_model import ExamResponse
from utils.loader import load_csv
from utils.utils import convert_json_to_md

BASE_DIR = Path(__file__).resolve().parents[0]
DOCS_DIR = Path(__file__).resolve().parents[0] / "frontend/static/docs"
PROMPTS_DIR = Path(__file__).resolve().parents[0] / "prompts"
JSON_DIR = MD_DIR = Path(__file__).resolve().parents[0] / "json"
MD_DIR = Path(__file__).resolve().parents[0] / "frontend/static/markdowns"

def get_llm():
    if DEFAULT_PROVIDER == "openrouter":
        return OpenRouterClient()
    return OllamaClient()

def generate_for_subject(subject: str):
    schema_instruction = load_text(PROMPTS_DIR / "schema_instruction.md")

    system_template = load_text(PROMPTS_DIR / "system.md")
    system_prompt = system_template.replace("{SCHEMA}", schema_instruction)
    
    user_template = load_text(PROMPTS_DIR / "user_template.md")
    user_prompt = user_template.replace("{SUJET}", subject)
    
    llm = get_llm()

    raw_output = llm.generate(system_prompt, user_prompt)

    parsed = json.loads(raw_output)

    try:
        return ExamResponse(**parsed)
    except Exception as e:
        print("Validation error :", e)
        print("JSON reçu :", json.dumps(parsed, indent=2, ensure_ascii=False))
        raise

# python main.py --send-email True
# python main.py

# ---------------------------
# Main orchestration
# ---------------------------
def main(args):
    # Charger .env si présent
    load_dotenv()

    docs = DOCS_DIR / "subjects.csv"
    subjects = load_csv(docs)
    success = False
    # for i in range(4):
    #     idx = i+1
    #     json_output_path = JSON_DIR / f"sujet_{idx}.json"
    #     convert_json_to_md(json_output_path, idx)

    for attempt in range(1):
        try:
            print(f"Tentative {attempt+1}...")
            for key,subject in subjects.items():
                result = generate_for_subject(subject)

                print(f"Génération sujet {key} réussie.")
                # print(result.model_dump_json(indent=2, ensure_ascii=False))
                
                json_output_path = JSON_DIR / f"sujet_{key}.json"
                with open(json_output_path, "w", encoding="utf-8") as f:
                    f.write(result.model_dump_json(indent=2, ensure_ascii=False))

                convert_json_to_md(json_output_path, key)
                success = True
            break

        except Exception as e:
            print(f"Erreur : {e}")
            time.sleep(2 ** attempt)

    if not success:
        print("Échec après 3 tentatives.")



# ---------------------------
# CLI
# ---------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Générateur automatique de plans BSPST avec OpenRouter + Ollama.")
    parser.add_argument("--output-dir", help="Dossier de sortie pour les résumés")
    parser.add_argument("--send-email", action="store_true", help="Activer l'envoi par mail")
    parser.add_argument("--smtp-host")
    parser.add_argument("--smtp-port", type=int)
    parser.add_argument("--smtp-user")
    parser.add_argument("--smtp-pass")
    parser.add_argument("--smtp-from")
    parser.add_argument("--smtp-to", help="Emails séparés par des virgules")
    parser.add_argument("--smtp-ssl", action="store_true", help="Utiliser SMTP_SSL (par défaut True si via env)")
    parser.add_argument("--smtp-starttls", action="store_true", help="Utiliser STARTTLS (si non SSL)")
    args = parser.parse_args()
    main(args)