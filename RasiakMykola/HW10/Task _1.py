
# 10.0 PRACTICAL TASKS / [GITHUB]

# Task 0
class Polygon:

    def __init__(self, no_of_sides): 
        self.n = no_of_sides 

    def inputSides(self):
        print('\n')
        self.sides = [float(input(f"Enter side {str(i+1)}: ")) for i in range(self.n)]
        
        
    def dispSides(self):
        for i in range(self.n):
            print(f"Side {i+1} is {self.sides[i]}")

            
class Triangle(Polygon):
    
    """
    Calculating the area of a triangle using Heron's formula
             S = (p*(p-a)*(p-b)*(p-c)) ** 0.5
    """
    
    def __init__(self):    
        super().__init__(3) 
    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        p = (a + b + c)/2
#-------------------------------------------------------------
        if (a + b + c)%2 == 0 and p > max(a,b,c) or p > max(a,b,c):
            area = (p*(p-a)*(p-b)*(p-c)) ** 0.5
            #area =  float(round(area))
            print(f"The area of the triangle is {area}")
        else:
            print ("There is no such triangle")
#-------------------------------------------------------------        


t1 = Triangle()
t1.inputSides()
t1.dispSides()
t1.findArea()
print(t1.__doc__)
#print(Triangle.__mro__) # Method Resolution Order

#==============================================================


# 10.1 PRACTICAL TASKS / [GITHUB]

# Task 1
class Rectangle(Polygon):
    
    """
    Calculating the area of a rectangle using the formula
                     S = a ⋅ b
    """
    
    def __init__(self):
        super().__init__(2)
        
        
    def findArea(self):
        a, b = self.sides
        area = a * b
        area = float(round(area))
        print(f"The area of the rectangle is {area}")
        
            
r1 = Rectangle()
r1.inputSides()
r1.dispSides()
r1.findArea()
print(r1.__doc__)


