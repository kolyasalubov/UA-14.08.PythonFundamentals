number = int(input('Enter the number: '))
item = 0
factorial = 1
while item < number:
    item += 1
    factorial *= item
print(f'{number}! = {factorial}')

