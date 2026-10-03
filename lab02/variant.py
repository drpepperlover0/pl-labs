total = int(input("Введите количество саженцев: "))
capacity = int(input("Введите количество саженцев в одном ряду: "))
print(f"Заполненных рядов саженцев: {total // capacity}\nОстаток: {total % capacity}\nРядов: {(total+capacity-1) // capacity}")