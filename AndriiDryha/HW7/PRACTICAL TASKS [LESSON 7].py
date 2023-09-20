# # Task 1

# def largest_number(n, m):
        
#         """This function returns largest number of two numbers"""
        
#         if n > m:
#             return n
#         else:
#             return m
        
# result = largest_number(int(input("Enter first number \n")), int(input("Enter second number \n")))

# print("The largest number of two entered numbers:", result)


# # Task 2

# Choice = input("Write the area of which figure you want to calculate: 'rectangle', 'triangle' or 'circle' \n")

# while True:

#     if Choice == "rectangle":
#         import Rectangle
#         print(Rectangle.rectangle_area)
#         break
#     if Choice == "triangle":
#         import Triangle
#         print(Triangle.triangle_area)
#         break
#     if Choice == "circle":
#         import Circle
#         print(Circle.circle_area)
#         break

# Task 3

def number_character(word):

    symbols = list(set(list(word)))
    number = -1
    even_numbers = []

    while True:
        if number < len(symbols):
            number = number + 1
            symbol_number = symbols[number] # number of the unique symbol in random order
            count = word.count(symbol_number) # count of the unique symbol in the entered string
            even_numbers.append(count)
        if len(even_numbers) == len(symbols):
            res = dict(map(lambda i,j : (i,j) , symbols,even_numbers))
            return res
    
word = number_character(str(input("Enter everything \n")))

print ("Count of the unique symbols in your input: " + str(word))

