# #first task
# class Polygon:
#     def __init__(self, sides):
#         self.sides = sides
#
#     def find_area(self):
#         pass
#
#
# class Rectangle(Polygon):
#     def __init__(self, length, width):
#         super().__init__(4)
#         self.length = length
#         self.width = width
#
#     def find_area(self):
#         return self.length * self.width
#
# my_rect = Rectangle(20, 10)
# print(my_rect.find_area())

# #second task
# class Human:
#     species = "Homosapiens"
#
#     def __init__(self, name):
#         self.name = name
#
#     def welcome_message(self):
#         return f"Hello, my name is {self.name}"
#
#     def get_species(self):
#         return f"I beyond to {self.species}"
#
#     def arbitrary_message(self):
#         return "I love python"
#
# first = Human("Marik")
#
# print(first.get_species())
# print(first.welcome_message())
# print(first.arbitrary_message())

# #third task
# class Employee:
#     total_employees = 0
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.total_employees += 1
#
#     def display_employees(self):
#         return f"Total employees: {self.total_employees} "
#
#     def info_about_employees(self):
#         return f"Info: Name: {self.name}, Salary: {self.salary} "
#
# first = Employee("Marik", 3000)
#
# print(first.info_about_employees())
# print(Employee.total_employees)
#
# print(f"Base Classes: {Employee.__bases__}")
# print(f"Class Namespace: {Employee.__dict__}")
# print(f"Class Name: {Employee.__name__}")
# print(f"Module Name: {Employee.__module__}")
# print(f"Documentation String: {Employee.__doc__}")


