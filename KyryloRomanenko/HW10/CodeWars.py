# 1 Regular Ball Super Ball

# class Ball(object):
#     def __init__(self, ball_type="regular"):
#         self.ball_type = ball_type

# 2 Color Ghost

# import random
#
#
# class Ghost(object):
#     def __init__(self):
#         self.color = random.choice(["white", "yellow", "purple", "red"])

# 3 Basic subclasses - Adam and Eve

# def God():
#     return [Man(), Woman()]
#
# class Human(object):
#     pass
#
# class Man(Human):
#     pass
#
# class Woman(Human):
#     pass

# 4 Classy Classes

# class Person:
#     def __init__(self, name, age):
#         self.info = f"{name}s age is {age}"

# 5 Building Spheres

# from math import pi
# class Sphere(object):
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass
#         self.volume = 4*pi * self.radius**3 / 3
#         self.surface = 4*pi* self.radius**2
#     def get_radius(self):
#         return self.radius
#     def get_mass(self):
#         return self.mass
#     def get_volume(self):
#         return round(self.volume,5)
#     def get_surface_area(self):
#         return round(self.surface,5)
#     def get_density(self):
#         return round(self.mass/self.volume, 5)

# 6 Python's Dynamic Classes #1

# def class_name_changer(cls, new_name):
#     assert new_name[0].isupper() and new_name.isalnum()
#     cls.__name__ = new_name