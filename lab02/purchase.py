price = int(input('Введите цену одной тетради: '))
count = int(input('Введите кол-во тетрадей: '))
paid = int(input('Введите сумму: '))

cost = price*count
print(f'\nСтоимость: {cost}\nСдача: {paid-cost}')
