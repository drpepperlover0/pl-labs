a, b = int(input('Введите первое число: ')), int(input('Введите второе число: '))
if a < b:
    for x in range(a, b+1):
        print(x)
else:
    for x in range(a, b-1, -1):
        print(x)
