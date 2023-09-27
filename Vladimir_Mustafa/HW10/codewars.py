#Regular Ball Super Ball

class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


#Color Ghost

import random

class Ghost:
    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]

        self.color = random.choice(colors)

#Building Spheres

import math

class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = (4 / 3) * math.pi * (self.radius ** 3)
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * math.pi * (self.radius ** 2)
        return round(surface_area, 5)

    def get_density(self):
        density = self.mass / ((4 / 3) * math.pi * (self.radius ** 3))
        return round(density, 5)

ball = Sphere(2, 50)
print(ball.get_radius())
print(ball.get_mass())
print(ball.get_volume())
print(ball.get_surface_area())
print(ball.get_density())