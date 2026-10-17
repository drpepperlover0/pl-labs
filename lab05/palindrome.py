a = input('Введите строку: ')
a = ''.join(a.lower().split())
if len(a) == 0:
    print('Нет текста')
else:
    if a == a[::-1]:
        print('Палиндром')
    else:
        print('Не палнидром')