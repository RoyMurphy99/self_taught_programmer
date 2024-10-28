"""
chapter 12 exercises.
Roy Murphy 28/09/2024.
"""

import math

# exercise 1
class Apple():
    def __init__(self, colour, weight, variety, country):
        self.colour = colour
        self.weight = weight
        self.variety = variety
        self.country = country

a1 = Apple("red", 12, "granny smiths", "England")
print(a1)
print(a1.colour)
print(a1.weight)
print()

# exercise 2
class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi*(self.radius**2)

c1 = Circle(10)
print(c1.area())
print()

# exercise 3
class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5*self.base*self.height

t1 = Triangle(2,4)
print(t1.area())
print()

# exercise 4
class Hexagon():
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 6*self.side

h1 = Hexagon(7)
print(h1.perimeter())
print()

    
        


