import math

def rectangle(a, b):
    return a * b

def triangle(a, b, c):
    p = (a + b + c)/2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s

def circle(r):
    return  math.pi * r * r