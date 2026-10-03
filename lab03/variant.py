percent = int(input('Введите процент прочитанной книги: '))
if percent > 100 or percent < 0:
    print('Ошибка диапазона')
else:
    if 0 <= percent <= 9:
        print('Начало')
    elif 10 <= percent <= 89:
        print('Чтение')
    else:
        print('Почти готово')
