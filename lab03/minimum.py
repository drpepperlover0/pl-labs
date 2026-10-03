a = int(input('Первое число: '))
b = int(input('Второе число: '))
c = int(input('Третье число: '))

mn = 0
if a <= b and a <= c:
    mn = a
elif b <= a and b <= c:
    mn = b
else:
    mn = c
print(f'\nМинимальное число: {mn}')