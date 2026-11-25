import json
from pathlib import Path
from tempfile import TemporaryDirectory

from storage import load_records, save_records

print("Начинаем тесты storage.py...")

with TemporaryDirectory() as tmp:
    tmp_path = Path(tmp)

    # ==========================================
    # 1. Сохранение и повторное чтение (round-trip)
    # ==========================================
    records = [
        {"id": 1, "title": "Python", "category": "учёба", "amount": 10, "completed": True},
        {"id": 2, "title": "Java", "category": "учёба", "amount": 5, "completed": False},
    ]
    path = tmp_path / "data.json"

    save_records(path, records)
    assert path.exists(), "Файл должен быть создан"

    loaded = load_records(path)
    assert loaded == records, "Данные после чтения должны совпадать с исходными"

    print("  [OK] Сохранение и чтение")

    # ==========================================
    # 2. Кириллица сохраняется читаемо (ensure_ascii=False)
    # ==========================================
    text = path.read_text(encoding="utf-8")
    assert "учёба" in text, "Кириллица должна быть читаемой в файле, а не в \\uXXXX"
    assert "\\u" not in text, "В файле не должно быть escape-последовательностей \\u"

    print("  [OK] Кириллица в файле читаема")

    # ==========================================
    # 3. Отсутствующий файл → FileNotFoundError
    # ==========================================
    missing = tmp_path / "no_such_file.json"
    try:
        load_records(missing)
    except FileNotFoundError:
        pass
    else:
        assert False, "FileNotFoundError не обнаружен!"

    print("  [OK] Отсутствующий файл")

    # ==========================================
    # 4. Поврежденный JSON → JSONDecodeError
    # ==========================================
    bad_json = tmp_path / "bad.json"
    bad_json.write_text("{это не JSON}", encoding="utf-8")
    try:
        load_records(bad_json)
    except json.JSONDecodeError:
        pass
    else:
        assert False, "JSONDecodeError не обнаружен!"

    print("  [OK] Поврежденный JSON")

    # ==========================================
    # 5. Неверная структура → ValueError (от validate_records)
    # ==========================================
    bad_structure = tmp_path / "bad_structure.json"
    bad_structure.write_text(
        json.dumps([{"id": "не число", "title": "X", "category": "Y",
                     "amount": 1, "completed": False}], ensure_ascii=False),
        encoding="utf-8"
    )
    try:
        load_records(bad_structure)
    except ValueError:
        pass
    else:
        assert False, "ValueError от validate_records не обнаружен!"

    print("  [OK] Неверная структура данных")

    # ==========================================
    # 6. Пустой список [] — валиден и читается
    # ==========================================
    empty_path = tmp_path / "empty.json"
    save_records(empty_path, [])
    assert load_records(empty_path) == [], "Пустой список должен читаться корректно"

    print("  [OK] Пустой список")

    # ==========================================
    # 7. Перезапись файла (save поверх существующего)
    # ==========================================
    save_records(path, [records[0]])
    loaded = load_records(path)
    assert len(loaded) == 1, "После перезаписи должна остаться 1 запись"
    assert loaded[0]["id"] == 1

    print("  [OK] Перезапись файла")

print("\nВсе тесты storage.py пройдены!")