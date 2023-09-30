from math import pow, pi 

def area_of_rectangle(a: float, b: float) -> float:
    '''Calculation the area of a rectangle'''
    return float(a) * float(b)

def area_of_triangle(a: float, h: float) -> float:
    '''Calculation the area of a triangle'''
    return round(0.5 * float(h) * float(a), 5)

def area_of_circle(r: float) -> float:
    '''Calculation the area of a circle'''
    return round(pi * pow(float(r), 2), 5)

