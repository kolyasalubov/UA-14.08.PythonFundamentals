# Task 1
class Polygon:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(0, 0)

    def input(self):
        self.length = int(input("Enter your length: "))
        self.width = int(input("Enter your width: "))

    def square(self):
        square = self.length * self.width
        return square

    def output(self, square):
        print(f"Your square: {square}")


rectangle = Rectangle()
rectangle.input()


square = rectangle.square()
rectangle.output(square)