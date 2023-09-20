# Вивід парних чисел які діляться на 2
print("Парні числа, які діляться на 2:")
for number in range(2, 11, 2):
    print(number)

# Вивід непарних чисел, які діляться на 3
print("\nНепарні числа, які діляться на 3:")
for number in range(1, 11, 2):
    if number % 3 == 0:
        print(number)

# Вивід чисел, які не діляться ні на 2, ні на 3
print("\nЧисла, які не діляться ні на 2, ні на 3:")
for number in range(1, 11):
    if number % 2 != 0 and number % 3 != 0:
        print(number)
