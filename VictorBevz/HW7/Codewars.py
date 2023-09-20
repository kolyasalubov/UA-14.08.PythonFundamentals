# #Johnny's secret
# def greeting(name):
#     if name == "Johnny":
#         return"Hello, sugar."
#     else:
#         return "Hello {name}".format(name=name)

# #No yelling!

# def filter(string):
#     words = string.split()
#     if words:
#         capitalized = [words[0].capitalize()] + [word.lower() for word in words[1:]]
#         return ' '.join(capitalized)
#     else:
#         return string
    
    
# #Convert a Number to a String!

# def num_str(number):
#     return str(number)


# # Reversing Words in a String
# def reversing_words(string):
#     phrase = string.split()
#     phrase.reverse()
#     return ' '.join(phrase)

# #Reverse List Order
# def reverse_orger(lst1):
#     return lst1[::-1]


# # Multiples of 3 or 5
# def multiples(num):
#     if num < 0:
#         return 0

#     sum = 0
#     for number in range(num):
#         if number % 3 == 0 or number % 5 == 0:
#             sum += number
#     return sum

# #Will you make it?
# def fuel(amount):
#     if amount < 2:
#         return False
#     else:
#         return True

# # Are You Playing Banjo?

# def banjo(name):
#     if name and (name[0] == "R" or name[0] == "r"):
#         return name + " plays banjo"
#     else:
#         return name + " does not play banjo"

# # Convert boolean values to strings 'Yes' or 'No'.

# def bool(boolean):
#     if boolean:
#         return "Yes"  
#     else:
#         return "No"

# # Is this my tail?

# def my_tail(body, tail):
#     return body[-1] == tail

