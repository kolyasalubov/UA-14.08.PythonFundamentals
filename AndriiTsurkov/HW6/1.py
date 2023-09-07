#1
# even number than are divisible on 2
# odd numbers, which by divisible on 3
# numbers that are not divisible by 2 and 3

divisible_on_2 = []
divisible_on_3 = []
not_divisible_by_2_and_3 = []
list_of_numbers = []

for i in range (1, 11):
    list_of_numbers.append(i)
    
    if i % 2 == 0:
        divisible_on_2.append(i)
    elif i % 3 == 0:
        divisible_on_3.append(i)
    else:
        not_divisible_by_2_and_3.append(i)

print ('List of all nubers in range(1, 10):', list_of_numbers)
print ('Number than are divisible on 2:', divisible_on_2)
print ('Number than are divisible on 3:', divisible_on_3)
print ('Numbers that are not divisible by 2 and 3:', not_divisible_by_2_and_3)