import random

random_number = random.randint(0, 100)
count = 0
max_attempts = 10

print("Welcome to the Guess the Number game!")
print(f"Guess a number from 0 to 100. You have {max_attempts} attempts.")

while count < max_attempts:
    input_guess_number = input("Enter your guess: ")

    if input_guess_number.isdigit():
        guess_number = int(input_guess_number)
        count += 1

        if guess_number > random_number:
            print("Your number is too high. Try again!")
        elif guess_number < random_number:
            print("Your number is too low. Try again!")
        else:
            print(f"YOU WIN!!! The number was {random_number}")
            break
    else:
        print("Invalid input.")

if count == max_attempts:
    print(f"Game Over! The correct number was {random_number}")
