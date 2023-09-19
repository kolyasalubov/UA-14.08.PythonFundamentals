import geometry
figure = input("Choose a type of geometric figure(e.g. rectangle, triangle, circle):")
if figure == "rectangle":
    a = float(input("Length of first side:"))
    b = float(input("Length of second side:"))
    area_rec = geometry.rec_area(a, b)
    print("Area of rectangle =", area_rec)
elif figure=="triangle":
    a = float(input("Length of first side:"))
    b = float(input("Length of second side:"))
    area_tr = geometry.tr_area(a, b)
    print("Area of triangle =", round(area_tr, 2))
else:
    r = float(input('Enter radius:'))
    area_cir = geometry.cir_area(r)
    print ("Area of circle =", round(area_cir, 2) )