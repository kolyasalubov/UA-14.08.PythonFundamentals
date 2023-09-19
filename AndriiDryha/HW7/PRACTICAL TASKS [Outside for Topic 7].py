# Task 1

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

# Task 2

def distance(x1, y1, x2, y2):
    distance = ((x2-x1)**2+(y2-y1)**2)**0.5
    distance2 = round(distance , 2)
    return distance2

# Task 3

def filter_words(st):
    return st.capitalize()

# Task 4

def number_to_string(num):
    return str(num)

# Task 5

def reverse(st):
    words = st.split()
    words.reverse()
    st = ' '.join(words)
    return st

# Task 6

def reverse_list(l):
    l.reverse()
    return l

# Task 7

def solution(number):
    
    number_list = []

    for x in range(1, number):
        if number >= 0 and x % 3 == 0 or x % 5 == 0:
            number_list.append(x)
    return sum(number_list)

# Task 8

def zero_fuel(distance_to_pump, mpg, fuel_left):

    if distance_to_pump/fuel_left <= mpg:
        return True
    else:
        return False
    
# Task 9

def are_you_playing_banjo(name):
    
    if name[0] == "r" or name[0] == "R":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    
# Task 10

def bool_to_word(boolean):
    
    if boolean == True:
        return "Yes"
    else:
        return "No"
    
# Task 11

def count_sheeps(sheep):
    
    count = sheep.count(True)
    return count

# Task 12

def correct_tail(body, tail):
    
        if body[-1] == tail:
            return True
        else:
            return False



