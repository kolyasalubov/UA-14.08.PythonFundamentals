import math

# Function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    return length * width

# Function to calculate the area of a triangle
def calculate_triangle_area(base, height):
    return 0.5 * base * height

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

# Main program
print("Welcome to the Area Calculator!")

while True:
    print("\nChoose a shape:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = calculate_rectangle_area(length, width)
        print(f"The area of the rectangle is {area:.2f} square units.")
    elif choice == "2":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = calculate_triangle_area(base, height)
        print(f"The area of the triangle is {area:.2f} square units.")
    elif choice == "3":
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(radius)
        print(f"The area of the circle is {area:.2f} square units.")
    elif choice == "4":
        print("Thank you for using the Area Calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")