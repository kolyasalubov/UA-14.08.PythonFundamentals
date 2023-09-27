class Polygon:
    def __init__(self, sides):
        self.sides = sides


class Rectangle(Polygon):
    def __str__(self):
        return (f"Rectangle:\n"
                f"length = {self.sides[0]}\n"
                f"width = {self.sides[1]}")

    def __init__(self, l, w):
        super().__init__([l, w])
        self.res = None

    def area(self):
        self.res = self.sides[0] * self.sides[1]
        return self.res


# Test
r1 = Rectangle(5, 10)
print(r1)
print(r1.area())
