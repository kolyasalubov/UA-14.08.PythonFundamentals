################# 1st task ##########################

class Poligon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = []
        for i in range(no_of_sides):
            self.sides.append(0)
    def input_sides(self):
        self.sides = []
        for i in range(self.n):
            self.sides.append(float(input(f"Enter side{i + 1}: ")))
    def disp_sides(self):
        for i in range(self.n):
            print(f"Side {i + 1} is {self.sides[i]}")

class Triangle(Poligon):
    def __init__(self):
        super().__init__(3)
    
    def find_area(self):
        a, b, c = self.sides
        if a > b + c or b > a + c or c > a + b: #check existence
            s = (a + b + c) / 2
            area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
            print(f"The area of the triangle is {area}")
        else: 
            print ("This triangle not exists")
        
print("Find the area of the triangle")
t = Triangle()
t.input_sides()
t.disp_sides()
t.find_area()


class Rectangle(Poligon):
    def __init__(self):
        super().__init__(2)
    
    def find_area(self):
        a, b = self.sides
        area = a * b
        print(f"The area of the rectangle is {area}")

print("Find the area of the rectangle")
t = Rectangle()
t.input_sides()
t.disp_sides()
t.find_area()




################## 2nd task ###################

# class Human:
#     species = "Homosapiens"
#     def __init__(self, name):
#         self.name = name
#     def get_name(self):
#         return f"Hello, {self.name}"
#     @classmethod
#     def classmethod(cls):
#         return f"Human is a species of {cls.species}"
#     @staticmethod
#     def staticmethod():
#         return "It is a static method"


# h = Human("Iryna")
# print(h.get_name())
# print(h.classmethod())
# print(h.staticmethod())





################## 3rd task ###############

# class Employee:
#     """
#     Employee information
#     """
#     number = 0
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.number += 1
#     def get_info(self):
#         return f"{self.name} has {self.salary}$"
#     @classmethod
#     def get_number(cls):
#         return f"The total number of employee is {cls.number}"   


# info1 = Employee("Sara", "1000")
# print(info1.get_info())


# info2 = Employee("Rachel", "1500")
# print(info2.get_info())

# info3 = Employee("Samanta", "2000")
# print(info3.get_info())


# print(Employee.get_number())

# print(Employee.__bases__)
# print(Employee.__dict__)
# print(info2.__class__.__name__)
# print(info1.__module__)
# print(info1.__doc__)







