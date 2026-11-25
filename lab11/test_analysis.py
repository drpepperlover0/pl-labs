import json
from pathlib import Path
from tempfile import TemporaryDirectory
from analysis import validate_todos, completion_counts, top_users, select_tasks


folder = Path(__file__).resolve().parent
todos_json = folder / "todos.json"
with open(todos_json, 'r', encoding='utf-8') as file:
    todos = json.load(file)

# ==========================================
# 1. Тесты на учебном наборе из ТЗ
# ==========================================

# Проверяем, что валидация проходит без ошибок
validate_todos(todos)

# Проверяем статистику
counts = completion_counts(todos)
assert counts == {5: 2, 10: 2}, "Ошибка в подсчете выполненных задач"

# Проверяем лидеров (несколько лидеров)
assert top_users(counts) == [5, 10], "Ошибка в поиске лидеров"

# Проверяем твой вариант №9 (user_id=5, подстрока="с")
selected = select_tasks(todos, 5, "с")
assert len(selected) == 1, "Ошибка в варианте 9 (должна быть 1 задача)"
assert selected[0]["id"] == 5, "Вариант 9 выбрал не ту задачу"

# Проверка неизвестного пользователя
assert select_tasks(todos, 999, "с") == [], "Неизвестный пользователь должен вернуть []"

# Проверка варианта без совпадений (например, ищем "я")
assert select_tasks(todos, 5, "я") == [], "Нет совпадений - должен быть []"

# ==========================================
# 2. Тесты на пустой список и набор без выполненных
# ==========================================
# Пустой список
assert top_users({}) == [], "Пустой словарь должен давать []"

# Набор только с completed=False
todos_false = [{"id": 1, "userId": 5, "title": "Тест", "completed": False}]
assert top_users(completion_counts(todos_false)) == [], "Нет выполненных - лидеров нет"

# ==========================================
# 3. Тесты на ошибки валидации (ValueError)
# ==========================================
# 3.1. Повторный id
bad_todos_id = [
    {"id": 1, "userId": 5, "title": "А", "completed": True},
    {"id": 1, "userId": 5, "title": "Б", "completed": True}
]
try:
    validate_todos(bad_todos_id)
except ValueError:
    pass
else:
    assert False, "Ошибка: повторный ID не обнаружен!"

# 3.2. Отсутствует userId
bad_todos_user = [{"id": 1, "title": "А", "completed": True}]
try:
    validate_todos(bad_todos_user)
except ValueError:
    pass
else:
    assert False, "Ошибка: отсутствие userId не обнаружено!"

# 3.3. completed="false" (строка вместо bool)
bad_todos_comp = [{"id": 1, "userId": 5, "title": "А", "completed": "false"}]
try:
    validate_todos(bad_todos_comp)
except ValueError:
    pass
else:
    assert False, "Ошибка: completed='false' не обнаружена!"

# 3.4. id=true (булево значение вместо int)
bad_todos_bool = [{"id": True, "userId": 5, "title": "А", "completed": True}]
try:
    validate_todos(bad_todos_bool)
except ValueError:
    pass
else:
    assert False, "Ошибка: id=true не обнаружена!"

# 3.5. Вместо списка передан объект
bad_root = {"id": 1, "userId": 5, "title": "А", "completed": True}
try:
    validate_todos(bad_root)
except ValueError:
    pass
else:
    assert False, "Ошибка: корень не является списком (не обнаружено)!"

# ==========================================
# 4. Тест записи и чтения JSON
# ==========================================
with TemporaryDirectory() as directory:
    path = Path(directory) / "test_selected.json"

    # Записываем выборку в файл
    with open(path, "w", encoding="utf-8") as file:
        json.dump(selected, file, ensure_ascii=False, indent=2)

    # Читаем обратно
    with open(path, "r", encoding="utf-8") as file:
        loaded = json.load(file)

    # Проверяем, что структура не изменилась
    assert loaded == selected, "Структура JSON после записи и чтения изменилась!"

print("Все проверки пройдены успешно!")