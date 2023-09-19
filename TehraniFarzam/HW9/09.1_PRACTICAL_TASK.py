import random

random_number = random.randint(0, 100)
count = 0

while count < 10:
    input_guess_number = input("Guess a number from 0 to 100: ")

    if input_guess_number.isdigit():
        guess_number = int(input_guess_number)
        count += 1
        if guess_number > random_number:
            print("Your number is too high. Try again!")
        elif guess_number < random_number:
            print("Your number is too low. Try again!")
        else:
            print(f"YOU WIN!!!. The number was {random_number}")
            break
    else:
        print("Invalid input.")
if count == 10:
    print(f"Game Over! The correct number was {random_number}")


