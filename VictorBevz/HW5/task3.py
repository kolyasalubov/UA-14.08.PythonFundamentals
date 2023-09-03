def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Enter a number: "))

factorial_result = factorial(n)
print("Factorial of", n, ":", factorial_result)
