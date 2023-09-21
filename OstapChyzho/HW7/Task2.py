import math 
def rec_area(length , width):
    """
    calculate area of rectangle
    """
    area_r = length * width
    return area_r
while True:
    try:
        length = float(input("Enter a length of your rectangle:"))
        width = float(input ("Enter a width of your rectangle:"))

        if type(length) == float and type(width) == float:
            area_r = rec_area(length, width)
            print("The are of your rectangle is:", area_r)
            break
        else:
            print("it's not a number")
    except:
        print("it's not a number")

def tri_area(base, height):
    """
    calculate area of triangle
    """
    area_t = 0.5 * (base * height)
    return area_t
while True:
    try:
        base = float(input("Enter a base of your tritangle:"))
        height = float(input ("Enter a height of your tritangle:"))

        if type(base) == float and type(height) == float:
            area_t = tri_area(base, height)
            print("The are of your triangle is:", area_t)
            break
        else:
            print("It's not a number")
    except:    
        print("it's not a number")

def circle_area(radius):
    """
    Calculate the area of a circle.
    """
    pi_num = math.pi
    area_c = pi_num * radius * radius
    return area_c

while True:
    try:
        radius = float(input("Enter the radius of your circle: "))

        if type(radius) == float:
            area_c = circle_area(radius)
            print("The area of your circle is:", area_c)
            break
        else:
            print("It's not a number")
    except:
        print("It's not a number")