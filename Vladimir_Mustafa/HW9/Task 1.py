import random
num = random.randint(1, 100)

print('Guess a number from 1 to 100, you have 10 attempts')

attempt = 0

while attempt <= 10:
    user_num = int(input('Enter number: '))
    attempt += 1

    if user_num < num and 0 <= user_num <= 100 :
        print('The number is higher. Try again.')

    elif user_num > num and 0 <= user_num <= 100:
        print('The number is lower. Try again.')

    elif user_num == num and 0 <= user_num <= 100:
        print(f'You are win, it is {num}')
        break

    else:
        break



