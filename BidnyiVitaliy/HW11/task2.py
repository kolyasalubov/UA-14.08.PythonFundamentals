# Write a program that prompts the user to enter their age, and then displays a
# message stating whether the age is even or odd. The program must provide the ability
# to enter a negative number, and in this case generate an exception. The master code
# should call a function that processes the information entered.

def days_func(day_index):
    days = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

    if day_index in range(0, 6):
        return days[day_index]
    else:
        message = 'Negativ Number, try again!'
        return message


try:
    day = int(input('Enter the number of a day : '))
    print(days_func(day))
except ValueError:
    print('Must be an integer!')