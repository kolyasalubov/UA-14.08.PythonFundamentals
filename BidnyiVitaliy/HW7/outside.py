# 1 Jenny's secret message

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
    	return "Hello, {name}!".format(name=name)

# Find The Distance Between Two Points

def distance(x1, y1, x2, y2):
     if x1 > x2:
         x = x1 - x2
     else:
          x = x2 - x1
     if y1 > y2:
          y = y1 - y2
     else:
          y = y2 - y1
     d = (x ** 2 + y ** 2) ** 0.5
     return round(d, 2)

print(distance(2, 3, 5, 6))

# 3 No yelling!

def filter_words(st):
    return " ".join(st.split()).capitalize()

# 4 Convert a Number to a String
def number_to_string(num):
    try:
        return str(num)
    except:
        return None

# 5 Reversing Words in a String

def reverse(st):
    return " ".join(reversed(st.split())).strip()

# 6 Reverse List Order

def reverse_list(l):
  l.reverse()
  return l

# 7 Multiples of 3 or 5

def solution(number):
    sum = 0
    for i in range(number):
        if (i % 3) == 0 or (i % 5) == 0:
            sum += i
    return sum

# 8 Will you make it?

def zeroFuel(distance_to_pump, mpg, fuel_left):
    return mpg*fuel_left >= distance_to_pump

# 9 Are You Playing Banjo?

def areYouPlayingBanjo(name):
    return name + (' plays' if name[0].lower() == 'r' else ' does not play') + " banjo";

# 10 Convert boolean values to strings 'Yes' or 'No’

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# 11 Counting sheep

def count_sheeps(array_of_sheep):
  # TODO May the force be with you
  count = 0
  for sheep in array_of_sheep:
      if sheep:
          count += 1 
  return count

# 12 Is this my tail?

def correct_tail(body, tail):
    return body[-1] == tail