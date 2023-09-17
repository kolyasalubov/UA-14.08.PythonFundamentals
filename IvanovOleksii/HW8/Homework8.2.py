import re
from colorama import *


def password(input_password: str) -> str:
    if len(input_password) < 6:
        print(Fore.RED + 'Your password must be longer than 6 characters.')
    elif len(input_password) > 16:
        print(Fore.RED + 'Your password must be less than 16 characters long.')
    elif len(re.findall('[a-z]', input_password)) < 1:
        print(Fore.RED + 'Your password must contain at least one lowercase letter. Please try again!')
    elif len(re.findall('[A-Z]', input_password)) < 1:
        print(Fore.RED + 'Your password must contain at least one capital letter. Please try again!')
    elif len(re.findall('[0-9]', input_password)) < 1:
        print(Fore.RED + 'Your password must contain at least one number. Please try again!')
    elif len(re.findall(r"[$#@]", input_password)) < 1:
        print(Fore.RED + 'Your password must contain at least one of the characters [$, #, @]. Please try again!')
    else:
        return 'Welcome!'



while True:
    resoult = (password(input_password=input(Style.RESET_ALL + 'Enter your password: ')))
    if resoult == 'Welcome!':
        print(Fore.LIGHTGREEN_EX + resoult)
        break






