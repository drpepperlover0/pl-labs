import table
from files_lab import read_matrix, selected_sum
from pathlib import Path


def read_positive_integer():
    while True:
        try:
            pos_int = int(input("Введите целое, положительное число: "))
        except ValueError:
            print("Ошибка, не целое число")
        else:
            if pos_int > 0:
                return pos_int
            print("Число должно быть больше нуля!")


def main():
    print("--- Проверка надежного ввода ---")
    number = read_positive_integer()
    print(f"Вы ввели корректное число: {number}\n")

    folder = Path(__file__).resolve().parent
    matrix_path = folder / "matrix.txt"
    report_path = folder / "report.txt"

    try:
        matrix = read_matrix(matrix_path)
    except FileNotFoundError:
        print("Ошибка: Файл не найден")
    except UnicodeError:
        print("Ошибка кодировки файла. Ожидается UTF-8")
    except ValueError as err:
        print(f"Ошибка формата данных: {err}")
    except OSError:
        print("Ошибка доступа к файлу")
    else:
        row_sum = table.row_sums(matrix)
        column_sum = table.column_sums(matrix)
        var = selected_sum(matrix)

        with open(report_path, 'w', encoding='utf-8') as file:
            file.write(f"Суммы строк: {' '.join(map(str, row_sum))}\n")
            file.write(f"Суммы столбцов: {' '.join(map(str, column_sum))}\n")
            file.write(f"Сумма элементов [-2; 3] (вариант 7): {var}\n")

        print("Отчёт успешно создан")


if __name__ == '__main__':
    main()