import math
def area_of_rectangle(length, width):
    rectangle = length * width
    return rectangle


def area_of_triangle(base, perpendicular_height):
    triangle = 0.5 * base * perpendicular_height
    return triangle

def area_of_circle(radius):
    circle = math.pi * math.pow(radius, 2)
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
