# # 1. Jenny's secret message

# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     return "Hello, {name}!".format(name=name)
# ==========================================
# # Find The Distance Between Two Points

# 2. def distance(x1, y1, x2, y2):
#     delta_x = x1 - x2
#     delta_y = y1 - y2
    
#     distance = delta_x ** 2 + delta_y ** 2
#     dist_sqrd = (distance) ** 0.5
    
#     return round(dist_sqrd, 2)
# # ============================================
# # 3. No yelling!

# def filter_words(st):
#     words = st.split()

#     result = ' '.join([words[0].capitalize()] + [word.lower() for word in words[1:]])

#     return result
# ============================================
# # 4. Convert a Number to a String

# def number_to_string(num):
#     str_num = str(num)
#     return str_num
# ==========================================
# # 5. Reversing Words in a String

# def reverse(st):
#     words = st.split()
    
#     words = [word for word in words if word.strip()]
    
#     reversed_words = words[::-1]
    
#     result = ' '.join(reversed_words)
    
#     return result
# ==============================================
# # 6. Reverse List Order

# def reverse_list(l):
#     'return a list with the reverse order of l'
#     reversed_l = l[::-1]
#     return reversed_l
# =========================================
# # 7.Multiples of 3 or 5

# def solution(number):
    
#     if number < 0:
#         return 0
    
#     sum_multiples = 0
    
#     for i in range(1, number):
#         if i % 3 == 0 or i % 5 == 0:
#             sum_multiples += i
            
#     return sum_multiples
# ==========================================
# # 8. Will you make it?

# def zero_fuel(distance_to_pump, mpg, fuel_left):
    
#     max_distance = mpg * fuel_left
    
#     if distance_to_pump <= max_distance:
#         return True
#     else:
#         return False
# ===========================================
# # 9. Are You Playing Banjo?

# def are_you_playing_banjo(name):
    
#     if name[0] == "R" or name[0] == "r":
#         return name + " plays banjo" 
#     else:
#         return name + " does not play banjo"
#     return name
# ==============================================
# # 10. Convert boolean values to strings 'Yes' or 'No’

# def bool_to_word(boolean):
#     if boolean == True:
#         return "Yes"
#     else:
#         return "No"
#     return boolean
# ==============================
# # 11. Counting sheep

# def count_sheeps(sheep):
#     count = 0
    
#     for is_present in sheep:
#         if is_present:
#             count += 1
#     return count
# =================================
# # 12.Is this my tail?

# def correct_tail(body, tail):
#     last_char_of_body = body[-1]
    
#     if last_char_of_body == tail:
#         return True
#     else:
#         return False







