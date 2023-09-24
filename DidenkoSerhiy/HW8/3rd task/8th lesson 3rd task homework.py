import formulas

def main():
    print("Enter the details")
    a = float(input("Enter rectangle side:"))
    b = float(input("Enter the second side:"))
    area = formulas.rectangle_area(a,b)
    print(f"The area is {area}")

if __name__ == "__main__":
    main()

# print("Enter the details")
# a = float(input("Enter rectangle side: "))
# b = float(input("Enter second side: "))

# area = formulas.rectangle_area(a,b)

# print(f"The area is {area}")

