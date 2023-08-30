# Task 1
zen_line = input('Enter line:\n').lower()

count_better = 0
count_never = 0
count_is = 0

for i in zen_line.split():
    if i == 'better':
        count_better += 1
    elif i == 'never':
        count_never += 1
    elif i == 'is':
        count_is += 1
    else:
        pass

print(f'\nNumber "better" in a row: {count_better}')
print(f'Number "never" in a row: {count_never}')
print(f'Number "is" in a row: {count_is}')


zen_line_upper = zen_line.upper()
print(f'\nLine in Uppercase: {zen_line_upper}')

zen_line_replase = zen_line.replace('i', '&')
print(f'\nline with replase letter "i": {zen_line_replase}\n')

# Task 2

natural_number = 1208

number_0 = list(str(natural_number))
num_list = list(number_0)
num_list.reverse()
num_2 = ''.join(num_list)
print(f'Revers num is: {num_2}')

a = int(number_0[0])
b = int(number_0[1])
c = int(number_0[2])
d = int(number_0[3])

print(f'All: {a, b ,c ,d}')

#Task 3

number_0.sort()
print(number_0)

