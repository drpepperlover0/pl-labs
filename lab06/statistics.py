inp = input('Введите целые числа через пробел: ')
nums = [int(x) for x in inp.split()]
if len(nums) == 0:
    print('Нет данных')
else:
    mn, mx = nums[0], nums[0]
    for n in nums:
        if n < mn:
            mn = n
        elif n > mx:
            mx = n
    print(f'Количество: {len(nums)} | Сумма: {sum(nums)}')
    print(f'Минимум: {mn} | Максимум: {mx}')
    print(f'Среднее арифметическое: {(sum(nums) / len(nums)):.2f}')