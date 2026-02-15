import csv
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"

def load_csv(path: str) -> dict[str, str]:
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"{path} introuvable")

    data_dict = {}

    with path.open(encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        required_columns = {"number", "subject"}
        if not required_columns.issubset(reader.fieldnames):
            raise ValueError(
                f"Le CSV doit contenir les colonnes : {required_columns}"
            )

        for row in reader:
            key = row["number"].strip()
            value = row["subject"].strip()
            data_dict[key] = value

    return data_dict

def load_text(path: str) -> str:
    return (BASE_DIR / path).read_text(encoding="utf-8")

def load_json(path: str) -> dict:
    return json.loads(load_text(path))
