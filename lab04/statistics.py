n = int(input('Введите целое число n: '))

mx = int(input())
s = mx
cnt_p = 1 if mx > 0 else 0
for x in range(n-1):
    a = int(input())
    s += a
    if a > 0:
        cnt_p += 1
    if a > mx:
        mx = a
print(f'Сумма чисел: {s}\nЧисло положительных значений: {cnt_p}\nМаксимум: {mx}')
