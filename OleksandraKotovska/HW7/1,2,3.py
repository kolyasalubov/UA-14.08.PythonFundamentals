############# First task ######################


def largest_number(num1: int, num2: int) -> int:
    """
    This function returns the largest
    number of two numbers
    """

    if isinstance(num1, int) and isinstance(num2, int):
        if num1 > num2:
            return(f"Number {num1} is larger then number {num2}")
        else:
            return (f"Number {num2} is larger then number {num1}")
    else:
        return "Please enter the numbers"

print(largest_number(3, 2))


################### Second task #######################


# def rectangle_area(side1: int, side2: int) -> int:
#     """
#     This function calculates 
#     the area of a rectangle
#     """
#     area = side1 * side2 
#     return area

# def triangle_area(base: int, hight: int) -> int:
#     """
#     This function calculates 
#     the area of a triangle
#     """
#     area = 0.5 * base * hight
#     return area

# def circle_area(radius: int) -> int:
#     """
#     This function calculates 
#     the area of a circle
#     """
#     area = 3.14 * radius ** 2
#     return area


# print("Here you can calculate the area of a rectangle, triangle and circle")
# user_choice = input("Choose figure you want to calculate the area: ")
# wrong_data = "Wrong data, enter an integer"
# if user_choice == "rectangle":
#     r1 = (input("Enter the first side: "))
#     r2 = (input("Enter the second side: "))
#     if not r1.isdigit() or not r2.isdigit():
#         print(wrong_data)
#     else:
#         print("The area is:",rectangle_area(int(r1), int(r2)))
# elif user_choice == "triangle":
#     b = input("Enter the base: ")
#     h = input("Enter the hight: ")
#     if not b.isdigit() or not h.isdigit():
#         print(wrong_data)
#     else:
#         print("The area is:",(triangle_area(int(b), int(h))))

# elif user_choice == "circle":
#     r = input("Enter the radius: ")
#     if not r.isdigit():
#         print(wrong_data)
#     else:
#         print("The area is:",(circle_area(int(r))))
# else:
#     print("Enter rectangle, triangle or circle")

#################### Third task ########################


# def count_characters(word):
#     """
#     This function calculates the number
#     of characters included in a given string
#     """
#     word_list = list(word.lower())
#     amount_list = []
#     for i in word_list:
#         amount_list.append(word_list.count(i))

#     my_dict = {}
#     for i, j in enumerate(word_list):
#         my_dict[j] = amount_list[i]

#     return my_dict

# user_word = input("Enter your word to calculates the number of characters: ")
# print(count_characters(user_word))







