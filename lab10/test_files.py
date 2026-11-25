from pathlib import Path
from tempfile import TemporaryDirectory
from files_lab import read_matrix, selected_sum

with TemporaryDirectory() as directory:
    path = Path(directory) / "matrix.txt"

    # 1. Успешное чтение
    path.write_text("2 3\n1 -2 3\n4 0 -6\n", encoding="utf-8")
    matrix = read_matrix(path)
    assert matrix == [[1, -2, 3], [4, 0, -6]]
    assert selected_sum(matrix) == -2

    # 2. Пустой файл
    path.write_text("", encoding="utf-8")
    try:
        read_matrix(path)
    except ValueError:
        pass
    else:
        assert False, "Ошибка пустого файла не обнаружена!"

    # 3. Заголовок 0 3
    path.write_text("0 3\n", encoding="utf-8")
    try:
        read_matrix(path)
    except ValueError:
        pass
    else:
        assert False, "Ошибка заголовка 0 3 не обнаружена!"

    # 4. Неверное количество колонок
    path.write_text("1 2\n1\n", encoding="utf-8")
    try:
        read_matrix(path)
    except ValueError:
        pass
    else:
        assert False, "Ошибка количества колонок не обнаружена!"

    # 5. Нечисловая ячейка
    path.write_text("1 2\n1 x\n", encoding="utf-8")
    try:
        read_matrix(path)
    except ValueError:
        pass
    else:
        assert False, "Ошибка нечисловой ячейки не обнаружена!"

    # 6. Лишние строки данных (1 1, а строк две)
    path.write_text("1 1\n5\n6\n", encoding="utf-8")
    try:
        read_matrix(path)
    except ValueError:
        pass
    else:
        assert False, "Ошибка лишних строк не обнаружена!"

    # 7. Отсутствующий файл
    missing_path = Path(directory) / "no_such_file.txt"
    try:
        read_matrix(missing_path)
    except FileNotFoundError:
        pass
    else:
        assert False, "Ошибка отсутствия файла не обнаружена!"

print("Все проверки пройдены!")