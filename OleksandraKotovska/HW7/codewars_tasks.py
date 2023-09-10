###############################
# 1. Jenny's secret message

def greet(name):
    
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)
    
print(greet("Li"))


###############################################
# 2. Find The Distance Between Two Points

# def distance(x1, y1, x2, y2):
#     if x1 > x2:
#         x = x1 - x2
#     else:
#         x = x2 - x1
#     if y1 > y2:
#         y = y1 - y2
#     else:
#         y = y2 - y1
#     d = (x ** 2 + y ** 2) ** 0.5
#     return round(d, 2)

# print(distance(2, 3, 5, 6))


########################
# 3. No yelling!

# def filter_words(st):
#     a = st.split()
#     b = " ".join(a)
#     c = b.capitalize()
    
#     return c

# print(filter_words('HELLO   CAN YOU     HEAR ME'))


#####################################
# 4. Convert a Number to a String

# def number_to_string(num):
#     my_string = str(num)
#     # print(type(my_string))
#     return my_string

# print(number_to_string(10.2))


####################################
# 5. Reversing Words in a String

# def reverse(st):
#     str_list = st.split()[::-1]
#     return " ".join(str_list)

# print(reverse('Reversing Words in a String'))


##############################
# 6. Reverse List Order

# def reverse_list(l):
#     for i in l:
#         return l[::-1]

# my_list = ['Reverse', 'List', 'Order']
# print(reverse_list(my_list))


###############################
# 7. Multiples of 3 or 5

# def solution(number):
#     a = []
#     if number < 0:
#         return 0
#     else: 
#         for i in range(number):
#             if i % 3 == 0:
#                 a.append(i)
#             elif i % 5 == 0:
#                 a.append(i)
        
#     return sum(a)

# print(solution(10))


###############################
# 8.  Will you make it?

# def zero_fuel(distance_to_pump, mpg, fuel_left):

#     if distance_to_pump > mpg * fuel_left:
#         return False
#     else:
#         return True

# print(zero_fuel(50, 25, 2))


#################################
# 9. Are You Playing Banjo?

# def are_you_playing_banjo(name):

#     if name.lower()[0] == 'r':
#         return name + " plays banjo" 
#     else:
#         return name + " does not play banjo"

# print(are_you_playing_banjo('roman'))


##########################################################
# 10.  Convert boolean values to strings 'Yes' or 'No’

# def bool_to_word(boolean):
#     if boolean == True:
#         return "Yes"
#     else:
#         return "No"

# print(bool_to_word(False))


###########################
# 11.Counting sheep

# def count_sheeps(sheep):
#     count = 0
#     for i in sheep:
#         if i == True:
#             count += 1
#     return count

# l = [True, False, False, True, False, False]
# print(count_sheeps(l))


# 12.Is this my tail?

# def correct_tail(body, tail):
#     if body[-1] == tail:
#         return True
#     else:
#         return False
    
# print(correct_tail('cat', 't'))

