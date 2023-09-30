import random
number = random.randint(1, 100)
attempts = 10
counter = 0
while counter<= attempts:
    your_number = int((input("Enter ur number from 1 to 100: ")))
    if your_number == number :
        print("U r right")
        break
    elif 1<=your_number<=40 and your_number<number:
        print(f"Attempt {counter + 1}: Secret number is higher. Try again!")
    elif 1<=your_number<=40 and your_number>number:
        print("Attempt {counter + 1}: Secret number is lower. Try again!")
    elif not 1<=your_number<=40:
        print("Ur number is out of range. Try something between 1 to 40!")

    counter+=1

    if counter == attempts and your_number != number:
        print(f"Sorry, you've reached the maximum number of attempts.The secret number was {number}. Let's try again :) ")