def rectangle_area(a, b):
    result = a * b
    return result

def triangle_area(a, b, c):
    result = (a + b + c) / 2
    return result

def circle_area(a):
    result = a * a * 3.14
    return result

print("Welcome to the area calculator :)\nChoose the shape:")
print("1. Rectangle\n2. Triangle\n3. Circle")
choice = int(input())

if choice == 1:
    num1 = float(input("Enter the first side: "))
    num2 = float(input("Enter the second side: "))
    result = rectangle_area(num1, num2)
    print(f"Area of your rectangle is {result}")
elif choice == 2:
    num1 = float(input("Enter the first side: "))
    num2 = float(input("Enter the second side: "))
    num3 = float(input("Enter the third side: "))
    result = triangle_area(num1, num2, num3)
    print(f"Area of your triangle is {result}")
elif choice == 3:
    num1 = float(input("Enter radius: "))
    result = circle_area(num1)
    print(f"Area of your circle is {result}")
else:
    print("Enter the correct option :)")
