import area_calculator

def main():
    print("Select a shape to calculate area: ")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = input("Enter figure number: ")

    if choice == '1':
        a = float(input("Enter side length a: "))
        b = float(input("Enter side length b: "))
        result = area_calculator.rectangle_area(a, b)
        print(f"Area of a rectangle: {result}")
    elif choice == '2':
        a = float(input("Enter base length a: "))
        h = float(input("Enter height h: "))
        result = area_calculator.triangle_area(a, h)
        print(f"Area of a triangle: {result}")
    elif choice == '3':
        r = float(input("Enter radius r: "))
        result = area_calculator.circle_area(r)
        print(f"Area of a circle: {result}")
    else:
        print("Wrong choice")

if __name__ == "__main__":
    main()
