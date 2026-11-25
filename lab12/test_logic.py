from logic import *

print("Начинаем тесты logic.py...")

# ==========================================
# 1. Тесты валидации
# ==========================================
validate_records([])

valid = [{"id": 1, "title": "Тест", "category": "Учёба", "amount": 10, "completed": False}]
validate_records(valid)

# Все ошибочные случаи: должны выбросить ValueError
bad_cases = [
    ("корень не список", {"id": 1}),
    ("запись не словарь", ["строка вместо словаря"]),
    ("нет ключа amount", [{"id": 1, "title": "T", "category": "C", "completed": False}]),
    ("id = True (bool вместо int)", [{"id": True, "title": "T", "category": "C", "amount": 1, "completed": False}]),
    ("id = -1 (отрицательный)", [{"id": -1, "title": "T", "category": "C", "amount": 1, "completed": False}]),
    ("title пустой после strip", [{"id": 1, "title": "   ", "category": "C", "amount": 1, "completed": False}]),
    ("category пустой", [{"id": 1, "title": "T", "category": "  ", "amount": 1, "completed": False}]),
    ("amount = -1", [{"id": 1, "title": "T", "category": "C", "amount": -1, "completed": False}]),
    ("amount = True (bool вместо int)", [{"id": 1, "title": "T", "category": "C", "amount": True, "completed": False}]),
    ("completed = 0 (int вместо bool)", [{"id": 1, "title": "T", "category": "C", "amount": 1, "completed": 0}]),
    ("повторный id", [
        {"id": 1, "title": "A", "category": "C", "amount": 1, "completed": False},
        {"id": 1, "title": "B", "category": "C", "amount": 2, "completed": False}
    ]),
]

for name, bad_data in bad_cases:
    try:
        validate_records(bad_data)
    except ValueError:
        pass
    else:
        assert False, f"Ошибка валидации не обнаружена: {name}"

print("[OK] Валидация")

# ==========================================
# 2. Тесты добавления и поиска
# ==========================================
records = []

r1 = add_record(records, "  Python  ", "  учёба ", 5)
assert r1["id"] == 1, "Первый ID должен быть 1"
assert r1["title"] == "Python", "Пробелы в title должны обрезаться"
assert r1["category"] == "учёба", "Пробелы в category должны обрезаться"
assert r1["completed"] is False, "Начальный статус должен быть False"

r2 = add_record(records, "Python", "учёба", 10)
assert r2["id"] == 2, "Второй ID должен быть 2"
assert r2["title"] == "Python", "Одинаковые названия разрешены"

# Поиск без учёта регистра
found = find_records(records, "PYTHON")
assert len(found) == 2, "Поиск 'PYTHON' должен найти 2 записи"

# Поиск по части названия
found = find_records(records, "yth")
assert len(found) == 2, "Поиск 'yth' (подстрока) должен найти 2 записи"

# Поиск несуществующего
assert find_records(records, "Java") == [], "Поиск 'Java' должен вернуть []"

# Пустой запрос — ошибка
try:
    find_records(records, "   ")
except ValueError:
    pass
else:
    assert False, "Ошибка пустого запроса не обнаружена!"

print("  [OK] Добавление и поиск")

# ==========================================
# 3. Тесты статуса и удаления
# ==========================================
# set_completed — успех
assert set_completed(records, 1, True) is True
assert records[0]["completed"] is True

# set_completed — неизвестный ID
assert set_completed(records, 99, True) is False
assert records[0]["completed"] is True  # статус не должен был измениться

# Удаляем запись с МИНИМАЛЬНЫМ ID (id=1), чтобы max=2 сохранился
assert delete_record(records, 1) is True
assert len(records) == 1
assert records[0]["id"] == 2, "ID=2 должен сохраниться, не перенумеровываться"

# Удаление неизвестного ID
assert delete_record(records, 99) is False
assert len(records) == 1

# Новый ID = max(2) + 1 = 3
r3 = add_record(records, "Новая", "работа", 20)
assert r3["id"] == 3, "После удаления id=1 новый ID должен быть 3 (max=2 + 1)"

print("  [OK] Статус и удаление")

# ==========================================
# 4. Тесты статистики
# ==========================================
# Сейчас в records: [id=2, "Python", "учёба", 10, False], [id=3, "Новая", "работа", 20, False]
stats = statistics(records)

assert stats["total"] == 2, "Всего должно быть 2"
assert stats["completed"] == 0, "Выполненных 0"
assert stats["not_completed"] == 2, "Невыполненных 2"
assert stats["total_amount"] == 30, "Сумма баллов = 10 + 20 = 30"
assert stats["by_category"]["работа"] == 20
assert stats["by_category"]["учёба"] == 10

# Проверка сортировки категорий (по алфавиту: работа < учёба)
categories_order = list(stats["by_category"].keys())
assert categories_order == ["работа", "учёба"], "Категории должны быть отсортированы по алфавиту"

# Пустая статистика
empty_stats = statistics([])
assert empty_stats["total"] == 0
assert empty_stats["completed"] == 0
assert empty_stats["total_amount"] == 0
assert empty_stats["by_category"] == {}

print("  [OK] Статистика")

print("\nВсе тесты logic.py пройдены!")