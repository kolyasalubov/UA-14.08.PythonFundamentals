def circle_area(r):

    from math import pi as pi
    from math import pow as pow

    circle_area = pi*pow(r,2)
    return circle_area

result_def3 = circle_area(float(input("Enter the radius \n")))

print("Area of the circle =",  result_def3)