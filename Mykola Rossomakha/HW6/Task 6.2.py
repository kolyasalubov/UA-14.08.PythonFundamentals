login = 'First'

while True:
    user_login = input('Будь ласка, введіть ваш логін: ')

    if user_login == login:
        print('Ласкаво просимо,', user_login)
        break
    else:
        print('Помилка. Будь ласка, спробуйте ще раз.')