import random


def float_check(number: str) -> float:
    """
    Check if arg cannot be float, asked input aghain
    :param number: str
    :return: float arg
    """
    while True:
        try:
            number = float(number)
            break
        except ValueError:
            print("Invalid input. Please enter a float.")
            number = input("Enter again:")
    return number


def random_choise():
    """
    Main function
    Returns:

    """
    random_number = random.randint(0, 100)
    clien_number = float_check(input("Enter your number:"))
    tries = 1
    while True:
        if tries >= 10:
            print(f"You used {tries} tries.\nYOU ARE LOSE!")
            break
        elif clien_number == random_number:
            print(f"Your number {int(clien_number)} is the same as {random_number}\nYou used {tries} tries.\nYOU ARE WIN!")
            break
        elif clien_number > random_number:
            print("Try a lover \u2b07 number.")
            tries += 1
            clien_number = float_check(input("Enter your number:"))
        else:
            print("Try a LARGE \u2B06 number.")
            tries += 1
            clien_number = float_check(input("Enter your number:"))


def main():
    random_choise()


if __name__ == '__main__':
    main()
