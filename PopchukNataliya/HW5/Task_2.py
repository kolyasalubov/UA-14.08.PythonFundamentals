# Fibonacci numbers
n = int(input(" Enter a number(n):"))


def print_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b


print("Fibonacci number up to", n, "are")
print_fibonacci(n)
