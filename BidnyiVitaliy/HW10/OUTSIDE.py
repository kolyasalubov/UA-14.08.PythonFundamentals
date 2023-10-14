#Ball-super-ball
# class Ball():
#   def __init__(self, ball_type="regular"):
#     self.ball_type = ball_type


#Color-ghost
# import random

# class Ghost(object):
#     def __init__(self):
#         self.colors = ['white', 'yellow', 'red', 'purple']
#         self.color = random.choice(self.colors)


#Basic-subclasses-Adam-and-Eve
# class Human:
#     pass

# class Man(Human):
#     pass

# class Woman(Human):
#     pass

# def God():
#     return [Man(), Woman()]


#Classy-classes
# class Person:
#     def __init__(self, name, age):
#         self.info = f"{name}s age is {age}"


#Building Spheres
# from math import pi

# class Sphere(object):
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass
#         self.volume = round(4 * pi * radius**3 / 3, 5)
#         self.surface_area = round(4 * pi * radius**2, 5)
#         self.density = round(self.mass / self.volume, 5)
    
#     def __getattr__(self, name):
#         return lambda: getattr(self, name[4:])



#Dynamic Classes
# def class_name_changer(cls, new_name):
#     assert new_name[0].isupper() and new_name.isalnum()
#     cls.__name__ = new_name        