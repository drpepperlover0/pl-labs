from table import *

# 1. Обычные проверки
assert row_sums([[1, 2, 3], [4, 5, 6]]) == [6, 15]
assert column_sums([[1, 2, 3], [4, 5, 6]]) == [5, 7, 9]

# 2. Граничные проверки (матрица 1x1)
assert row_sums([[7]]) == [7]
assert column_sums([[7]]) == [7]
assert diagonal_pattern(1) == [[0]]

# 3. Матрица-столбец
assert row_sums([[1], [-1], [0]]) == [1, -1, 0]
assert column_sums([[1], [-1], [0]]) == [0]

# 4. Пустая матрица
assert row_sums([]) == []
assert column_sums([]) == []
assert transform([]) == []

# 5. Узор 3х3
assert diagonal_pattern(3) == [[0, 1, 1], [2, 0, 1], [2, 2, 0]]

# 6. Индивидуальный вариант (Вариант 7: положительные += 5)
control_matrix = [[-2, 0, 3], [4, -5, 6]]
expected_result = [[-2, 0, 8], [9, -5, 11]]
assert transform(control_matrix) == expected_result

# 7. Проверка неизменяемости исходной матрицы (как в ТЗ)
result = transform(control_matrix)
result[0][0] = 67
assert control_matrix[0][0] == -2

# 8. Дополнительный модуль (рекурсия)
assert factorial(0) == 1
assert factorial(3) == factorial_iterative(3) == 6
assert factorial(5) == factorial_iterative(5) == 120

print("Все тесты пройдены успешно!!!")
