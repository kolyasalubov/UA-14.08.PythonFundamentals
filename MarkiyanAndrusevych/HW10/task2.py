# #task1
# class Ball(object):
#     def __init__(self, ball_type="regular"):
#         self.ball_type = ball_type
#
# ball1 = Ball()
# ball2 = Ball("lox")
#
# print(ball1.ball_type)
# print(ball2.ball_type)

# #task2
# import random
# class Ghost(object):
#     def __init__(self):
#         colors = ["white", "yellow", "purple", "red"]
#         self.color = random.choice(colors)
#
# gh1 = Ghost()
# print(gh1.color)

# #task3
# class Human:
#     def __init__(self, name):
#         self.name = name
#
# class Woman(Human):
#     def __init__(self, name):
#         super().__init__(name)
#
# class Man(Human):
#     def __init__(self, name):
#         super().__init__(name)
#
# def God():
#     adam = Man("Adam")
#     eve = Woman("Eve")
#     return [adam, eve]
#
# adam, eve = God()
#
# print(adam.name)
# print(eve.name)

# #task4
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.info= f"{name}s age is {age}"
#
# marik = Person("Marik", 24)
# print(marik.info)

# #task5
# import math
# class Sphere(object):
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass
#
#     def get_radius(self):
#         return self.radius
#
#     def get_mass(self):
#         return self.mass
#
#     def get_volume(self):
#         volume = (4/3) * math.pi * self.radius**3
#         return round(volume, 5)
#
#     def get_surface_area(self):
#         surf_area = 4 * math.pi * self.radius**2
#         return round(surf_area, 5)
#
#     def get_density(self):
#         return round(self.mass / self.get_volume(), 5)
#
# mysphere = Sphere(2, 40)
# print(mysphere.get_volume())
# print(mysphere.get_mass())
# print(mysphere.get_density())
# print(mysphere.get_radius())
# print(mysphere.get_surface_area())

# #task6
# import re
#
# def class_name_changer(cls, new_name):
#     if not re.match(r'^[A-Z][a-zA-Z0-9]*$', new_name):
#         raise ValueError("Invalid class name. Class names must start with an uppercase letter "
#                          "and contain only alphanumeric characters.")
#
#     cls.__name__ = new_name
#
# class MyClass:
#     pass
#
# class_name_changer(MyClass, "UsefulClass")
