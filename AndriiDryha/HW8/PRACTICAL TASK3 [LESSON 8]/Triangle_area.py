def triangle_area(c, h):

    triangle_area = 0.5*c*h
    return triangle_area

result_def2 = triangle_area(float(input("Enter the base \n")), float(input("Enter the height \n")))

print("Area of the triangle =",  result_def2)