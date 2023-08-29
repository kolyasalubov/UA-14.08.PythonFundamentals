import math

# the first part
while True:
    number = input('enter your number:')
    if len(number) != 4 or not number.isdigit():
        print('Enter four-digit number!!!!!!!')
    else:
        break
number = list(number)
int_number_list = []

for i in number:
    int_number_list.append(int(i))

resoult = math.prod(int_number_list)
print(resoult)
print('------------')

# the second part
print(list(reversed(number)))
print('------------')

# the third part
print(sorted(int_number_list))
