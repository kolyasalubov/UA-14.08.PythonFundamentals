#First task: Write a function that returns the largest number of two numbers
def get_largest_numb(num1, num2):
    """Returns the largest of two numbers.
    Used: num1 (int or float): The first number.
          num2 (int or float): The second number.
    Returns:
        int or float: The largest of the two numbers."""
    if num1 > num2:
        return num1
    else:
        return num2
largest_number = get_largest_numb(568, 8.5)
print(largest_number)
print("------------------------")
#Second task: Write a program that calculates the area of ​a rectangle, triangle and circle
def rectangle_area(length, width):
    """Calculates the area of a rectangle.
    The length (float) of the rectangle.
    The width (float) of the rectangle.
    The area (float) of the rectangle."""
    return length * width
def triangle_area(base, height):
    """Calculates the area of a triangle.
    The base length (float) of the triangle.
    The height (float) of the triangle.
    The area (float) of the triangle."""
    return 0.5 * base * height
def circle_area(radius):
    """Calculates the area of a circle.
    The radius (float) of the circle.
    The area (float) of the circle."""
    return 3.14 * (radius**2)
def main():
    print("Choose a shape to calculate its area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = int(input("Enter your choice (1, 2, or 3): "))

    if choice == 1:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = rectangle_area(length, width)
        print(f"The area of the rectangle is: {area}")
    elif choice == 2:
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = triangle_area(base, height)
        print(f"The area of the triangle is: {area}")
    elif choice == 3:
        radius = float(input("Enter the radius of the circle: "))
        area = circle_area(radius)
        print(f"The area of the circle is: {area}")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
if __name__ == "__main__":
    main()
print("----------------------")
#Third task:Write a function that calculates the number of characters included in a given string
def calc_characters(input_string):
    """Calculates the number the number of characters included in a given string.
        input_string (str): The input string.
        dict: A dictionary containing characters as keys and their respective counts as values."""
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
input_string = "family"
char_count = calc_characters(input_string)
print(char_count)

