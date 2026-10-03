number = int(input("Введите число: "))

for x in range(2, int(number**0.5)+1):
    if number % x == 0:
        print("Составное")
        break
else:
    print("Простое")