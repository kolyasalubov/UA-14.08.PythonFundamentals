# Гра, що вгадує число загадане програмою
import random

random_number = random.randint(0, 100)

print("Ця програма загадує число в діапазоні віж 1 до 100. Задача гравя вгадати число")

for i in range(10):
    try:
        user_number = int(input("Введите вашу догадку: "))
    except ValueError:
        print("Пожалуйста, введите целое число.")
        continue
    
    if user_number < random_number:
        print("Загаданное число больше. Попробуйте еще раз.")
    elif user_number > random_number:
        print("Загаданное число меньше. Попробуйте еще раз.")
    else:
        print("Поздравляю!")
        break
else:
    print("Ви вичерпали кількість спроб!")