"""
chapter 14 of self taught programmer.
Roy P Murphy 6th october 2024
"""

# exercise 1
class Shape():
    def what_am_i(self):
        print("I am a shape")
        
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return 4*self.side

    def change_size(self, change):
        self.side = self.side + change

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return self.length*2 + self.width*2

sq1 = Square(2)
print(sq1.calculate_perimeter())

rc1 = Rectangle(4,2)
print(rc1.calculate_perimeter())

print("")


# exercise 2
sq1.change_size(2)
print(sq1.side)
print("")


# exercise 3
sq2 = Square(3)
rc2 = Rectangle(5,4)

print(sq2.what_am_i())
print(rc2.what_am_i())

print("")


# exercise 4

class Rider():
    def __init__(self, name):
        self.name=name

class Horse():
    def __init__(self, name, rider):
        self.name = name
        self.rider = rider

r1 = Rider("Horace")
h1 = Horse("Champion",r1)

print(h1.rider.name)
print(h1.name)

print("")



        
