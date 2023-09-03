list_of_number = []
float_list_of_number = []
lenght_of_list = int(input('Enter lenght of the list: '))

for i in range(lenght_of_list):
    elements = int(input('Enter the items: '))
    list_of_number.append(elements)


for i in range(len(list_of_number)):
    new_float_number = float(list_of_number[i])
    float_list_of_number.append(new_float_number)

print(f'integer list: {list_of_number},\n'
      f'float list: {float_list_of_number}')



