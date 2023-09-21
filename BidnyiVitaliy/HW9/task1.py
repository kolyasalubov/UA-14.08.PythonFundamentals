# Напишіть ігровий сценарій, який випадковим чином генерує число з діапазону
# 1 до 100 і просить користувача вгадати це число з 10 спроб.
# Програма зчитує введені користувачем числа та запитує користувача
# чи вгадане число більше чи менше за число, введене
# користувача. Гра має тривати, поки користувач не використає 10 спроб і не вгадає
# Кількість. Якщо користувач вгадав число, програма друкує a
# вітальне повідомлення, а якщо 10 спроб вичерпано, і користувач
# не встиг вгадати номер, то відповідне повідомлення є
# відображається.
# (для виконання завдання необхідно імпортувати випадковий модуль,
# і з нього функція randint())

import random

print("Hello! What is your name?")

name = input()

print("Hello, " + name + "! I guessed a number from 1 to 10. You have 10 tries to guess it.")

number = random.randint(1, 10)

tries = 0

while tries < 10:

   print("Attempt №" + str(tries+1) + ": ")

   guess = int(input())

   if guess == number:

       print("Congratulations, " + name + "! You guessed the number for " + str(tries+1) + " an attempt(-s)!")

       break

   elif guess < number:

       print("My number is more.")

   else:

       print("My number is less.")

   

   tries += 1

if tries == 3:

   print("Unfortunately, " + name + ", you didn't guess the number. I guessed the number " + str(number) + ".")


