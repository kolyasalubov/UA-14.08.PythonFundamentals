# Програма що перевіряє надійснійсть паролю
import re
def check_password(password):
    """Ця функція перевіре пароль на дані умови"""
    if len(password) < 6 or len(password) > 16:
        return False
    elif not re.search(r'[$#@]', password):
        return False
    elif not re.search(r'\d', password):
        return False
    elif not re.search(r'[A-Za-z]', password):
        return False
    else:
        return True

def main():
    """Якщо пароль не правильний попросе ввести його ще раз, якщо вірний то виведе "Чудово! Ваш пароль вірний та захищенний" """
    while True:
        password = input("Введіть пароль: ")
        if check_password(password):
            print("Чудово! Ваш пароль вірний та захищенний")
            break
        else:
            print("Пароль не вірний, будь ласка повторіть спробу: ")

if __name__ == "__main__":
    main()