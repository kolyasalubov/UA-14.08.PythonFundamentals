num = int(input("Enter a number (n): "))

fib1, fib2 = 0, 1

print(fib1, fib2, end=" ")

while fib2 <= num:
    fib_next = fib1 + fib2
    print(fib_next, "\n")
    fib1, fib2 = fib2, fib_next
