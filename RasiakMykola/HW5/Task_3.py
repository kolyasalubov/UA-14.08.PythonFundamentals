
# 05.1 PRACTICAL TASKS / [GITHUB]

#Task3
user_number = int(input('\nPlease enter an integer : '))

if user_number == 0:
    print(f'\nYour factorial {user_number}!=1')
elif user_number < 0:
    print('Does not exist.')
else:
    print('\nPrint Factorial numbers:')
    print('0!=1')
    any_number = user_number - 1
    value = 1
    result = 0
    i = 1
    while i <= any_number:
        value = value * i
        print(f'{i}!={value}')
        i = i + 1
    result = user_number * value
    print('#'*68)
    print(f'\nYour factorial {user_number}!={result}')
