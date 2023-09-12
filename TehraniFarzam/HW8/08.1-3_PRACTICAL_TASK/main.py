import area_calculator

def main():
    choice = input("Enter the name of the shape (rectangle, triangel, cirlcle): ")


    if choice == "rectangle":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = area_calculator.rectangle_area(length, width)
        print(f"The are of {choice} is: {area}")

    elif choice == "triangle":
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        area = area_calculator.triangle_area(base, height)
        print(f"The are of {choice} is: {area}")
    elif choice == "circle":
        radius = float(input("Enter the radius: "))
        area = area_calculator.circle_area(radius)
        print(f"The are of {choice} is: {area}")

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()