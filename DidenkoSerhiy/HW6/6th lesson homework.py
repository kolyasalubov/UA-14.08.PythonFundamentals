#task 6.1

even_numbers = []
odd_numbers = []
other_numbers = []

for item in range(1, 11):
    if item % 2 == 0:
        even_numbers.append(item)
print("Even numbers that are divisible by 2 (from 1 to 10):", even_numbers)

for item in range(1, 11):
    if item % 3 == 0:
        odd_numbers.append(item)
print("Odd numbers that are divisible by 3 (from 1 to 10):", odd_numbers)

for item in range(1,11):
    if item % 2 != 0 and item % 3!= 0:
        other_numbers.append(item)
print("Numbers that are not divisible by 2 and 3:", other_numbers)

#task 6.2

login = input("Enter your login:\n")

while login != 'First':
    print("Login needs to be \"First\" ")
    break
else:
    print("Great, you've entered the correct login")