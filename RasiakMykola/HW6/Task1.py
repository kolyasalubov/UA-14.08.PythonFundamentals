
# 06.1 PRACTICAL TASKS / [GITHUB]

# Task_1
list_integer = list(range(1, 11))

list_even_numbers_2 = [x for x in list_integer if x%2 == 0]
list_odd_numbers_3 = [x for x in list_integer if x%3 == 0]
list_odd_numbers = [x for x in list_integer if  x%3 != 0 and x%2 != 0]

print(f'\nEven numbers{list_even_numbers_2} that are ÷ 2,',\
      f'\nOdd numbers{list_odd_numbers_3} that are ÷ 3,',\
      f'\nNumbers{list_odd_numbers}, which are not ÷ 2 and ÷ 3') 
