
# 10. PRACTICAL TASKS / [GITHUB] [OUTSIDE]

#Tasks
#---------------------------------------------------------

# I. Ball-super-ball
class Ball(object):
    # your code goes here
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type
        
    def ballType(self):
        return f'{self.ball_type}'
    
ball1 = Ball()        
ball2 = Ball("super")  


#---------------------------------------------------------

# II. Color-ghost
import random

class Ghost:
    def __init__(self):
        dict_colors = {0: "white", 1: "yellow", 2: "purple", 3: "red"}
        self.color = random.choice(dict_colors)
        

#---------------------------------------------------------

# III. Basic-subclasses-Adam-and-Eve
def God():
    human = Human()
    human.paradise[0] = Man('Adam')
    human.paradise[1] = Woman('Eva')
    return human.array()


class Human():

    def __init__(self, paradise = list('ab')):
        self.paradise = paradise
        
    def array(self):
        return self.paradise

class Man(Human):

    def __init__(self, man):
        self.man = man
          
class Woman(Human): 
    
    def __init__(self, woman):
        self.woman = woman
print(God())
#---------------------------------------------------------
        
# IV. Classy-classes  
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @property
    def info(self):
        return f"{self.name}s age is {self.age}"

#---------------------------------------------------------

# V. Building Spheres
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
        volume = lambda volume : round(4/3 * math.pi *  self.radius**3, 5)
        return volume(None)
    
    def get_surface_area(self):
        surface_are = lambda surface_area : round(4*math.pi *  self.radius**2, 5)
        return surface_are(None)
    
    def get_density(self):
        get_density = lambda get_density : round(self.mass / (4/3 * math.pi *  self.radius**3),5)
        return get_density(None)

#---------------------------------------------------------

# VI. Dynamic Classes
def class_name_changer(cls, new_name):
    if not new_name[0].isupper() or not new_name.isalnum():
        raise ValueError("Invalid class name format")
    cls.__name__ = new_name
