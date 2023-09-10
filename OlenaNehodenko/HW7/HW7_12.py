#First task
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {0}!".format(name)
#Second task
from math import sqrt
def distance(x1, y1, x2, y2):
    return round(sqrt((x2-x1)**2+(y2-y1)**2),2)
#Third task
def filter_words(st):
    return ' '.join(st.capitalize().split())
#Fourth task
def number_to_string(num):
    return str(num)
#Fifth task
def reverse(st):
    return ' '.join(reversed(st.split()))
#Sixth task
def reverse_list(l):
    return l[::-1]
#Seventh task
def solution(number):
  if number < 0:
     return 0
  total = 0
  for i in range(number):
    if i % 3 == 0 or i % 5 == 0:
      total += i
  return total
#Eighth task
def zero_fuel(distance_to_pump, mpg, fuel_left):
   average_miles = 25
   max_distance = fuel_left * average_miles
   return distance_to_pump <= max_distance
#Ninth task
def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'
#Tenth task
def bool_to_word(boolean):
     if boolean:
        return "Yes"
     else:
      return "No"
#Eleven task
def count_sheeps(sheep):
  return sheep.count(True)
#Twelfth task
def correct_tail(body, tail):
    return body[-1] == tail




