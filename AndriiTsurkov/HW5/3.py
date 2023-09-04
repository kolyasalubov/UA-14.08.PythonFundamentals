factorial_calculation_number = input("Enter a number to calculate the factorial: ")

if not factorial_calculation_number.isdecimal():
    print("Error: You have enter not a number!")
    exit()

factorial = 1
for i in range(1, int(factorial_calculation_number)+1):
    factorial *= i

print (f"Factorial of {factorial_calculation_number} will be: {factorial}")