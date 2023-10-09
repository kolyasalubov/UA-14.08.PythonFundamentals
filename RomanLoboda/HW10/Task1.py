class Polygon:
    def __init__(self, no_sides):
        self.n = no_sides
        self.sides = [0 for i in range(no_sides)]

    def inp_sides(self):
        self.sides = [float(input(f"Enter side {str(i + 1)} : ")) for i in range(self.n)]

    def dis_sides(self):
        for i in range(self.n):
            print(f"Side {i + 1} is {self.sides[i]}")


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def find_area(self):
        a, b = self.sides
        area = a * b
        print(f"The area of rectangle : {area}")


rect1 = Rectangle()
rect1.inp_sides()
rect1.dis_sides()
rect1.find_area()
