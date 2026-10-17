s = input('Введите строку: ')
s = s.split()
c = 0
for i in range(len(s)):
    s[i] = s[i].strip('.,!?;:').lower()
    if s[i].count('р') >= 1:
        print(s[i])
        c += 1
if c == 0:
    print('Нет совпадений')
print(f'Количество слов: {c}')