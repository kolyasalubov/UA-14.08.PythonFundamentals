#Import secont module for user input
import geometry
def main():
    print("Choose figure's area for calculate?")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == '1':
        a = float(input("Enter the length of the rectangle: "))
        b = float(input("Enter the width of the rectangle: "))
        area = geometry.rectangle_area(a, b)
        print(f"The area of the rectangle is: {area}")
    elif choice == '2':
        a = float(input("Enter the base of the triangle: "))
        h = float(input("Enter the height of the triangle: "))
        area = geometry.triangle_area(a, h)
        print(f"The area of the triangle is: {area}")
    elif choice == '3':
        r = float(input("Enter the radius of the circle: "))
        area = geometry.circle_area(r)
        print(f"The area of the circle is: {area}")
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()