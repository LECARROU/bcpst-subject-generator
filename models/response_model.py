from pydantic import BaseModel, Field
from typing import List

class SchemaItem(BaseModel):
    nom: str
    description: str
    interet_concours: str

class Partie(BaseModel):
    titre: str
    informations_cles: List[str] = Field(min_items=3, max_items=4)
    schemas: List[SchemaItem] = Field(min_items=1)

class Introduction(BaseModel):
    definitions: str
    cadre: str
    annonce_problematique: str
    annonce_plan: str

class ExamResponse(BaseModel):
    sujet: str
    problematique: str
    introduction: Introduction
    plan: List[Partie] = Field(min_items=2, max_items=3)
    conclusion: str
