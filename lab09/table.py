def row_sums(matrix):
    res = []
    for row in matrix:
        res.append(sum(row))
    return res

def column_sums(matrix):
    if not matrix:
        return []
    res = [0 for _ in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for row in matrix:
            res[i] += row[i]
    return res

def diagonal_pattern(size):
    res = [[0]*size for _ in range(size)]
    for row in range(size):
        for column in range(size):
            if row == column:
                res[row][column] = 0
            elif row < column:
                res[row][column] = 1
            else:
                res[row][column] = 2
    return res

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
