inp = input('Введите целые числа через пробел: ').split()
nums = list(map(int, inp))
if len(nums) > 0:
    mx = max(nums)
    id = [x for x, _ in enumerate(nums) if nums[x] == mx]
    print(f'Индексы максимумов: {id}')
else:
    print('Нет данных')
