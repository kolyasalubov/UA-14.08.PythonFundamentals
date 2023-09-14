def max_number(first_number: int, second_number: int) -> int:
    """
    compares numbers

    :param first_number: int number
    :param second_number: int number
    :return: max number betwen a and b
    """

    if first_number > second_number:
        return first_number
    else:
        return second_number


print('*** Compare two numbers ***')

first_input_number = int(input('\nEnter first number:\n'))
second_input_number = int(input('Enter second number:\n'))

print(f'\nThe maximum number:{max_number(first_input_number, second_input_number)}')
