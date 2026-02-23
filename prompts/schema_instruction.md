Tu dois répondre STRICTEMENT avec ce JSON exact :

{
"sujet": "string",
"problematique": "string",
"introduction": {
"definitions": "string",
"cadre": "string",
"annonce\_problematique": "string",
"annonce\_plan": "string"
},
"plan": \[
{
"titre": "string",
"informations\_cles": \["string"],
"schemas": \[
{
"nom": "string",
"description": "string",
"interet\_concours": "string"
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

* "plan" doit contenir 2 ou 3 parties.
* Chaque "informations\_cles" doit contenir exactement 3 ou 4 éléments.
* Chaque partie doit contenir au moins 1 objet dans "schemas".
* Aucun champ ne doit être omis.
