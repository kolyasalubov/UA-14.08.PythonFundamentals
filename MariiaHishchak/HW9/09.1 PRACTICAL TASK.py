# Task 1
import random
n = 0
random_number = random.randint(1, 100)
print("Random number:", random_number)
while(n < 10):
    n += 1
    print("")
    answer = int(input("Guess the number: "))
    if (answer == random_number):
        print("CONGRATULATION!!!")
        exit()
    elif (answer > 100 or answer < 1):
        print("Your number must be in diapason from 1 to 100!!!\nTry again!!!")
    else:
        print("WRONG!!!.Try again :( ")
