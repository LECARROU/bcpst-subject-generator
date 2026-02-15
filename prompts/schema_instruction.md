Tu dois répondre STRICTEMENT avec ce JSON exact :

{
  "sujet": "string",
  "problematique": "string",
  "introduction": {
    "definitions": "string",
    "cadre": "string",
    "annonce_problematique": "string",
    "annonce_plan": "string"
  },
  "plan": [
    {
      "titre": "string",
      "informations_cles": ["string"],
      "schemas": [
        {
          "nom": "string",
          "description": "string",
          "interet_concours": "string"
        }
      ]
    }
  ],
  "conclusion": "string"
}


Ne change AUCUN nom de champ.
Ne traduis PAS les clés.
Réponds en français.
Contraintes obligatoires :
- "plan" doit contenir 2 ou 3 parties.
- Chaque "informations_cles" doit contenir exactement 3 ou 4 éléments.
- Chaque partie doit contenir au moins 1 objet dans "schemas".
- Aucun champ ne doit être omis.

