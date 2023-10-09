# #1
# class Ball:
#     def __init__(self, ball_type = "regular"):
#         self.ball_type = ball_type
    
# #2
# import random

# class Ghost:
#     def __init__(self):
#         self.color = random.choice(["white", "yellow", "purple", "red"])

# #3
# def God():
#     return [Man("Adam"), Woman("Eve")]

# class Human:
#     def __init__(self, name):
#         self.name = name
        
# class Man(Human):
#     def __init__(self, name):
#         self.name = name
        
# class Woman(Human):
#     def __init__(self, name):
#         self.name = name

# #4
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     @property
#     def info(self):
#         return f"{self.name}s age is {self.age}"

# #5
# import math

# class Sphere(object):
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass
#         self.volume = round(4 * pi * radius**3 / 3, 5)
#         self.surface_area = round(4 * pi * radius**2, 5)
#         self.density = round(self.mass / self.volume, 5)
    
#     def __getattr__(self, name):
#         return lambda: getattr(self, name[4:])

# #6
# import re

# def class_name_changer(cls, new_name):
#     if not re.match(r'^[A-Z][a-zA-Z0-9]*$', new_name):
#         raise ValueError("Invalid class name format")
        
#     cls.__name__ = new_name