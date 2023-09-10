import math


# Task1
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"


print(greet('Johnny'))


# Task2
def distance(x1, y1, x2, y2):
    res = math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
    return round(res, 2)


print(distance(1, 1, 0, 0))


# Task3
def filter_words(st: str):
    low_st = st.capitalize().lower().split()
    return ' '.join(low_st)


print(filter_words('  HELLO         woRlD!'), 'Hello world!')


# Task4
def number_to_string(num):
    return str(num)


# Task5
def reverse(st: str):
    sp_st = st.split()
    sp_st[0], sp_st[-1] = sp_st[-1], sp_st[0]
    res = ' '.join(sp_st)
    return res


print(reverse('Hello    World'))


# Task6
def reverse_list(l):
    res = list(reversed(l))
    return res


print(reverse_list([3, 6, 9]))


# Task7
def solution(number):
    if number < 0:
        return 0

    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return int(sum)


print(solution(10))


# Task8
def zero_fuel(distance_to_pump, mpg, fuel_left):
    fuel = mpg * fuel_left
    if fuel >= distance_to_pump:
        return True
    else:
        return False


# Task9
def are_you_playing_banjo(name: str):
    nname = name.lower()

    if nname[0] == 'r':
        return f'{name} plays banjo'
    else:
        return f'{name} does not play banjo'


print(are_you_playing_banjo('Martin'))


# Task10
def bool_to_word(boolean):
    if boolean:
        return 'Yes'
    elif not boolean:
        return 'No'


# Task11
def count_sheeps(sheep):
    res = 0
    for i in sheep:
        if i:
            res += 1
    return res


print(count_sheeps([True, True, True, False,
                    True, True, True, True,
                    True, False, True, False,
                    True, False, False, True,
                    True, True, True, True,
                    False, False, True, True]))


# Task12
def correct_tail(body, tail):
    if tail[0] == body[-1]:
        return True
    else:
        return False


print(correct_tail('Fox', 'x'))
