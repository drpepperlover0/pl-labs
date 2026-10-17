inp = input('Введите целые числа через пробел: ').split()
nums = list(map(int, inp))
anums = list(map(abs, nums))
print(f'Исходный список: {nums} || Новый список: {anums}')