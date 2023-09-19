class Poligon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def input_sides(self):
        self.sides = [float(input(f"Enter side {str(i + 1)}")) for i in range(self.n)]

    def disp_Sides(self):
        for i in range(self.n):
            print(f"Side {i + 1} is {self.sides[1]}")


class Triangle(Poligon):
    def __init__(self):
        Poligon.__init__(self, 3)

    def find_area(self):
        a, b, c = self.sides

        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print(f"The area of the triangle is {area}")


t = Triangle()
t.input_sides()
t.disp_Sides()
t.find_area()
