# Task 1
list1 = [1, 2, 3]
for digit in list1:
    x = float(digit)
    print(x)
# Task 2
n = int(input("Enter n number: "))
fibonacci_num = [0, 1]
sum_ = 0
while len(fibonacci_num) < n:
    sum_ = fibonacci_num[-1] + fibonacci_num[-2]
    fibonacci_num.append(sum_)
print(f"Fibonacci numbers: {fibonacci_num}")

# Task 3
number = int(input("Enter number: "))
product = 1
i = 0
while i < number:
    i += 1
    product *= i
print(f"Factorial of entered number: {product}")
