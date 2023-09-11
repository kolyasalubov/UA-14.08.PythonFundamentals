#Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)

#No yelling!

def filter_words(st):
    words = st.split()
    if words:
        capitalized_words = [words[0].capitalize()] + [word.lower() for word in words[1:]]
        return ' '.join(capitalized_words)
    else:
        return st

# Convert a Number to a String!
def number_to_string(num):
    return str(num)

# Reversing Words in a String
def reverse(st):
    words = st.split()
    words.reverse()
    return ' '.join(words)

#  Reverse List Order
def reverse_list(l):
    return l[::-1]

# Multiples of 3 or 5
def solution(number):
    if number < 0:
        return 0

    total = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    return total

# Are You Playing Banjo?

def are_you_playing_banjo(name):
    if name and (name[0] == 'R' or name[0] == 'r'):
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

# Convert boolean values to strings 'Yes' or 'No'.

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# Is this my tail?

def correct_tail(body, tail):
    return body[-1] == tail



