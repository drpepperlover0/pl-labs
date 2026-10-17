inp = input('Введите целые числа через пробел: ').split()
nums = [int(x) for x in inp if int(x) % 3 != 0]
print(f'Исходный список: {nums}')
print(f'Количество: {len(nums)} | Сумма: {sum(nums)}')
print(f'Сортировка по возрастанию: {sorted(nums)}')