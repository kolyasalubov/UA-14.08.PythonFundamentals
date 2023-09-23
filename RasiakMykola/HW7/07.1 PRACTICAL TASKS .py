
# 07.1 PRACTICAL TASKS / [GITHUB TOPIC 7]

# Task1.
def largest_number(num1, num2):
    """
    Find the largest number among two numbers using the max function.

    Returns:
    int or float.
    
    """
    return max(num1, num2)

largest_number = largest_number(456, 256)
print('\nThe largest number are: ', largest_number)

print('#','-'*70)
#############################################################

# 07.1 PRACTICAL TASKS / [GITHUB TOPIC 7]

# Task2.

while True:
    print("\nSelect a geometric shape to calculate the area:")
    print("Triangle - 1,")
    print("Rectangle - 2,")
    print("Circle - 3,")
    print("Exit - 4.\n")
    actions = int(input("Your number: "))
    if actions > 4:
        print("\t\tPlease select a number from 1 to 4")
    
    match actions:
        case 1:
            its_side = float(input("Enter the side of a triangle: "))
            its_height = float(input("Enter the height of a triangle: "))
            def triangle_area(its_side, its_height):
                triangle_area_s = 1/2*its_side*its_height
                return triangle_area_s
    
            triangle_area = triangle_area(its_side, its_height)
            print("The area of the triangle is", triangle_area)
            print('#','-'*70)
            
        case 2:
            its_width = float(input("Enter the rectangle width: "))
            its_height = float(input("Enter the rectangle height: "))
            def rectangle_area(its_width, its_height):
                rectangle_area_s = its_width*its_height
                return rectangle_area_s
    
            rectangle_area = rectangle_area(its_width, its_height)
            print("The area of the rectangle is", rectangle_area)
            print('#','-'*70)
            
        case 3:
            circle_radius = float(input("Enter the circle radius: "))
            def circle_area(circle_radius):
                circle_area_s = 3.14*circle_radius**2
                return circle_area_s
    
            circle_area = circle_area(circle_radius)
            print("The area of the circle is", circle_area)
            
        case 4:
            break

print('#','-'*70)
#############################################################

# 07.1 PRACTICAL TASKS / [GITHUB TOPIC 7]

# Task3.
user_word = input('Type any English word: ')

def count_characters(input_str):
    output_count = {}
    for char in user_word:
        if char in output_count:
            output_count[char] += 1
        else:
            output_count[char] = 1
   
    return output_count

user_word = user_word.lower()
result = count_characters(user_word)
print(result)

#############################################################           

    


