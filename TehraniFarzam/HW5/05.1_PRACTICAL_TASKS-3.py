num = int(input("Enter a number: "))

if num < 0:
    print("It's not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")




