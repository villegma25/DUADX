import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)


radius_input = float(input("Insert the circle radius: "))
circle = Circle(radius_input)
print("Area of the circle:", circle.get_area())