# task1 (Jenny's secret message)
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return f"Hello, {name}!"


print(greet("Johnny"))

# task2 (Find The Distance Between Two Points)
from math import sqrt


def distance(x1, y1, x2, y2):
    return round(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)


print(distance(1, 1, 0, 0))


# task3 No yelling!
def filter_words(st):
    new_string = ""
    second_space = ""
    counter = 0
    st = st.lower().strip()
    for n in st:
        if counter == 0:
            new_string += n.upper()
        else:
            if n == " " and n != second_space:
                second_space = n
                new_string += n
            elif n == second_space:
                pass
            else:
                new_string += n
                second_space = ""
        counter += 1
    return new_string


print(filter_words('This    will    noT    pass'))


# task4 Convert a Number to a String
def number_to_string(num):
    return str(num)


print(number_to_string(1 - 2), '-1')


# task5 Reversing Words in a String

def reverse(st):
    a = st.split()
    a.reverse()
    st = " ".join(a)
    return st


print(reverse('Hi There.'))


# task6 Reverse List Order
def reverse_list(l):
    l.reverse()
    return l


print(reverse_list([1, 2, 3, 4]))


# task7 Multiples of 3 or 5

def solution(number):
    number -= 1
    counter = 0
    if number < 0:
        return 0
    else:
        while number > 0:
            if number % 3 == 0 or number % 5 == 0:
                counter += number
            number -= 1
        return counter


print(solution(6))


# task8 Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump / mpg == fuel_left:
        return True
    else:
        return False


print(zero_fuel(50, 25, 2))


# task9 Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


print((are_you_playing_banjo("martin")))


# task10 Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"


print((bool_to_word(True)))


# task11 Counting sheep
def count_sheeps(sheep):
    result = 0
    for n in sheep:
        if n:
            result += 1
    return result


array1 = [True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True]

print(count_sheeps(array1))


# task12 Is this my tail?
def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    else:
        return False


print(correct_tail("Fox", "x"))
