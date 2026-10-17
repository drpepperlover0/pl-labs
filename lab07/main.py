from functions import *

number = int(input("Введите целое число для подсчёта суммы: "))
print(f"Сумма: {sum_digits(number)}")

numbers = [int(number) for number in input("Введите числа через пробел: ").split()]
print(f'Среднее арифметическое: {average(numbers)}' if (average(numbers)) else "Нет данных")

text = input("Введите текст: ")
print(f'Нормализованный текст - {normalize_text(text)}')

numbers = [int(num) for num in input("Введите числа через пробел: ").split()]
threshold = int(input("Введите порог: "))
print(f'Результат: {select_numbers(numbers, threshold)}')

text = input("Введите текст: ")
print(f'Палиндром: {is_palindrome(text)}')