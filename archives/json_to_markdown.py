import json

# Charger le JSON
with open('data_1.json', 'r', encoding='utf-8') as f:
    result = json.load(f)

# Initialiser le contenu markdown
md = []

# 1. Titre principal (sujet)
md.append(f"# 🧪 sujet : {result['sujet']}")

# 2. Problématique
md.append(f"## 💡 problematique")
md.append(result['problematique'])

# 3. Introduction
md.append("## 🔗 introduction")
intro = result['introduction']

# Definitions
if 'definitions' in intro:
    md.append(f"- 📖 definitions : {intro['definitions']}")

# Cadre
if 'cadre' in intro:
    md.append(f"- 📐 cadre : {intro['cadre']},")

# Annonce problématique
if 'annonce_problematique' in intro:
    md.append(f"- 🎤 annonce_problematique : {intro['annonce_problematique']},")

# Annonce plan
if 'annonce_plan' in intro:
    md.append(f"- 🎯 annonce_plan : {intro['annonce_plan']},")

# 4. Plan
md.append("## 🧬 plan")

for partie_idx, partie in enumerate(result['plan']):
    md.append(f"### {partie_idx} : 🖍️ Partie {partie_idx + 1}")
    
    # Titre
    md.append(f"- 🖍️ titre : {partie['titre']}")
    
    # Informations clés
    if 'informations_cles' in partie:
        md.append("- 🔑 informations_cles :")
        for i, info in enumerate(partie['informations_cles']):
            md.append(f"  - {i} : {info},")
    
    # Schémas
    if 'schemas' in partie:
        md.append("- 📈 schemas :")
        for schema_idx, schema in enumerate(partie['schemas']):
            md.append(f"  - {schema_idx} : schema {schema_idx + 1}")
            md.append(f"    - nom : {schema['nom']},")
            md.append(f"    - description : {schema['description']},")
            if 'interet_concours' in schema:
                md.append(f"    - interet_concours : {schema['interet_concours']}")

# 5. Conclusion
md.append("## 🔥 conclusion")
md.append(result['conclusion'])

# Écrire le fichier
with open('output_1.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(md))

print("✅ Fichier créé : output.md")