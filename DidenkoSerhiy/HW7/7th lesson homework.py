#task 7.1

def compare_numbers(number1, number2):
    """
    This function created to compare 2 numbers
    """
    if number1 > number2:
        print(f"{number1} is bigger than {number2}")
    elif number1 < number2:
        print(f"{number2} is bigger than {number1}")
    else:
        print(f"{number1} is equal {number2}")
        return compare_numbers

number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))
compare_numbers(number1, number2)

#task 7.2

user_choice = int(input("Press 1 if you want to calculate rectangle area,\n"\
                        "Press 2 if you want to calculate triangle area,\n"\
                        "Press 3 if you want to calculate circle area: "))

if user_choice == 1:
    def rectangle_area(rectangle_a_side, rectangle_b_side):
        """
        This function calculates the area of the rectangle
        """
        return rectangle_a_side * rectangle_b_side
    
    rectangle_a_side = float(input("Enter the side of the rectange: "))
    rectangle_b_side = float(input("Enter another rectangle side: "))
    rectangle_area_result = "{:.2f}".format(rectangle_area(rectangle_a_side, rectangle_b_side))
    print("Rectangle area is: ", rectangle_area_result)


if user_choice == 2:
    def triangle_area(triangle_height, triangle_side):
        """
        This function calculates triangle area
        """
        return 1/2 * triangle_height * triangle_side
    
    triangle_height = float(input("\nEnter the height of triangle: "))
    triangle_side = float(input("Enter the side of triangle: "))
    triangle_area_result = "{:.2f}".format(triangle_area(triangle_height, triangle_side))
    print("Triangle area is: ", triangle_area_result)

if user_choice == 3:
    def circle_area(circle_radius):
        """
        This function calculates the area of the circle
        """
        return 3.14 * circle_radius ** 2
    circle_radius = float(input("Enter the radius of the circle: "))
    circle_area_result = "{:.2f}".format(circle_area(circle_radius))
    print("The area of the circle is:", circle_area_result)

#task 7.3

def characters_calculate(string_input):
    string_count = {}

    for i in string_input:
        if i in string_count:
            string_count[i] += 1
        else:
            string_count[i] = 1
    return string_count

string_input = input(str("Enter the word: "))
string_input_result = characters_calculate(string_input)
print(string_input_result)