import random
def divine_number():
    number = random.randint(1, 100)
    attempts = 0
    print("Welcome the Number Game!")
    print("I've chosen a number between 1 and 100. You have 10 tries to divine it.")
    while attempts < 10:
        user_guess = int(input(f"Attempt {attempts+1}/10. Enter your divine: "))
        if user_guess == number:
            print(f"Congratulations! You've divined the number {number}!")
            return
        elif user_guess < number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
        attempts += 1
    print(f"Sorry, you've used all 10 attempts. The number was {number}.")
# Run the game
divine_number()
