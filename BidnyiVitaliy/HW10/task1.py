# Create a polygon class and a rectangle class 
# that inherits from the polygon class and finds the square 
# of rectangle.

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]


class Rectangle(Polygon):
    def __init__(self, width, length):
        Polygon.__init__(self, 4)
        self.sides = [width,length, width, length]
        
    def square(self):
        return self.sides[0] * self.sides[1]

#test
r = Rectangle(10, 5)
print('S = ', r.square())
