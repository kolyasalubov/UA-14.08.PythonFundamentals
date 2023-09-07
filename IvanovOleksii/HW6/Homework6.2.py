from colorama import *
login = 'First'
while True:
    log_input = input(Style.RESET_ALL + 'Enter your login: ')
    if log_input == login:
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT +'Login successful!')
        break
    else:
        print(Fore.RED + Style.BRIGHT + 'The login is incorrect, try again!\n')