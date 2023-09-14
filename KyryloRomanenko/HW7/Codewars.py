# 1. Jenny's secret message

def greet(name):
    if name == 'Johnny':
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"


# 2. Find The Distance Between Two Points

def distance(x1, y1, x2, y2):
    return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)


# 3. No yelling!

def filter_words(st):
    cap_str = st.capitalize()
    words = cap_str.split(" ")
    result_list = []
    for i in words:
        if i != "":
            result_list.append(i)
    return " ".join(result_list)


# 4. Convert a Number to a String!


def number_to_string(num):
    return str(num)


# 5. Reversing Words in a String

def reverse(st):
    words = st.split()
    reversed_words = list(reversed(words))
    reversed_string = " ".join(reversed_words)
    return reversed_string


# 6. Reverse List Order

def reverse_list(l):
    return l[::-1]


# 7. Multiples of 3 or 5


def solution(number):
    result = 0
    for i in range(number):
        if i % 3 == 0:
            result += i
        elif i % 5 == 0:
            result += i
    return result


# 8. Will you make it?


def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump / mpg <= fuel_left:
        return True
    else:
        return False


# 9. Are You Playing Banjo?


def are_you_playing_banjo(name):
    if name[0] in ('r', 'R'):
        return f'{name} plays banjo'
    else:
        return f'{name} does not play banjo'


# 10. Convert boolean values to strings 'Yes' or 'No'.

def bool_to_word(boolean):
    if boolean:
        return 'Yes'
    else:
        return 'No'


# 11. Counting sheep...


def count_sheeps(sheep):
    return sheep.count(True)


# 12. Is this my tail?


def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    else:
        return False
