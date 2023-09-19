class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width])
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    

lenght = int(input("Length: "))
width = int(input("Width: "))

rectangle = Rectangle(lenght, width)

print(f"The area of rectangle is: {rectangle.area()}")