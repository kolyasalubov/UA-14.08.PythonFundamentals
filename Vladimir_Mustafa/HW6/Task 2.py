#Task 2

while True:
    user_login = input('Enter your login: ')

    if user_login == 'First':
        print(f'Hi, {user_login}!')
        break
    else:
        print('Error! Try again.')
