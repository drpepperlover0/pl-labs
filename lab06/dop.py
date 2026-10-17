inp = input('Введите целые числа через пробел: ').split()
nums = list(map(int, inp))
i = 0
while i < len(nums):
    if nums[i] in nums[:i]:
        nums.pop(i)
    else:
        i += 1
print(nums)