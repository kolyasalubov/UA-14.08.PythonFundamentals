
# 09.1 PRACTICAL TASK / [GITHUB TOPIC 9]

#Task 1
import random

# Task 1
secret_number = random.randint(1, 100)

print("\nWelcome to the game 'Guess the number from 1 to 100'!")
print("You have 10 attempts to guess the number.")


attempts = 0
while True:
    guess = input("\nPlease enter your option: ")
    if not guess.isdigit():
        print("\n\t_____It's not a number. Please enter a number between 1 and 100_____")
    else:
        guess = int(guess)
        if guess < 1 or guess > 100:
            print("\n\t\t_____Your number is not in the range from 1 to 100_____")
        else:
            attempts += 1
#-------------------------------------------------------------------------------------------------------                               
            if secret_number == guess or secret_number == guess and attempts == 10:
                print("Congratulations! You are a winner!!!.")
                print(f"Please try again.  Attempts used {attempts}")
                break
            elif secret_number != guess and attempts == 10:
                print(f"Sorry, please try again. Attempts used {attempts}")
                print(f"My secret number {secret_number}")
                break
#-------------------------------------------------------------------------------------------------------            
            print(f"The guessed number is less. Attempts used {attempts}") if (secret_number > guess) \
                else print(f"The guessed number is greater. Attempts used {attempts}")
      
