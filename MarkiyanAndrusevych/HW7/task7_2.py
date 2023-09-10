# #task1
# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     else:
#         return "Hello, {name}!".format(name=name)

# #task2
# import math
# def distance(x1, y1, x2, y2):
#     a = float(x2 - x1)
#     b = float(y2 - y1)
#     d = float(a * a + b * b)
#     result = math.sqrt(d)
#     return round(result, 2)

# #task3
# def filter_words(input_str):
#     words = input_str.split()
#     if words:
#         words[0] = words[0].capitalize()
#     result_str = ' '.join(words)
#
#     return result_str

# #task4
# def number_to_string(num):
#     return str(num)

# #task5
# def reverse(st):
#     words = st.split()
#     reversed_st = ' '.join(reversed(words))
#
#     return reversed_st

# #task6
# def reverse_list(l):
#     reversed_list = l[::-1]
#     return reversed_list

# #task7
# def solution(number):
#     if number < 0:
#         return 0
#
#     total_sum = 0
#
#     for i in range(1, number):
#         if i % 3 == 0 or i % 5 == 0:
#             total_sum += i
#
#     return total_sum

# #task8
# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if distance_to_pump / mpg <= fuel_left:
#         return True
#     else:
#         return False

# #task9
# def are_you_playing_banjo(name):
#     if name[0].lower() == 'r':
#         return name + " plays banjo"
#     else:
#         return name + " does not play banjo"

# #task10
# def bool_to_word(boolean):
#     if boolean == True:
#         return "Yes"
#     else:
#         return "No"

# #task11
# def count_sheeps(sheep):
#     return sheep.count(True)

# #task12
# def correct_tail(body, tail):
#     sub = body[-len(tail):]
#     if sub == tail:
#         return True
#     else:
#         return False







