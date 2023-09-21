n = int(input("Enter the number of Fibonacci terms to generate: "))
a = 0
b = 1

fib_sequence = [a, b]

while len(fib_sequence) < n:
    a, b = b, a + b
    fib_sequence.append(b)

print(fib_sequence)