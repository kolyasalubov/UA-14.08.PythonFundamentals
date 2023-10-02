######  1. Ball super ball ###########

class Ball(object):
    def __init__ (self, ball_type = 'regular'):
        self.ball_type = ball_type
    def get_ball(self):
        return self.ball_type
    
ball1 = Ball()
ball2 = Ball("super")
print(ball1.ball_type)
print(ball2.ball_type)

############## 2. Сolor ghost ##########################

# import random
# class Ghost(object):
#     def __init__(self):
#         self.color = random.choice(["white", "yellow", "purple", "red"])     

# ghost = Ghost()
# print(ghost.color)


########## 3. Basic subclasses - Adam and Eve ##################

# class Human:
#    def __init__(self):
#       pass

# class Man(Human):
#    def __init__(self, name = "Adam"):
#       self.name = name
      

# class Woman(Human):
#    def __init__(self, name = "Eva"):
#       self.name = name

# def God():
#     a = Man()
#     e = Woman()
#     return [a, e]

# print(God())


############# 4. Classy Classes ####################

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.info = f"{self.name}'s age is {self.age}"
#     def get_info(self):
#         return self.info
        
# p = Person("Samanta", 23)
# print(p.get_info())

############## 5. Building Spheres ##################


# class Sphere(object):
#     """
#     Some calculations with a sphere
#     """
#     pi = 3.14159265358979
#     def __init__(self, radius, mass):
#         self.raduis = float(radius)
#         self.mass = float(mass)
#         self.volume = 4 * Sphere.pi * self.raduis ** 3 / 3
#         self.area = 4 * Sphere.pi * self.raduis ** 2
#         self.density = self.mass / self.volume
#     def get_radius(self) :
#         return self.raduis
#     def get_mass(self):
#         return self.mass
#     def get_volume(self):
#         return round(self.volume, 5)
#     def get_surface_area(self):
#         return round(self.area, 5)
#     def get_density(self):
#         density = round(self.density, 5)
#         return density
    
# ball = Sphere(2,50)
# print(ball.get_radius())
# print(ball.get_mass())
# print(ball.get_volume()) 
# print(ball.get_surface_area())
# print(ball.get_density())


############ 6. Python's Dynamic Classes ######################

# class MyClass:
#     pass

# def class_name_changer(cls, new_name):
#     if new_name[0].isupper() and new_name.isalnum():
#         cls.__name__ = new_name
#     else:
#         raise Exception("The first letter of class has to be upper!")

# myObject = MyClass()
# print(MyClass.__name__)

# class_name_changer(MyClass, "FefulClass")
# print(MyClass.__name__)

# class_name_changer(MyClass, "UsefulClass2")
# print(MyClass.__name__)

# class_name_changer(MyClass, "sefulClass")
# print(MyClass.__name__)
    
































