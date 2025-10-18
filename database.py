# database.py (ФИНАЛЬНАЯ БЕЗОПАСНАЯ ВЕРСИЯ)

import json
import os
import time

DB_FILE = "user_diagrams.json"

def _load_data():
    if not os.path.exists(DB_FILE): return {}
    try:
        with open(DB_FILE, "r", encoding="utf-8") as f:
            content = f.read()
            return json.loads(content) if content else {}
    except (json.JSONDecodeError, FileNotFoundError): return {}

def _save_data(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_user_data(user_id: int):
    """Возвращает ВСЕ данные пользователя, создавая их при необходимости."""
    user_id_str = str(user_id)
    data = _load_data()
    if user_id_str not in data:
        timestamp = int(time.time())
        default_diagram_name = f"Новая диаграмма_{timestamp}"
        data[user_id_str] = {
            "diagrams": {
                default_diagram_name: {"nodes": [], "edges": [], "node_counter": 0}
            },
            "active_diagram_name": default_diagram_name,
            "settings": {"theme": "dark"}
        }
        _save_data(data)
    return data[user_id_str]

def save_user_data(user_id: int, user_data: dict):
    data = _load_data()
    data[str(user_id)] = user_data
    _save_data(data)

def list_saved_diagrams(user_id: int):
    """Возвращает список имен сохраненных диаграмм."""
    user_data = get_user_data(user_id)
    return list(user_data["diagrams"].keys())

def set_active_diagram(user_id: int, name: str):
    """Делает диаграмму с указанным именем активной."""
    user_data = get_user_data(user_id)
    if name in user_data["diagrams"]:
        user_data["active_diagram_name"] = name
        save_user_data(user_id, user_data)
        return True
    return False

def create_new_diagram(user_id: int):
    """Создает новую пустую диаграмму и делает ее активной."""
    user_data = get_user_data(user_id)
    new_name = f"Новая диаграмма_{int(time.time())}"
    user_data["diagrams"][new_name] = {"nodes": [], "edges": [], "node_counter": 0}
    user_data["active_diagram_name"] = new_name
    save_user_data(user_id, user_data)
    return new_name

def save_active_diagram(user_id: int, new_name: str):
    """Переименовывает (сохраняет) активную диаграмму."""
    user_data = get_user_data(user_id)
    active_name = user_data["active_diagram_name"]
    if new_name != active_name and new_name in user_data["diagrams"]:
        # Защита от перезаписи существующей диаграммы
        return False
    user_data["diagrams"][new_name] = user_data["diagrams"].pop(active_name)
    user_data["active_diagram_name"] = new_name
    save_user_data(user_id, user_data)
    return True