import json
from pathlib import Path

MD_DIR = Path(__file__).resolve().parent.parent / "markdowns"

def convert_json_to_md(path: str, id)->None:

    # Charger le JSON
    with open(path, 'r', encoding='utf-8') as f:
        result = json.load(f)

    # Initialiser le contenu markdown
    md = []

    # 1. Titre principal (sujet)
    md.append(f"# Sujet numéro : {id}")
    md.append(f"# 🧪 {result['sujet']}")

    # 2. Problématique
    md.append(f"## 💡 Problématique")
    md.append(result['problematique'])

    # 3. Introduction
    md.append("## 🔗 Introduction")
    intro = result['introduction']

    # Definitions
    if 'definitions' in intro:
        md.append(f"- 📖 Définitions : {intro['definitions']}")

    # Cadre
    if 'cadre' in intro:
        md.append(f"- 📐 Cadre : {intro['cadre']},")

    # Annonce problématique
    if 'annonce_problematique' in intro:
        md.append(f"- 🎤 Annonce de la problématique : {intro['annonce_problematique']},")

    # Annonce plan
    if 'annonce_plan' in intro:
        md.append(f"- 🎯 Annonce du plan : {intro['annonce_plan']},")

    # 4. Plan
    md.append("## 🧬 plan")

    for partie_idx, partie in enumerate(result['plan']):
        md.append(f"### {partie_idx} : 🖍️ Partie {partie_idx + 1}")
        
        # Titre
        md.append(f"- 📍 Titre : {partie['titre']}")
        
        # Informations clés
        if 'Informations clées' in partie:
            md.append("- 🔑 informations_cles :")
            for i, info in enumerate(partie['informations_cles']):
                md.append(f"  - {i+1} : {info},")
        
        # Schémas
        if 'schemas' in partie:
            md.append("- 📈 Schemas :")
            for schema_idx, schema in enumerate(partie['schemas']):
                md.append(f"  - Schema {schema_idx + 1}")
                md.append(f"    - nom : {schema['nom']},")
                md.append(f"    - description : {schema['description']},")
                if 'interet_concours' in schema:
                    md.append(f"    - interet_concours : {schema['interet_concours']}")

    # 5. Conclusion
    md.append("## 🔥 Conclusions")
    md.append(result['conclusion'])

    # Écrire le fichier
    outpout_path = MD_DIR / f"sujet_{id}.md"
    with open(outpout_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

    print("✅ Fichier créé : output.md")