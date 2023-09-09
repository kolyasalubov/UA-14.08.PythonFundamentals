#Task 1

for number in range(1, 11):
    if number % 2 == 0:
        print(f"{number} - even number")
    elif number % 3 == 0:
        print(f"{number} - odd number that is divisible by 3")
    else:
        print(f"{number} - number that is not divisible by 2 and 3")


