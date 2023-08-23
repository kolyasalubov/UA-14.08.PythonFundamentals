number_1 = int(input('Enter the first number: '))
your_action = input('What do you want to do?')
number_2 = int(input('Enter the second number: '))

if your_action == '+':
    print(f'Result: {number_1 + number_2}')

elif your_action == '-':
    print(f'Result: {number_1 - number_2}')

elif your_action == '/':
    print(f'Result: {number_1 / number_2}')

elif your_action == '*':
    print(f'Result: {number_1 * number_2}')

elif your_action == '//':
    print(f'Result: {number_1 // number_2}')

elif your_action == '**':
    print(f'Result: {number_1 ** number_2}')

elif your_action == '%':
    print(f'Result: {number_1 % number_2}')

else:
    print('ERROR!!!')
    


