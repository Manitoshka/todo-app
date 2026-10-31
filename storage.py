import json
import os
from logic import Task

FILENAME = "tasks.txt"

def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump([t.to_dict() for t in tasks], f, ensure_ascii=False, indent=4)

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as f:
        data = json.load(f)
        return [Task.from_dict(item) for item in data]