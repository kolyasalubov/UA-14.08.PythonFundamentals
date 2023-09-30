# *****   1 task    *****

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

# *****   2 task    *****

import math


def distance(x1, y1, x2, y2):
    # Calculate the difference in x and y coordinates
    dx = x2 - x1
    dy = y2 - y1

    # Calculate the square of the differences
    dx_squared = dx ** 2
    dy_squared = dy ** 2

    # Calculate the sum of the squared differences
    sum_squared = dx_squared + dy_squared

    # Calculate the square root of the sum to get the distance
    dist = math.sqrt(sum_squared)

    # Round the distance to two decimal places
    return round(dist, 2)

# *****   3 task    *****

def filter_words(st):
    # Split the input string into words
    words = st.split()

    # Capitalize the first word and convert the rest to lowercase
    words[0] = words[0].capitalize()
    for i in range(1, len(words)):
        words[i] = words[i].lower()

    # Join the words back together with a single space between them
    result = ' '.join(words)

# *****   4 task    *****

def number_to_string(num):
    return "{}".format(num)

# *****   5 task    *****

def reverse(st):
    # Split the input string into words using whitespace as the delimiter
    words = st.split()

    # Reverse the order of the words
    reversed_words = words[::-1]

    # Join the reversed words back together with a single space between them
    reversed_string = " ".join(reversed_words)

    return reversed_string

# *****   6 task    *****

def reverse_list(l):
    # Use list slicing to reverse the list
    reversed_l = l[::-1]

    return reversed_l

# *****   7 task    *****

def solution(number):
    if number < 0:
        return 0

    total_sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i

    return total_sum

# *****   8 task    *****

def zero_fuel(distance_to_pump, mpg, fuel_left):
    # Calculate the maximum distance the car can travel with the remaining fuel
    max_distance = mpg * fuel_left

    # Check if the maximum distance is greater than or equal to the distance to the pump
    if max_distance >= distance_to_pump:
        return True
    else:
        return False

# *****   9 task    *****

def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

# *****   10 task    *****

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# *****   11 task    *****

def count_sheeps(sheep):
    count = 0
    for is_present in sheep:
        if is_present:
            count += 1
    return count

# *****   12 task    *****

def correct_tail(body, tail):
    # Extract the last character from the body and compare it to the tail
    last_character_of_body = body[-1]
    return last_character_of_body == tail