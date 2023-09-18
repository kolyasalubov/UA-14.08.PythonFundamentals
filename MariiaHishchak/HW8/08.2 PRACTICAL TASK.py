# Task 1
import re
def if_has_letters(string):
    return bool(re.search('[a-zA-Z]', string))

def if_has_numbers(int):
    return bool(re.search('[0-9]', int))

def if_has_sign(string):
    return bool(re.search('[$#@]', string))

while True:
    password = str(input("Enter your password: "))
    if len(password) >= 16 and len(password) <= 6:
        print("Your password length must be between 6 and 16 characters")
    elif if_has_letters(password) == False:
        print("Your password must contain at least one letter.")
    elif if_has_numbers(password) == False:
        print("Your password must contain at least one number.")
    elif if_has_sign(password) == False:
        print("Your password must contain at least one of the following characters: $, #, @")
    else:
        result = "Your password is valid"
        print(result)
        break
