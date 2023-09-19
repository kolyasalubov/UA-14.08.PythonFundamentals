class Poligon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def input_sides(self):
        self.sides = [float(input(f"Enter side {str(i + 1)}: ")) for i in range(self.n)]

    def disp_sides(self):
        for i in range(self.n):
            print(f"Side {i + 1} is {self.sides[1]}")


class Triangle(Poligon):
    def __init__(self):
        super().__init__(3)

    def find_area(self):
        a, b, c = self.sides

        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print(f"The area of the triangle is {area}")


class Rectangle(Poligon):
    def __init__(self):
        super().__init__(2)

    def find_area(self):
        l, w = self.sides
        area = l * w
        print(f"The area of the rectangle is {area}")


def triangle_request():
    t = Triangle()
    print("Enter the sides of the triangle")
    t.input_sides()
    t.disp_sides()
    t.find_area()


def rectangle_reqest():
    r = Rectangle()
    print("Enter the side of rectangle")
    r.input_sides()
    r.disp_sides()
    r.find_area()


def choise():
    number = input("Which area do you want a calculate:\n"
                   "1. Triangle\n"
                   "2. Rectangle\n"
                   "Enter: ")
    match number:
        case "1":
            triangle_request()
        case "2":
            rectangle_reqest()
        case _:
            number = input("Incorrect Enter. Which area do you want a calculate:\n"
                           "1. Triangle\n"
                           "2. Rectangle\n"
                           "Enter: ")


if __name__ == '__main__':
    choise()
