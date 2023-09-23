import random

random_value = random.randint(0, 100)
counter = 10

while counter > 0:
    input_value = int(input("Enter your number : "))
    counter -= 1
    if input_value == random_value:
        print("You win ")
        break
    elif input_value > random_value:
        print(f"Try again. Your number is bigger. You have {counter} attempts")
    elif input_value < random_value:
        print(f"Try again. Your number is lower. You have {counter} attempts")

