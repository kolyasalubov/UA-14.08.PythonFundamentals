import math

def rectangle_area(side1: int, side2: int) -> int:
    """
    This function calculates 
    the area of a rectangle
    """
    area = side1 * side2 
    return area

def triangle_area(base: int, hight: int) -> int:
    """
    This function calculates 
    the area of a triangle
    """
    area = 0.5 * base * hight
    return area

def circle_area(radius: int) -> int:
    """
    This function calculates 
    the area of a circle
    """
    area = math.pi * math.pow(radius, 2)
    return area













