class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
        
    def inputSides(self):
        self.sides = [float(input(f"Enter side {str(i+1)}: ")) for i in range(self.n)]
    
    def dispSides(self):
        for i in range(self.n):
            print(f"Side {i+1} is {self.sides[i]}")
 
            
class Triangle(Polygon):
    """
    Triangle class
    """
    def __init__(self):
        # Polygon.__init__(self, 3)
        super().__init__(3)
        print("\nPlease enter the sides of the triangle:")
        super().inputSides()
        self.findArea()

    def checking_existence(self):
        """checking for the existence of a triangle"""
        triangle_sides = self.sides
        triangle_sides.sort() 
        if triangle_sides[0] + triangle_sides[1] <= triangle_sides[2]:
            return False
        return True

    def findArea(self):
        a, b, c = self.sides
        
        if self.checking_existence():
            # calculate the semi-perimeter
            p = (a + b + c) / 2
            area = (p*(p-a)*(p-b)*(p-c)) ** 0.5
            print(f"The area of the triangle is {round(area, 2)}")
        else:
            print("The triangle with such sides cannot exist!")

class Rectangle(Polygon):
    """
    Rectangle class
    """
    def __init__(self):
        # Polygon.__init__(self, 3)
        super().__init__(2)
        print("\nPlease enter the sides of the rectangle:")
        super().inputSides()
        self.findAreaRect()

    def findAreaRect(self):
        a, b = self.sides
        # calculate the semi-perimeter
        area = a*b
        print(f"The area of the rectangle is {area}")



t = Triangle()
w = Rectangle()
