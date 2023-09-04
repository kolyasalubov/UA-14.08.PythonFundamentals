range_list = [item for item in range(1, 11)]
print(range_list)

even_list = [item for item in range(1, 11) if item % 2 == 0]
print(even_list)

odd_list = [item for item in range(1, 10, 2) if item % 3 ==0]
print(odd_list)

interesting_list = [item for item in range(1, 11) if item % 2 != 0 if item % 3 != 0]
print(interesting_list)
