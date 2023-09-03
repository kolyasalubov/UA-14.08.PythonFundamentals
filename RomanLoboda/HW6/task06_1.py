original_list = [number for number in range(1, 10)]

even_list = []
odd_list_3 = []
not_divisible_2_3 = []

for n in original_list:
    if n % 2 == 0:
        even_list.append(n)
    elif n % 3 == 0:
        odd_list_3.append(n)
    else:
        not_divisible_2_3.append(n)

print("Original list : ",original_list)
print("Even number that are divisible by 2 : ", even_list)
print("Odd number, which are divisible by 3 : ", odd_list_3)
print("Numbers that are not divisible by 2 and 3 : ", not_divisible_2_3)
