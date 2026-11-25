def row_sums(matrix):
    result = []
    for row in matrix:
        result.append(sum(row))
    return result


def column_sums(matrix):
    if not matrix:
        return []
    result = [0 for _ in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for row in matrix:
            result[i] += row[i]
    return result


def diagonal_pattern(size):
    result = [[0]*size for _ in range(size)]
    for row in range(size):
        for column in range(size):
            if row == column:
                result[row][column] = 0
            elif row < column:
                result[row][column] = 1
            else:
                result[row][column] = 2
    return result

def transform(matrix):
    if not matrix:
        return []
    result = [r.copy() for r in matrix]
    rows_len = len(result[0])
    for row in range(len(result)):
        for column in range(rows_len):
            if result[row][column] > 0:
                result[row][column] += 5
    return result

def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number-1)

def factorial_iterative(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result
