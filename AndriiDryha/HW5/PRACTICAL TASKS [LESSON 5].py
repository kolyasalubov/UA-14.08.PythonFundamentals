# # Task 1

# number_list = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
# number_list = [float (x) for x in number_list]

# print(number_list)

# Task 2
Fibonacci_number1 = 0
Fibonacci_number2 = 1

n = int(input("limit for the Fibonacci number"))

print(Fibonacci_number1, Fibonacci_number2, end=' ')

for i in range(2, n):
    Fibonacci_number1, Fibonacci_number2 = Fibonacci_number2, Fibonacci_number1 + Fibonacci_number2
    print(Fibonacci_number2, end=' ')


