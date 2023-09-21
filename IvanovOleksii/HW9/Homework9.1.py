import random
import colorama


def randomNumber():
    rand_num = random.randint(1, 100)
    tries = 10
    while tries > 0:
        try:
            choice = int(input(colorama.Style.RESET_ALL + 'Enter your number: '))
            if choice == rand_num:
                print(colorama.Fore.LIGHTCYAN_EX + f'Try {tries}. ' + colorama.Style.BRIGHT + 'YOU ARE WINNER!!!')
                break
            elif choice < rand_num:
                print(colorama.Fore.YELLOW + f'Try {tries}. Your number is less. Try again!')
            elif choice > rand_num:
                print(colorama.Fore.YELLOW + f'Try {tries}. Your number is higher. Try again!')

            tries -= 1
        except ValueError:
            print(colorama.Fore.RED + 'You must enter a number!!!')
    if tries == 0:
        print(colorama.Fore.RED + colorama.Style.BRIGHT + 'You louse!')


if __name__ == '__main__':
    randomNumber()
