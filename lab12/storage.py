import json
from logic import validate_records


def load_records(path):
    with open(path, 'r', encoding='utf-8') as file:
        todos = json.load(file)
    validate_records(todos)
    return todos


def save_records(path, records):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(records, file, ensure_ascii=False, indent=2)
