class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def __str__(self):
        return f"This is a {len(self.sides)}-sided polygon."

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width])
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def square_rectangle(self):
        return self.area() ** 2

    def __str__(self):
        return f"This is a rectangle with length {self.length} and width {self.width}."

# Creating an instance of Rectangle
rect = Rectangle(4, 6)

print(rect)
print("Area:", rect.area())
print("Square of Rectangle:", rect.square_rectangle())