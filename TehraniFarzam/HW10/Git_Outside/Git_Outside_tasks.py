# # ============Ball super ball =====================
# class Ball:
#     def __init__(self, ball_type = "regular"):
#         self.ball_type = ball_type
    
# # ============= Color ghost ===================
# import random

# class Ghost:
#     def __init__(self):
#         colors = ["white", "yellow", "purple", "red"]
        
#         self.color = random.choice(colors)

# # ============ Basic subclasses-Adam and Eve ==========
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

# # ============ Classy classes =====================
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     @property
#     def info(self):
#         return f"{self.name}s age is {self.age}"

# # ================== Building Spheres =================
# import math

# class Sphere:
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

# =============== Dynamic Classes ==================
# import re

# def class_name_changer(cls, new_name):
#     if not re.match(r'^[A-Z][a-zA-Z0-9]*$', new_name):
#         raise ValueError("Invalid class name format")
        
#     cls.__name__ = new_name