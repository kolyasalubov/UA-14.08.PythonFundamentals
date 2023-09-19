#First task to create class Ball
class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type
# Example 
regular_ball = Ball()
special_ball = Ball("special")

print(regular_ball.ball_type)  
print(special_ball.ball_type)  
print("-------------------------")

#Second task to create a class Ghost
import random
class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

# Example 
ghost1 = Ghost()
ghost2 = Ghost()

print(ghost1.color) 
print(ghost2.color) 
print("---------------------------")

#Third task to create method for representing Adam and Eve).
class Human:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Man(Human):
    def __init__(self, name):
        super().__init__(name, "man")

class Woman(Human):
    def __init__(self, name):
        super().__init__(name, "woman")

def God():
    adam = Man("Adam")
    eve = Woman("Eve")
    return [adam, eve]

paradise = God()
print(isinstance(paradise[0], Man))
print("------------------------")

#Fourth task 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"{self.name}s age is {self.age}"
#Fifth task
from math import pi

class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        self.volume = round(4 * pi * radius**3 / 3, 5)
        self.surface_area = round(4 * pi * radius**2, 5)
        self.density = round(self.mass / self.volume, 5)
    
    def __getattr__(self, name):
        return lambda: getattr(self, name[4:])
#Six task
import re
def class_name_changer(cls, new_name):
    if re.match(r'^[A-Z][a-zA-Z0-9-_]*$', new_name):
        cls.__name__ = new_name
    else:
        raise Exception('Invalid Class Name')
