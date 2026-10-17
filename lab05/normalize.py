s = input('Введите строку: ')
res = s.strip()
while '  ' in res:
    res = res.replace('  ', ' ')
print(f'Исходная длина: {len(s)} | Новая длина: {len(res)}')
print(f'Нормализованный текст: {res} | Кол-во слов: {len(res.split())}')