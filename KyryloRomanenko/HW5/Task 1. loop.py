item = 0
even_list = []
odd_list = []

while item < 100:
    if item % 2 == 0:
        even_list.append(item)
    else:
        odd_list.append(item)
    item += 1

print(f'int list: {even_list}')

float_even_list = []

for item in even_list:
    float_even_list.append(float(item))

print(f'float list: {float_even_list}')
