# # Task 1
# n = int(input("Enter the first number of the list: \n"))
# m = int(input("Enter the limit number of the list: \n"))
# r = int(input("Enter the list gap: \n"))

# number_list = list(range(n, m, r))
# number_list = [float (x) for x in number_list]

# print(number_list)

# # Task 2
# Fibonacci_number1 = 0
# Fibonacci_number2 = 1

# n = int(input("Enter the limit for the sequence of Fibonacci numbers: \n"))

# while Fibonacci_number1 < n:
#     print(Fibonacci_number1, end = ' ')
#     Fibonacci_number1, Fibonacci_number2 = Fibonacci_number2, Fibonacci_number1 + Fibonacci_number2

# Task 3
n = int(input("Enter your number: \n"))
m = str(n)
factorial = 1
while n > 1:
    factorial *= n
    n -= 1

print(f'{m}! = {factorial}')