import random
import re

# Task1

class Ball(object):
    def __init__(self, name='regular'):
        self.ball_type = name


ball1 = Ball()
print(ball1.ball_type)


# Task2
class Ghost(object):
    def __init__(self):
        self.color_choice = random.choice(["white", "yellow", "purple", "red"])


ghost1 = Ghost()
print(ghost1.color_choice)


# Task3
def God():
    return [Man(), Woman()]


class Human(object):
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


# Task4
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{name}s age is {age}"


# Task6
from math import pi


# Task7
class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        self.volume = round(4 * pi * radius ** 3 / 3, 5)
        self.surface_area = round(4 * pi * radius ** 2, 5)
        self.density = round(self.mass / self.volume, 5)

    def __getattr__(self, name):
        return lambda: getattr(self, name[4:])


# Task8

def class_name_changer(cls, new_name):
    if not re.search('^([A-Z][a-z0-9]*)+$', new_name):
        raise ValueError('{!r} is invalid class name'.format(new_name))
    cls.__name__ = new_name
