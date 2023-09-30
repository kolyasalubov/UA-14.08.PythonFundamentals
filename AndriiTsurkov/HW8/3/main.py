from figures_area import *

def num_check(num: str):
    ''' Check for float'''
    try:
        if float(num):
            return True
    except:
        return False

while True:
    print("For EXIT plese enter 'q'.")
    user_choice = input("Enter a digit to calculate the area of the required figure (rectangle: 1, triangle: 2, circle: 3): ")
    if user_choice.lower() == "q":
        print("Bye")
        exit(0)
    if num_check(user_choice) and (user_choice == "1" or user_choice == "2" or user_choice == "3"):
        
        match user_choice:
            case "1":
                print("Area of rectangle:")
                a = input("Please enter side 'a': ")
                b = input("Please enter side 'b': ")
                if num_check(a) and num_check(b):
                    print("Area of rectangle will be: ", area_of_rectangle(a, b), "\n")
                else:
                    print(f"Please enter only digits!\n")
                
            case "2":
                print("Area of triangle:")
                a = input("Please enter side 'a': ")
                h = input("Please enter height 'h': ")
                if num_check(a) and num_check(h):
                    print("Area of triangle will be: ", area_of_triangle(a, h), "\n")
                else:
                    print(f"Please enter only digits!\n")
        
            case "3":
                print("Area of circle:")
                r = input("Please enter radius of circle: ")
                if num_check(r):
                    print("Area of circle will be: ", area_of_circle(r), "\n")
                else:
                    print(f"Please enter only digits!\n")
    
        
    else:
        print("Error: Please choose only from: 1, 2 or 3.\n")