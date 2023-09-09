list_quantity = input("Please enternumber number of digits for changing: ")

if not list_quantity.isdecimal():
    print("Error: You have enter not a number!")
    exit()

list_of_int = list(range(int(list_quantity)))

list_of_float = []
for i in list_of_int:
    list_of_float.append(float(i))

print("List of integer:", list_of_int)
print("List of float:\t", list_of_float)