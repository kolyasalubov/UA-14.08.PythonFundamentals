# Введення чотиризначного натурального числа
number = int(input("Введіть чотиризначне натуральне число: "))

# Перевірка, що число дійсно чотиризначне
if 1000 <= number <= 9999:
    # Обчислення добутку цифр числа
    digit1 = number // 1000
    digit2 = (number // 100) % 10
    digit3 = (number // 10) % 10
    digit4 = number % 10
    product = digit1 * digit2 * digit3 * digit4

    # Пошук числа в зворотньому порядку
    reversed_number = int(str(number)[::-1])

    # Створення списка з цифр числа
    digits_list = [digit1, digit2, digit3, digit4]

    # Сортування цифр за зростанням
    sorted_digits = sorted(digits_list)

    # Виведення результатів
    print(f"Добуток цифр числа: ", product)
    print(f"Число в зворотньому порядку: ", reversed_number)
    print(f"Цифри числа в порядку зростання: ", sorted_digits)
else:
    print("Ви ввели невірне число. Введіть чотиризначне натуральне число.")
