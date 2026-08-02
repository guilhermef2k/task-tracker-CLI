import json
import os

DB_FILE = "tasks.json"

def load_tasks()->list:
    """Carrega as tasks salvas no JSON, retorna uma lista vazia se não houver tasks salvas"""
    if not os.path.exists(DB_FILE):
        return[]
    try:
        with open(DB_FILE, "r", encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return[]

def save_task(task:list)->None:
    """Salva as tasks em um arquivo JSON"""
    with open(DB_FILE, "w", encoding="utf-8") as file:
        json.dump(task, file, ensure_ascii=False, indent=4)