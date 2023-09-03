amount_of_numbers = int(input("Enter amount of numbers you want to have in list : "))

int_numbers = [number for number in range(amount_of_numbers)]
float_numbers = []

for float_number in int_numbers:
    float_numbers.append(float(float_number))


print("integer list : ", int_numbers)
print("float list : ", float_numbers)
