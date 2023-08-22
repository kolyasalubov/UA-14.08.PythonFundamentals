# a = float(21)
# b = float(6)
# print('a + b =', a + b)
# print('a - b =', a - b)
# print('a * b =', a * b)
# print('a / b =', a / b)
# print('a ** b =', a ** b)
# print('a // b =', a // b)
# print('a % b =', a % b)
# number_a = float(input('Enter (A) number:'))
# number_b = float(input('Enter (B) number:'))
#
# print(f'{number_a} + {number_b} =', number_a + number_b)
# print(f'{number_a} - {number_b} =', number_a - number_b)
# print(f'{number_a} * {number_b} =', number_a * number_b)
# print(f'{number_a} / {number_b} =', number_a / number_b)
# print(f'{number_a} ** {number_b} =', number_a ** number_b)
# print(f'{number_a} % {number_b} =', number_a % number_b)
# print(f'{number_a} == {number_b} =', number_a == number_b)
#
# while
# number_a = input('Enter (A) number: ')
# number_b = input('Enter (B) number: ')
#  number_a = float(number_a)
#    number_b = float(number_b)
#     print(f'{number_a} + {number_b} =', number_a + number_b)
#     print(f'{number_a} - {number_b} =', number_a - number_b)
#     print(f'{number_a} * {number_b} =', number_a * number_b)
#     print(f'{number_a} / {number_b} =', number_a / number_b)
#     print(f'{number_a} ** {number_b} =', number_a ** number_b)
#     print(f'{number_a} % {number_b} =', number_a % number_b)
#     print(f'{number_a} == {number_b} =', number_a == number_b)
# else:
#     print("Invalid input. Please enter valid numbers.")
#
while True:
    number_a = input('Enter (A) number:')
    number_b = input('Enter (B) number:')

    try:
        number_a = float(number_a)
        number_b = float(number_b)

        if type(number_a) == float and type(number_b) == float:
            print(f'{number_a} + {number_b} =', number_a + number_b)
            print(f'{number_a} - {number_b} =', number_a - number_b)
            print(f'{number_a} * {number_b} =', number_a * number_b)
            print(f'{number_a} / {number_b} =', number_a / number_b)
            print(f'{number_a} ** {number_b} =', number_a ** number_b)
            print(f'{number_a} % {number_b} =', number_a % number_b)
            print(f'{number_a} == {number_b} =', number_a == number_b)
            break
        else:
            print("Invalid data type")

    except ValueError:
        print("Invalid data type")
        continue
