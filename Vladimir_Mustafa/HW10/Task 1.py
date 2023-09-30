class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

    def area(self):
        raise NotImplementedError("The 'area' method must be overridden in a subclass.")


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width, length, width])

    def area(self):
        return self.sides[0] * self.sides[1]

    def square_area(self):
        side_length = min(self.sides[0], self.sides[1])
        return side_length ** 2


