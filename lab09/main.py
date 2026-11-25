from table import *

rows = int(input("Введите количество строк в таблице: "))
while rows <= 0:
    rows = int(input("Некорректные данные! Введите количество строк (положительное число): "))

columns = int(input("Введите количество столбцов в таблице: "))
while columns <= 0:
    columns = int(input("Некорректные данные! Введите количество столбцов (положительное число): "))

table = [[0]*columns for _ in range(rows)]
for i in range(rows):
    row = input(f"Введите {i+1} строку через пробел ({columns} значений): ").split()
    while len(row) != columns:
        row = input(f"Ошибка! Нужно ровно {columns} чисел. Повторите {i+1} строку: ").split()
    table[i] = list(map(int, row))

print("\n~~~ Исходная таблица ~~~")
for r in table:
    print(*r)

orig = [row.copy() for row in table]
print(f"\nСумма строк: {row_sums(table)}")
print(f"Сумма столбцов: {column_sums(table)}")
assert orig == table

# ~~~ Индивидуальный вариант 7 ~~~
print("\n~~~ Преобразованная таблица (положительные увеличить на 5) ~~~")
transformed = transform(table)
for r in transformed:
    print(*r)


print()
size = int(input("Введите размер квадратной матрицы (положительное число): "))
while size <= 0:
    size = int(input("Некорректные данные! Введите положительный размер: "))

print("~~~ Диагональный узор ~~~")
pattern = diagonal_pattern(size)
for r in pattern:
    print(*r)