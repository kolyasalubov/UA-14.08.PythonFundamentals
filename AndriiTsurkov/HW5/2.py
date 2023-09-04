fibonacci_calculation_number = input("Please enter a digit to calculate Fibonacci numbers: ")

if not fibonacci_calculation_number.isdecimal():
    print("Error: You have enter not a number!")
    exit()

fibonacci_numbers = [0, 1]
for i in range(1, int(fibonacci_calculation_number)):
    if i >= 1:
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i])

print ("List of Fibonacci numbers:", fibonacci_numbers)
