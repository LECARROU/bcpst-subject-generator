# Générateur automatique de plans BCPST pour concours Agro/Véto A-CPGE

Ce projet permet de générer automatiquement des plans structurés pour des sujets d’examens BCPST (Biologie, Chimie, Physique et Sciences de la Terre) préparant au concours Agro/Véto A-CPGE, en utilisant des modèles LLM locaux (LLama 3.2 via Ollama) ou des modèles OpenRouter (GPT-4o).

Le pipeline produit pour chaque sujet : 

- Une problématique scientifique claire
- Une introduction structurée
- Un plan en 2 ou 3 parties
- 3 à 4 informations clés par partie
- Au moins un schéma par partie
- Une conclusion concise
- JSON strictement valide correspondant à la structure Pydantic

---

## 🧩 Architecture du projet

```markdown
biology/
├─ frontend/ # Site web 
│ └─ static/
│     └─ docs/
│          └─ subjects.csv # Liste des sujets d’examens
│     └─ markdowns/
│          └─ sujet_1.md # Sujet structuré au format markdown généré avec GPT-4o
├─ llm/
│ ├─ base.py # Classe abstraite provider
│ ├─ ollama_client.py # Client Ollama / LLM local
│ └─ openrouter_client.py # Client OpenRouter
├─ models/
│ └─ response_models.py # Modèles Pydantic pour valider la sortie
├─ prompts/
│ ├─ schema_instruction.md # Schéma JSON à respecter
│ ├─ system.md # Prompt system décrivant le rôle du LLM
│ └─ user_template.md # Template du prompt utilisateur
└─ utils/ 
│ ├─ loader.py # fonctions pour chargers les fichiers, prompts, etc.
│ └─ utils.py # fonction pour convertir json en markdown
├─ .env.example # Fichier exemple de configuration des variables d'environnement (OPENROUTER_API_KEY)
├─ main.py # Entrée principale du programme
├─ README.md
```


---

## ⚡ Fonctionnement

1. **Chargement des sujets :** `docs/subjects.csv` est lu et transformé en dictionnaire Python.  
2. **Préparation des prompts :** le fichier `schema_instruction.md` définit le format JSON strict, injecté dans `system.md`.  
3. **Génération LLM :** `generate_for_subject(subject)` appelle le modèle (Ollama local ou OpenRouter) pour générer le plan.  
4. **Validation Pydantic :** le JSON généré est validé avec `ExamResponse`.  
5. **Post-traitement :** certaines erreurs du LLM (liste trop courte, champs manquants) sont corrigées automatiquement.  
6. **Sortie :** le résultat est écrit dans `output/output.json`.

---

## ⚙️ Installation

### Prérequis

- Python 3.11+
- Ollama CLI avec LLaMA 3.2 installé pour usage local (optionnel)
- Clé API OpenRouter (optionnel)

### Création de l’environnement

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / macOS
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```
Dépendances principales
- pydantic pour validation des modèles
- python-dotenv pour gérer les clés API
- ollama ou openai / openrouter SDK pour les appels LLM

🚀 Utilisation
Ligne de commande
```bash
python main.py
```

### 🛠️ Personnalisation des prompts

- schema_instruction.md : définit la structure JSON obligatoire
- system.md : décrit le rôle du LLM et injecte le schéma
- user_template.md : contient le sujet et les consignes pédagogiques

Pour LLama 3.2 local, les contraintes exactes (nombre d’items, présence de champs) sont respectées autant que possible, certaines corrections sont appliquées automatiquement en post-traitement.