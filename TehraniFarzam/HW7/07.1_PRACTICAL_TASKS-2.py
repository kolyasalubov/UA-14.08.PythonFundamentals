# ============= The area of circle ================
def calculate_circle_area(radius, pi = 3.14):
    """
    Calculate the area of a circle

    Parameters: 
    radius (float): The radius of the circle 
    pi (float) = 3.14
    
    Returns: 
    The area of circle (float)
    """
    area = pi * (radius ** 2)
    return area
# ============= The area of rectangle ================
def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle

    Parameters: 
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.
    
    Returns: 
    The area of rectangle (float)
    """
    area = length * width
    return area
# ============= The area of triangle ================
def calculate_triangle_area(base, height):
    """
    Calculate the area of a triangle

    Parameters: 
    base (float): The length of the triangle's base.
    height (float): The height of the triangle.
    
    Returns: 
    The area of triangle (float)
    """
    area = base * height
    return area
# ============= The area of selected shape ================
def calculate_area(shape)-> None:
    """
    Calculate the area of a shape selected by user.

    Parameters:
    shape (str): The name of the shape ('rectangle', 'circle', 'triangle').

    Returns:
    None
    """
    shape = shape.lower() 

    shape_functions = {
        'rectangle': calculate_rectangle_area,
        'circle': calculate_circle_area,
        'triangle': calculate_triangle_area,
    }

    match shape:
        case 'rectangle':
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            return shape_functions['rectangle'](length, width)
        
        case 'circle':
            radius = float(input("Enter the radius: "))
            return shape_functions['circle'](radius)

        case 'triangle':
            base = float(input("Enter the base: "))
            height = float(input("Enter the height: "))
            return shape_functions['triangle'](base, height)

        case _:
            raise ValueError("Invalid shape name.")
user_shape = input("Enter the name of the shape (rectangle, circle, or triangle): ")

result = calculate_area(user_shape)
print(f"The area of the {user_shape} is {result}.")


# I may have spent around 6 hours writing this!

