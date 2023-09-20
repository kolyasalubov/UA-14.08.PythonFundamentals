import areas

choice = input("Choose a shape to calculate the area: 1. Rectangle; 2. Triangle; 3. Circle  ")

def main():
    if choice == '1':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = areas.rectangle_area(length, width)
        print(f"The area of the rectangle is {area}")
    elif choice == '2':
        base = float(input("Enter the base length of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = areas.triangle_area(base, height)
        print(f"The area of the triangle is {area}")
    elif choice == '3':
        radius = float(input("Enter the radius of the circle: "))
        area = areas.circle_area(radius)
        print(f"The area of the circle is {area}")
    else:
        print("Invalid choice. Please enter 1, 2, 3")

if __name__ == "__main__":
    main()