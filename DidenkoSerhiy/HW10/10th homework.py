# 10.1
# class Polygon:
#     def __init__(self, sides):
#         self.sides = sides

#     def perimeter(self):
#         return sum(self.sides)

#     def area(self):
#         pass

# class Rectangle(Polygon):
#     def __init__(self, length, width):
#         super().__init__([length, width])

#     def area(self):
#         return self.sides[0] * self.sides[1]

# rect = Rectangle(4, 6)
# print("Perimeter:", rect.perimeter())
# print("Area:", rect.area())

#10.2

# class Human:
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return f'Hello {self.name}'

# result = Human('Oleg')
# print(result)

# 10.3

# class Employee:
#     counter = 0
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.counter += 1
#     def get_information(self):
#         return f'{self.name}  is receiving {self.salary} in a month'
#     @classmethod
#     def total_number(cls):
#         return f'The total number of employee is: {cls.counter}'

# first_employee = Employee('Anna', '1800')
# print(first_employee.get_information())

# second_employee = Employee("Valeriy", "2000")
# print(second_employee.get_information())

# print(Employee.total_number())