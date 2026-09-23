first_room = input('Введите название 1-ой аудитории: ')
second_room = input('Введите название 2-ой аудитории: ')
print(f'\nПервая аудитория: [{first_room}] | Вторая аудитория: [{second_room}]')

t = first_room
first_room = second_room
second_room = t
print(f'Первая аудитория: [{first_room}] | Вторая аудитория: [{second_room}]')
