import random
number = random.randint(0, 100)
count = 0

while count <= 10:
    user_number = int(input("Enter the number from 0 to 100->"))
    count += 1
    if user_number > number:
        print("Try lower!")
    elif user_number < number:
        print("Try higher!")
    else:
        print(f"You won!!!. The number was {number}")
        break
if count == 11:
    print(f"The correct number was {number}. Try another time!")