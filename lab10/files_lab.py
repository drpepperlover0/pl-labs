def read_matrix(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()

    if not lines:
        raise ValueError("Файл пустой")

    header = lines[0].split()
    if len(header) != 2:
        raise ValueError("Строка 1: ожидалось 2 значения (строки и столбцы)")

    try:
        rows = int(header[0])
        columns = int(header[1])
    except ValueError:
        raise ValueError("Строка 1: заголовок должен состоять из целых чисел")

    if rows <= 0 or columns <= 0:
        raise ValueError("Строка 1: количество строк и столбцов должно быть больше нуля")

    data = lines[1:]

    if len(data) != rows:
        raise ValueError(f"Ожидалось {rows} строк (сейчас - {len(data)})")

    result = []
    for i, line in enumerate(data, 2):
        parts = line.split()
        if len(parts) != columns:
            raise ValueError(f"Строка {i}: ожидалось {columns} чисел (сейчас - {len(parts)})")
        try:
            row = [int(x) for x in parts]
        except ValueError:
            raise ValueError(f"Строка {i}: содержится нечисловая ячейка")
        result.append(row)

    return result


def selected_sum(matrix):
    if not matrix:
        return 0
    s = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] in range(-2, 4):
                s += matrix[row][column]
    return s