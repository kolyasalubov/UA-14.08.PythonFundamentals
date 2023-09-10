# #task1
# def find_number(a, b):
#
#     if a > b:
#         return a
#     else:
#         return b
#
# num1 = 22
# num2 = 33
# result = find_number(num1, num2)
# print(f"Largest number between {num1} and {num2} is {result}")

# #task2
# def rectangle_area(a, b):
#     result = a*b
#     return result
#
#
# def triangle_area(a, b , c):
#     result = (a+b+c)/2
#     return result
#
# def circle_area(a):
#     result = a*a*3,14
#     return result
#
# print("Welcome to area calaculator :) \n Choose the figure: \n 1. Rectangle \n 2. Triangle \n 3. Circle")
# choice = int(input())
#
# if choice == 1:
#     num1 = float(input("Enter the first side "))
#     num2 = float(input("Ente the second side "))
#     result = rectangle_area(num1,num2)
#     print(f"Area of your rectangle is {result}")
# elif choice == 2:
#     num1 = float(input("Enter the first side "))
#     num2 = float(input("Enter the second side "))
#     num3 = float(input("Enter the third side "))
#     result = triangle_area(num1, num2, num3)
#     print(f"Area of your triangle is {result}")
# elif choice == 3:
#     num1 = float(input("Enter radius "))
#     result = circle_area(num1)
#     print(f"Area of your circle is {result}")
# else:
#     print("Enter the correct option :)")

# #task3
# def count_char(str):
#     char_count = {}
#
#     for char in str:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#     return char_count
# input_str = input("Enter ur word")
# result = count_char(input_str)
# print(result)



