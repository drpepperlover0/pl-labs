last_name = input('Введите фамилию: ')
name = input('Введите имя: ')
group = input('Введите группу: ')
city = input('Введите ваш город: ')
age = int(input('Ваш возраст: '))
fav = input('Любимый предмет: ')
cnt_hrs_week = float(input('Часов в неделю: '))
if 1 <= age <= 120 and 0 <= cnt_hrs_week <= 168:
    print('~~~ Карточка студента ~~~')
    print(f'{name} {last_name}\nВозраст через 4 года: {age+4}\nЗа 4 недели: {cnt_hrs_week*4:.2f}\nСреднее время за неделю: {cnt_hrs_week/7:.2f}')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~')
else:
    print('Неправильно введены данные')