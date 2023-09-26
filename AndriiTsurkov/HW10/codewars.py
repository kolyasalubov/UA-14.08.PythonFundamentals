# # I. Ball-super-ball
# class Ball(object):
#     def __init__(self, ball_type = "regular"):
#         self.ball_type = ball_type

# ball1 = Ball()
# ball2 = Ball("super")
# print(ball1.ball_type)  #=> "regular"
# print(ball2.ball_type)  #=> "super"


# II Color-ghost
# class Ghost(object):
#     def __init__(self):
#         from random import randint
#         color = ["white", "yellow", "purple", "red"]
#         self.color = color[randint(0,3)]

# ghost = Ghost()
# print(ghost.color)


# III. Basic-subclasses-Adam-and-Eve
# class Human():
#     pass
# class Man(Human):
#       pass
# class Woman(Human):
#       pass
# def God():
#     return [Man(), Woman()]


# IV. Classy-classes
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.info=f"{name}s age is {age}"

# a = Person("Igor", 44)
# print(a.info)


# V. Building Spheres
# class Sphere(object):
#     def __init__(self, radius, mass):
#         from math import pi
#         self.radius = radius
#         self.mass = mass
#         self.volume = 4 / 3 * pi * self.radius ** 3
#         self.surface_area = 4 * self.radius ** 2 * pi
#         self.density = self.mass/self.volume

#     def get_radius(self):
#         return self.radius
    
#     def get_mass(self):
#         return self.mass
    
#     def get_volume(self):
#         return  round(self.volume, 5)

#     def get_surface_area(self):
#         return round(self.surface_area, 5)

#     def get_density(self):
#         return round(self.density, 5)
    
# ball = Sphere(2,50)
# print(ball.get_radius()) #->       2
# print(ball.get_mass()) #->         50
# print(ball.get_volume()) #->       33.51032
# print(ball.get_surface_area()) #-> 50.26548
# print(ball.get_density()) #->      1.49208


# Dynamic Classes
# class MyClass:
#     pass

# def name_validity_sring(sring):
#     import re
#     pattern_string = r'^[A-Z][a-zA-Z0-9_]{1,}*$'
#     pattern = re.compile(pattern_string) 
#     return bool(pattern.match(sring))

# def class_name_changer(cls, new_name):
#     if name_validity_sring(new_name):
#         cls.__name__ = new_name
#         return cls.__name__
#     return "Error" 

# print(MyClass.__name__, "\n")
# print(class_name_changer(MyClass, "GteefGhhk"))
# print(MyClass.__name__)


