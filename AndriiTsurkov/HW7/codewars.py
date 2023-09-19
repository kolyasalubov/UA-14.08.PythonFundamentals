# Jenny's secret message
# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     else:
#         return "Hello, {name}!".format(name=name)
# greet(Johnny)

# Find The Distance Between Two Points
# def distance(x1, y1, x2, y2):
#     from math import sqrt
#     distance = sqrt (((x2 - x1) ** 2) + ((y2 - y1) **2))
#     return round(distance, 2) 
# print(distance(1, 1, 0, 0))

# No yelling!
# Write a function taking in a string like WOW this is REALLY          amazing and returning Wow this is really amazing.
# String should be capitalized and properly spaced. Using re and string is not allowed.
# def filter_words(st):
#     st = st.capitalize()
#     st = st.split()
#     st = ' '.join(st)
#     return st
# print(filter_words("HELLO CAN YOU HEAR     ME"))

# Convert a Number to a String
# We need a function that can transform a number (integer) into a string.
# def number_to_string(num):
#     num = str(num)
#     return num
# print(number_to_string(456))

# Reversing Words in a String
# def reverse(st):
#     st = st.split()
#     st.reverse()
#     st = ' '.join(st)
#     return st
# print(reverse("Hello World"))

# Reverse List Order
# def reverse_list(l):
#     return l[::-1]
# print(reverse_list([0,1,2,3,4,5]))

# Multiples of 3 or 5
# def solution(number):
#     if number < 0:
#         return 0
#     sum = 0
#     for i in range(1, number):
#         if i % 3 == 0 and i % 5 == 0:
#             sum += i
#         elif i % 3 == 0 or i % 5 == 0:
#             sum += i
#     return sum
# print(solution(10))

# Will you make it?
# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     pass
#     can_miles = fuel_left * mpg
#     return distance_to_pump <= can_miles
# print(zero_fuel(85, 25, 4))

# Are You Playing Banjo?
# def are_you_playing_banjo(name):
#     return (name + " plays banjo" if name[0] == "R" or name[0] == "r" else name + " does not play banjo")
# print(are_you_playing_banjo("Rikke"))

# Convert boolean values to strings 'Yes' or 'No’
# def bool_to_word(boolean):
#     return "Yes" if boolean else "No"
# print(bool_to_word(False))

# Counting sheep
# def count_sheeps(sheep):
#     count = 0
#     for i in sheep:
#         if i:
#             count += 1
#     return count

# array1 = [True,  True,  True,  False,
#             True,  True,  True,  True ,
#             True,  False, True,  False,
#             True,  False, False, True ,
#             True,  True,  True,  True ,
#             False, False, True,  True]
# print(count_sheeps(array1))

# Is this my tail?
# def correct_tail(body, tail):
#     return True if body[-1] == tail else False
# print(correct_tail("Fox", "x"))
