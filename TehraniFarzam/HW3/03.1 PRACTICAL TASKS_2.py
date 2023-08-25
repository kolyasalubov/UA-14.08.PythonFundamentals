number = input("Enter a four-digit number: ")

if len(number) != 4 or not number.isdigit():
    print("Invalid number")
else:
    four_digit_number = int(number)
# ====== find the product of the four-digit number ======
    dig_1 = four_digit_number // 1000
    dig_2 = (four_digit_number // 100) % 10
    dig_3 = (four_digit_number //10) % 10
    dig_4 = four_digit_number % 10

    product = dig_1 * dig_2 * dig_3 * dig_4

    print(f"Product of the digits of your number is: {product} ")

# ====== write the number in reverse order ======
reversed_number = number[::-1]
print(f"This is your number in reversed order: {reversed_number}")

# ====== ascending sort the number =======
ascending_sorted_number = ''.join(sorted(str(number)))
print(f"This is the ascending sort version of your number: {ascending_sorted_number}")