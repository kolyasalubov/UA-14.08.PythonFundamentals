while True:
    login = input('Enter your login:\n')

    if login.lower() == 'first':
        print(f'Your login {login} accept!')
        break
    else:
        print(f'Your login {login} uncorrect. Try again.')

print('Welcom to our club!')
