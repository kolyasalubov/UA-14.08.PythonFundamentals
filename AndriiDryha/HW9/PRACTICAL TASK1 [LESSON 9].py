import random

counter = 10

number = random.randint(1, 100)

while True:

  guess_number = int(input("Enter your number from range: 1 to 100: \n"))

  if guess_number == number:
    print("Good job! You are winner!")
    break
  counter -= 1
  if counter > 0 and 1 <= guess_number <= 100 and guess_number < number:
    print("Your number is less! Left", counter, "tries. Try again.")
  elif counter > 0 and 1 <= guess_number <= 100 and guess_number > number:
    print("Your number is more! Left", counter, "tries. Try again.")
  elif counter > 0 and 1 > guess_number or guess_number > 100:
    print("Your number is not in range 1 to 100! Left", counter, "tries. Try again.")
  else:
    print("Tries exhaused.")
    break