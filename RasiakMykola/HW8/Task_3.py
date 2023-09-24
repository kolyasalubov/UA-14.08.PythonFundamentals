from math import pi, pow


def rectangle_area(its_width, its_height):
    return its_width * its_height

def triangle_area(its_side, its_height):
    return  (1/2) * its_side * its_height

def circle_area(circle_radius):
    return pi * pow(circle_radius, 2)



def main():
    
    while True:
        print("\nSelect a geometric shape to calculate the area:")
        print("Rectangle - 1,")
        print("Triangle - 2,")
        print("Circle - 3,")
        print("Exit - 4.\n")
        
        actions = int(input("Your number: "))
        
        if actions > 4:
            print("\t\tPlease select a number from 1 to 4")
            print('#','-'*70)
        match actions:
            case 1:
                its_width = float(input("Enter the rectangle width: "))
                its_height = float(input("Enter the rectangle height: "))
                result = rectangle_area(its_width, its_height)
                print(f"The area of the rectangle is: {result}")
                print('#','-'*70)
            case 2:
                its_side = float(input("Enter the side of a triangle: "))
                its_height = float(input("Enter the height of a triangle: "))
                result = triangle_area( its_side, its_height)
                print(f"The area of the triangle is: {result}")
                print('#','-'*70)
            case 3:
                circle_radius = float(input("Enter the circle radius: "))
                result = circle_area(circle_radius)
                print(f"The area of the circle is: {result}")
                print('#','-'*70)
            case 4:
                break
            
if __name__ == "__main__":
    main()

   
        

