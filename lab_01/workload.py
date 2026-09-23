obj1 = input('Введите первый предмет: ')
obj2 = input('Введите второй предмет: ')
cnt1 = int(input('Кол-во занятий в 1 предмете: '))
cnt2 = int(input('Кол-во занятий во 2 предмете: '))
obj_time1 = int(input('Продолжительность одного занятия (мин): '))
obj_time2 = int(input('Продолжительность второго занятия (мин): '))
time_week = int(input('Доступное время на неделю (час): '))
if cnt1 >= 0 and cnt2 >= 0 and obj_time1 > 0 and obj_time2 > 0 and (obj_time1 * cnt1 + obj_time2 * cnt2) <= time_week*60:
    first = cnt1*obj_time1
    second = cnt2*obj_time2
    all_work = first+second
    print(f'\n1 занятие: {first}\n2 занятие: {second}')
    print(f'Общая нагрузка: {all_work} мин ИЛИ {(all_work/60):.2f} часов')
    print(f'Остаток свободного времени: {time_week-all_work/60:.2f} часа\nНагрузка за 4 недели: {(all_work/60)*4:.2f} часа')
else:
    print('Некорректные данные')
    