order_name = input("Введите название заказа: ")
customer = input("Введите имя заказчика: ")

first_pos_name = input("Введите название первой позиции: ")
first_pos_count = int(input("Введите количество первой позиции: "))
first_pos_cost = float(input("Введите цену первой позиции: "))
second_pos_name = input("Введите название второй позиции: ")
second_pos_count = int(input("Введите количество второй позиции: "))
second_pos_cost = float(input("Введите цену второй позиции: "))
delivery_cost = float(input("Введите стоимость доставки: "))
inputed_money = float(input("Введите внесённую стоимость: "))
discount = float(input("Введите скидку на заказ (%): ")) / 100

first_pos_total = first_pos_cost * first_pos_count
second_pos_total = second_pos_cost * second_pos_count

total_without_delivery = first_pos_total + second_pos_total
total_without_delivery_discount = total_without_delivery * (1 - discount)
total_with_delivery_discount = total_without_delivery_discount + delivery_cost
total_pos_count = first_pos_count + second_pos_count
change = inputed_money - total_with_delivery_discount

print(f"\n~~~~Заказ: {order_name}, от {customer}~~~~")
print(f"Название: {first_pos_name} | Количество: {first_pos_count} | Цена: {first_pos_cost:.2f} руб | Стоимость: {first_pos_total:.2f} руб")
print(f"Название: {second_pos_name} | Количество: {second_pos_count} | Цена: {second_pos_cost:.2f} руб | Стоимость: {second_pos_total:.2f} руб")

print(f"\nСтоимость товаров без доставки: {total_without_delivery:.2f} руб")
print(f"Скидка ({discount*100:.2f}%): {total_without_delivery * discount:.2f} руб")
print(f"Общая сумма с доставкой и скидкой: {total_with_delivery_discount:.2f} руб")
print(f"Общее количество товара: {total_pos_count}")
print(f"Сдача: {change:.2f} руб")
