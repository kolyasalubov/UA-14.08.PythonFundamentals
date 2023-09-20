from math import pi, pow


def area_rectangle(width: int, height: int) -> int:
    return width * height


def area_triangle(base: int, height: int) -> float:
    return (1 / 2) * base * height


def area_circle(radius: int) -> float:
    return pi * pow(radius, 2)
