def circle_area(r):

    from math import pi as pi

    circle_area = pi*r**2
    return circle_area

result_def3 = circle_area(float(input("Enter the radius \n")))

print("Area of the circle =",  result_def3)