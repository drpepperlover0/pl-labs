a = float(input('Первое число: '))
b = float(input('Второе число: '))
oper = input('Введите операцию: ')

if oper == '+':
    print(f'{a} + {b} == {a+b:.2f}')
elif oper == '-':
    print(f'{a} - {b} == {a-b:.2f}')
elif oper == '*':
    print(f'{a} * {b} == {a*b:.2f}')
elif oper == '/':
    if b == 0:
        print('Деление на ноль запрещено')
    else:
        print(f'{a} / {b} == {a/b:.2f}')
else:
    print('Неизвестная операция')
