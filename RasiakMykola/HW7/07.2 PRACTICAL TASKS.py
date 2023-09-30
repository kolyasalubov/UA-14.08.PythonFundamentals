
# 07.2 PRACTICAL TASKS / [GITHUB OUTSIDE FOR TOPIC 7]

#I. Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"    
    elif not name == "Johnny":
        return "Hello, {name}!".format(name=name)

    
print(greet("Johnny"))
print('#','-'*50)

#II. Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    # Your code here
    dx = x2 - x1
    dy = y2 - y1
    
    dist = (dx**2 + dy**2)**0.5
    
    rounded_distance = round(dist, 2)
    
    return rounded_distance


print(distance(1, 1, 4, 4))
print('#','-'*50)

#III. No yelling!
def filter_words(st):
    # Your code here.
    st = st.lower()
    st = st.capitalize()
    return st


print(filter_words("HELLO worLd!"))
print('#','-'*50)

#IV. Convert a Number to a String
def number_to_string(num):
    # Return a string of the number here!
    num = str(num)
    return num


print(number_to_string(456))
print('#','-'*50)

#V. Reversing Words in a String
def reverse(st):
    words = st.split()
    st = ' '.join(reversed(words))
    
    return st


print(reverse("Hello my friend"))
print('#','-'*50)

#VI. Reverse List Order
def reverse_list(l):
    reversed_l = l[::-1]
    return reversed_l


print(reverse_list([1, 2, 3, 4]))
print('#','-'*50)

#VII. Multiples of 3 or 5
def solution(number):
    actions = 0
    if number < 0 or number == 0:
        actions = 1
    elif number > 0:
        actions = 2
    match actions:
        case 1:
            return 0
        case 2:
            summ = 0
            for num in range(1, number):
                if num%3 == 0 or num%5 == 0:
                    summ = summ + num
            number = summ
            return number
        

print(solution(10))
print('#','-'*50)

#VIII. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
    max_distance = fuel_left * mpg
    
    if max_distance >= distance_to_pump:
        return True
    else:
        return False
    

print(zero_fuel(100, 25, 4))
print('#','-'*50)

#IX. Are You Playing Banjo?
def are_you_playing_banjo(name):
    # Implement me!
    if name[0] == 'R'or name[0] == 'r':
        name = name + " plays banjo" 
    else:
        name =  name + " does not play banjo"
        
    return name


print(are_you_playing_banjo('Rita'))
print(are_you_playing_banjo('Tom'))
print('#','-'*50)

#X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    # TODO
    return "Yes" if (boolean == True) else "No"


print(bool_to_word(5 > 6))
print('#','-'*50)

#XI. Counting sheep
def count_sheeps(sheep):
    # TODO May the force be with you
    
    count = 0
    i  = 0 
    while i < len(sheep):
        sheep[i]
        if sheep[i]:
            count += 1
        i += 1
    
    return count


print(count_sheeps([True, None, None, True, False, None, None, False, True, None, None, True, False ]))
print('#','-'*50)

#XII. Is this my tail?
def correct_tail(body, tail):
     return True if (body[-1] == tail[0]) else False

    
print(correct_tail("fox", "x"))
print('#','-'*50)




