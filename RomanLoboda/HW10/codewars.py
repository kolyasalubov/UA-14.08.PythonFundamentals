# Task 1
class Ball(object):
    def __init__(self, type="regular"):
        self.ball_type = type


ball1 = Ball()
ball2 = Ball("super")
print(ball1.ball_type)
print(ball2.ball_type)

# Task 2
import random


class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


ghost = Ghost()
print(ghost.color)


# Task 3
def God():
    return [Man("Adam"), Woman("Eve")]


class Human:
    def __init__(self, name):
        self.name = name


class Man(Human):
    pass


class Woman(Human):
    pass


# Task 4
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"


# Task 5
import math


class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round(4 / 3 * math.pi * self.radius ** 3, 5)

    def get_surface_area(self):
        return round(4 * math.pi * self.radius ** 2, 5)

    def get_density(self):
        return round(self.mass / self.get_volume(), 5)


# Task 6
import re


def class_name_changer(cls, new_name):
    if re.match(r'^[A-Z][a-zA-Z0-9-_]*$', new_name):
        cls.__name__ = new_name
    else:
        raise Exception('Invalid Class Name')
