# 1. Jenny's secret message
# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     else:
#         return f"Hello, {name}!"

# 2. Find The Distance Between Two Points
# import math
# def distance(x1, y1, x2, y2):
#     result = math.sqrt((x2-x1) ** 2 +(y2-y1)**2)
#     return round(result, 2)

# 3. No yelling!
# def filter_words(st):
#     split_words = st.split()
#     filtered = " ".join(split_words)
#     result = filtered.capitalize()
#     return result
# 4. Convert a Number to a String!
# def number_to_string(num):
#     return str(num)
#
# 5. Reversing Words in a String
# def reverse(st):
#     s = st.split()[::-1]
#     return " ".join(s)
# 6. Reverse List Order
# def reverse_list(l):
#     return l[::-1]

# 7. Multiples of 3 or 5
# def solution(number):
#     count = []
#     if number < 0:
#         return 0
#     else:
#         for i in range(0, number):
#             if i % 3 == 0:
#                 count.append(i)
#             elif i % 5 == 0:
#                 count.append(i)
#     return sum(count)

# 8. Will you make it?
# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if distance_to_pump > mpg * fuel_left:
#         return False
#     else:
#         return True
# 9. Are You Playing Banjo?
# def are_you_playing_banjo(name):
#     if name[0] == 'r' or name[0] == 'R':
#         return name + " plays banjo"
#     else:
#         return name + " does not play banjo"
# 10. Convert boolean values to strings 'Yes' or 'No'.
# def bool_to_word(boolean):
#     return "No" if boolean == 0 else "Yes"
# 11. Counting sheep...
# def count_sheeps(sheep):
#     list1 = []
#     for i in sheep:
#         if i is True:
#             list1.append(i)
#             i += 1
#     return len(list1)
# 12. Is this my tail?
# def correct_tail(body, tail):
#     if body[-1] == tail:
#         return True
#     else:
#         return False
