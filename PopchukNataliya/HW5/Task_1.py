# # change list of integer to list of float
integer_list = [1, 2, 3, 4, 5, 6]
float_list = []

for var in integer_list:
    float_var = float(var)
    float_list.append(float_var)

print("Converted Float List:", float_list)

