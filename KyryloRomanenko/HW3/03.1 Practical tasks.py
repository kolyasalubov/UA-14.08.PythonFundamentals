# # first task
# line_from_zen = input('Enter line from "Zen of Pyiton":\n').lower()

# count_better = 0
# count_never = 0
# count_is = 0

# for i in line_from_zen.split():
#     if i == 'better':
#         count_better += 1
#     elif i == 'never':
#         count_never += 1
#     elif i == 'is':
#         count_is += 1
#     else:
#         pass

# print(f'\nNumber "better" in a row: {count_better}')
# print(f'Number "never" in a row: {count_never}')
# print(f'Number "is" in a row: {count_is}')


# line_from_zen_upper = line_from_zen.upper()
# print(f'\nLine in Uppercase: {line_from_zen_upper}')

# line_from_zen_replase = line_from_zen.replace('i', '&')
# print(f'\nline with replase letter "i": {line_from_zen_replase}\n')

# # second task
# number = input('Enter your number:\n')
# product = 0

# for i in number:
#     product += int(i)

# print(f'Your product of the digit of number: {product}\n')

# print(f'Your reversed number: {number[::-1]}\n')

# print(f"Your sorted number: {''.join(sorted(number))}\n")

# Third task
a = 'a'
b = 'b'

a, b = b, a

print(f'a = {a}')
print(f'b = {b}')