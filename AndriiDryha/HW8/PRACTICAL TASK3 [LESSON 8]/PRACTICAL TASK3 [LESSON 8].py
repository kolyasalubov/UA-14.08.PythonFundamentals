Choice = input("Write the area of which figure you want to calculate: 'rectangle', 'triangle' or 'circle' \n")

while True:

    if Choice == "rectangle":
        import Rectangle_area
        print(Rectangle_area.rectangle_area)
        break
    if Choice == "triangle":
        import Triangle_area
        print(Triangle_area.triangle_area)
        break
    if Choice == "circle":
        import Circle_area
        print(Circle_area.circle_area)
        break