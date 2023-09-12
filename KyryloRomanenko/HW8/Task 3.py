import math


def rectangle_area() -> float:
    """
    Calculation rectangle area
    :return: float
    """

    print("To calculate the area of a rectangle, you need to enter the height and width:")
    height = float_check(input("Enter height:"))
    width = float_check(input("Enter width"))

    return height * width


def triangle_area() -> float:
    """
    Calculation triangle area
    :return: float
    """

    print("To calculate the area of a triangle, you need to enter the height and side:")
    height = float_check(input("Enter height:"))
    side = float_check(input("Enter side"))

    return math.sqrt(height * side)


def circle_area() -> float:
    """
    Calculation circle area
    :return: float
    """

    print("To calculate the area of a circle, you need to enter the radius:")
    radius = float_check(input("Enter radius:"))

    return math.pi * math.pow(radius, 2)


def var_input() -> str:
    """
    Asked variant and check. if the variat incorrect ask again
    :return: ones from variant
    """
    variant = input("""
    What area do you want to calculate?:
        1. Rectangle
        2. Triangle
        3. Circle
    Enter the number:
    """)
    while variant not in ('1', '2', '3'):
        variant = input("""
    Incorrect input.
    What area do you want to calculate?:
        1. Rectangle
        2. Triangle
        3. Circle
    Enter the number:
    """)
    else:
        return variant


def match_variant(variant) -> None:
    """

    :param variant: str ("1" or "2" or "3")
    :return: print
    """
    match variant:
        case "1":
            print(f'Area of the rectangle = {rectangle_area()}')
        case "2":
            print(f'Area of the triangle = {triangle_area()}')
        case "3":
            print(f'Area of the circle = {circle_area()}')


def float_check(arg: str) -> float:
    """
    Check if arg cannot be float, asked input aghain
    :param arg: str
    :return: float arg
    """
    while True:
        try:
            arg = float(arg)
            break
        except ValueError:
            print("Invalid input. Please enter a float.")
            arg = input("Enter again:")
    return arg


def main():
    match_variant(var_input())


if __name__ == "__main__":
    main()
