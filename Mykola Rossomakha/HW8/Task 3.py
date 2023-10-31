import math

def rectangle_area(length, width):
    return length * width

def triangle_area(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

def circle_area(radius):
    return math.pi * radius ** 2

print("Welcome to the area calculator :)")
print("Choose the shape:")
print("1. Rectangle\n2. Triangle\n3. Circle")

choice = int(input())

if choice == 1:
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    result = rectangle_area(length, width)
    print(f"Area of your rectangle is {result}")
elif choice == 2:
    side1 = float(input("Enter the first side: "))
    side2 = float(input("Enter the second side: "))
    side3 = float(input("Enter the third side: "))
    result = triangle_area(side1, side2, side3)
    print(f"Area of your triangle is {result}")
elif choice == 3:
    radius = float(input("Enter the radius: "))
    result = circle_area(radius)
    print(f"Area of your circle is {result}")
else:
    print("Enter a valid option.")
