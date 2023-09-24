import formulas

def area():
    """
    Calculation the area of rectangle, tringle or circle
    based on the user's choise
    """
    print("Press 1 to calculate rectangle area\
          Press 2 to calculate triangle area\
          Press 3 to calculate cirle area")
    users_choise = input("Make your choise: ")
    if users_choise == 1:
        a = float(input("Enter rectangle side: "))
        b = float(input("Enter the second side: "))
        area = formulas.rectangle_area(a,b)
        print(f"The are of rectangle is {area}")
    elif users_choise == 2:
        h = float(input("Enter the triangle's height: "))
        a = float(input("Enter the base of triangle: "))
        area = formulas.triangle_area(h,a)
        print(f"Triangle's area is {area}")
    elif users_choise == 3:
        r = float(input("Enter the circle's radius"))
        area = formulas.circle_area(r)
        print(f"Circle's area is {area}")
    else:
        print("Wrong input. Please make your choise 1,2 or 3")

if __name__ == "__area__":
    area()



