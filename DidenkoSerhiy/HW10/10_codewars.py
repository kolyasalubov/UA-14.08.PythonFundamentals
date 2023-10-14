# 1. Regular Ball Super Ball

# class Ball(object):
#     def __init__(self, ball_type = 'regular'):
#         self.ball_type = ball_type

# # 2. Color Ghost
# import random

# class Ghost(object):
#     def __init__(self):
#         self.color = random.choice(["white", "yellow", "purple", "red"])

# 3. Basic subclasses - Adam and Eve

# class Human():
#     pass

# class Man(Human):
#     def __init__(self, name):
#         self.name = name
        
# class Woman(Human):
#     def __init__(self, name):
#         self.name = name
# a1 = Man('Adam')
# a2 = Woman("Eva")

# def God():
#     return [a1, a2]

# 4. Classy Classes
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.info = f"{self.name}s age is {self.age}"
#     def get_info(self):
#         return self.info

# 5. Building Spheres
# import math
# class Sphere(object):
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass
#     def get_radius(self):
#         return self.radius
#     def get_mass(self):
#         return self.mass
#     def get_volume(self):
#         return round(4/3 * math.pi * self.radius ** 3, 5)
#     def get_surface_area(self):
#         return round(4 * math.pi * self.radius ** 2, 5)
#     def get_density(self):
#         return round(self.mass / self.get_volume(), 5)

# 6. Dynamic Classes
# import re

# def class_name_changer(cls, new_name):
#     if re.match(r'^[A-Z][a-zA-Z0-9-_]*$', new_name):
#         cls.__name__ = new_name
#     else:
#         raise Exception('Invalid Class Name')