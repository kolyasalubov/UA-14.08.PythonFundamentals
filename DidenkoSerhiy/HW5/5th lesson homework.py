#task 5.1
import time

integer_numbers = [24, 25, 18, 19, 20]
print("This is the list with the integer numbers:", integer_numbers)
time.sleep(2)
print("Let's convert the list to float type")
for item in integer_numbers:
    print(float(item))

#task 5.2
time.sleep(3)

entered_number = int(input("Enter a number and you'll see Fibonacci numbers up to your number: "))

first_fibonacci_number = 0
second_fibonacci_number = 1

while first_fibonacci_number <= entered_number:
    print(first_fibonacci_number, end = ',')

    next_fibonacci_number = second_fibonacci_number
    second_fibonacci_number = first_fibonacci_number + next_fibonacci_number
    first_fibonacci_number = next_fibonacci_number

print("\nList of Fibonacci numbers up to", entered_number, "is generated.")

#task 5.3 factorial
time.sleep(3)

user_number = int(input("Enter the number you want to calculate the factorial for:"))
factorial = 1

for i in range(1, user_number + 1):
    factorial = factorial * i
print("Factorial of the entered number is:", factorial)