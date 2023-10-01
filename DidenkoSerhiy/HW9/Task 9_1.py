#9.1
import random

count = 0

random_number = random.randint(1, 101)

while count < 10:
    count += 1
    user_input = int(input("Enter your number from 1 to 100: "))
    print("Try to guess the number from 1 to 100")
    if user_input == random_number:
        print("Great! You guessed the number")
        break
    elif user_input < random_number:
        print("Your number is less, try more")
    elif user_input > random_number:
        print("Your number is bigger, try more")