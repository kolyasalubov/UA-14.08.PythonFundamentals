
# 05.1 PRACTICAL TASKS / [GITHUB]

#Task2
user_number = int(input('\nPlease enter an integer: '))
print(f'\nPrinting the Fibonacci sequence: ')
value_one  = 0
value_two = 1
fibonacci_number = 0
print(f'\t\t/{value_one}/')

while True:
    fibonacci_number = ((value_one*2)+(value_two*2))/2
    if fibonacci_number >= user_number or user_number < 0:
        break
    fibonacci_number = int(fibonacci_number)
    print(f'\t\t/{fibonacci_number}/')
    value_two, value_one = value_one, fibonacci_number
    
    
