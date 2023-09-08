# 1 Function for calculation area of a rectangle
def rectangle_area(a, b):
    """ Function for calculation area of a rectangle"""
    
    if a.isdecimal() and b.isdecimal():
        a = int(a)
        b = int(b)

        area = a * b
        return area
    else:
        return 'Error! You have enter not a digit.'



# 2 Function for calculation area of a triangle
def triangle_area(a, b, c):
    """ Function for calculation area of a triangle
    p = (a + b + c) / 2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    """
    from math import sqrt

    if a.isdecimal() and b.isdecimal() and c.isdecimal():
        a = int(a)
        b = int(b)
        c = int(c)

        p = (a + b + c) / 2
        s = sqrt(p*(p-a)*(p-b)*(p-c))
        return s
    else:
        return 'Error! You have enter not a digit.'

# 3 Function for calculation area of a circle
def circle_area(radius):
    """ Function for calculation area of a circle
    S = π * r**2
    """
    from math import pi

    if radius.isdecimal():
        radius = int(radius)

        s = pi * radius ** 2
        return s
    else:
        return 'Error! You have enter not a digit.'


print ("\nArea of a rectangle:")
a = input("Please enter the first side (a): ")
b = input("Please enter the second side (b): ")
print(f"Area of rectangle will be: {rectangle_area(a, b)}")

print ("\nArea of a triangle:")
a = input("Please enter the first side (a): ")
b = input("Please enter the second side (b): ")
c = input("Please enter the thirth side (c): ")
print(f"Area of triangle will be: {triangle_area(a, b, c)}")

print ("\nArea of a circle:")
s = input("Please enter the radius of circle (r): ")
print("Area of circle will be: ", circle_area(s))
