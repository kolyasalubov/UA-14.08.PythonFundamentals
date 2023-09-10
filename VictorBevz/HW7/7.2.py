figure = input("Choose a type of geometric figure(e.g. rectangle, triangle, circle):")
if figure == "rectangle":
    a = int(input("Length of first side:"))
    b = int(input("Length of second side:"))
    area_rec = a * b
    print("Area of rectangle =", a * b)
elif figure=="triangle":
    a = int(input("Length of first side:"))
    b = int(input("Length of second side:"))
    c = int(input("Length of third side:"))
    p = (a+b+c)/2
    area_tr = (p*(p-a)*(p-b)*(p-c))**0.5
    print("Area of triangle =", round(area_tr, 2))
else:
    r=int(input('Enter radius:'))
    area_cir =3.14*(r**2)
    print ("Area of circle =", round(area_cir, 2) )