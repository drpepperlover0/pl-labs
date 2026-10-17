s = input('Введите строку: ')
k = s.count(':')
while ':' in s:
    s = s.replace(':', '-')
print(f'Кол-во замен: {k}\nНовая строка: {s}')