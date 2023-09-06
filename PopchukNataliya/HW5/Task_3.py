# calculate factorial
n = int(input("Enter a number: "))

def calculate_factorial(n):
    factorial=1
    for i in range (1, n+1):
        factorial *= i
    return factorial
if n<0 :
    print("Factorial is not defined for negative numbers")
else:
    result= calculate_factorial(n)
    print(f"Factorial of {n} is {result}")