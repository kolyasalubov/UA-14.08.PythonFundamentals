from math import sqrt
from math import pi


def rectangle_area(height: float, width: float) -> float:
    """

    :param height: height of the rectangle
    :param width: width of the rectangle

    :return: return the area of the rectangle
    """

    return height * width


def triangle_area(a: float, b: float, c: float) -> float:
    """
    This funcoin uses Heron's formula

    :param a: side AB of the triangle
    :param b: side BC of the triangle
    :param c: side CD of the triangle

    :return: return the area of the triangle
    """
    p = (a + b + c) / 2  # half perimetr

    area = sqrt(p * (p - a) * (p - b) * (p - c))

    return area


def circle_area(rad: float) -> float:
    """

    :param rad: radius of the circle

    :return: return the area of the triangle
    """

    PI = round(pi, 2)
    s = PI * (rad ** 2)
    return s


print(rectangle_area(5, 10))
print(triangle_area(3, 5, 7))
print(circle_area(5))
