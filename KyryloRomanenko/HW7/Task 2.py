import math


def rectangle_area() -> float:
    """
    Calculation rectangle area
    :return: float
    """

    print("To calculate the area of a rectangle, you need to enter the height and width:")
    height = float(input("Enter height:"))
    width = float(input("Enter width"))

    return height * width


def triangle_area() -> float:
    """
    Calculation triangle area
    :return: float
    """

    print("To calculate the area of a triangle, you need to enter the height and side:")
    height = float(input("Enter height:"))
    side = float(input("Enter side"))

    return 0.5 * height * side


def circle_area() -> float:
    """
    Calculation circle area
    :return: float
    """

    print("To calculate the area of a circle, you need to enter the radius:")
    radius = float(input("Enter radius:"))

    return math.pi * (radius ** 2)


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


def main():
    variant = var_input()
    match_variant(variant)



if __name__ == "__main__":
    main()
