# Task 1
def largest_number_of_two_numbers(number1, number2):
    ''' This function takes two numbers, 'a' and 'b', and returns the largest of two numbers'''
    if number1 > number2:
        return number1
    elif number2 > number1:
        return number2
    elif number1 == number2:
        return "The numbers are the same!!!"


result = largest_number_of_two_numbers(3, 3)
print(result)


# Task 2
def area_of_rectangle(length, width):
    rectangle = length * width
    return rectangle


def area_of_triangle(base, perpendicular_height):
    triangle = 0.5 * base * perpendicular_height
    return triangle


def area_of_circle(radius):
    pi = 3.14
    circle = pi * radius ** 2
    return circle


print("\nMENU")
print("Enter 1 to find area of rectangle")
print("Enter 2 to find area of triangle")
print("Enter 3 to find area of circle")
while True:
    choice = input("Enter your choice:")
    if choice == "1":
        length = float(input("Enter length of rectangle: "))
        width = float(input("Enter width of rectangle: "))
        print("Area of rectangle: ", (area_of_rectangle(length, width)))
    if choice == "2":
        base = float(input("Enter base of triangle: "))
        perpendicular_height = float(input("Enter perpendicular height of triangle: "))
        print("Area of triangle: ", (area_of_triangle(base, perpendicular_height)))
    if choice == "3":
        radius = float(input("Enter radius of circle: "))
        print("Area of radius: ", (area_of_circle(radius)))
    if choice == "exit":
        break

# Task 3
def number_of_characters(string):
    char_count = {}
    while True:
        for char in string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count
string = str(input("\nEnter string: "))
print("Number of characters included in given string: ", number_of_characters(string))
