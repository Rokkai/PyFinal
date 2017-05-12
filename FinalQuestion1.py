"""Python Final: Question 1"""
import math

class Circle():
    def __init__(self,r):
        """define what's given-- the radius."""
        self.radius=r

    def area(self):
        """return the calculation of pi r squared."""
        return self.radius**2*math.pi

    def circumference(self):
        """return the calculation of 2*pi*r."""
        return 2*math.pi*self.radius

    def diameter(self):
        """return the calculation of the diameter"""
        return 2*self.radius


userInput=raw_input("Give a radius for a circle")

convertedInput = int(userInput)

newCircle = Circle(convertedInput)

print("Diameter: " + str(newCircle.diameter()))
print("Area: " + str(newCircle.area()))
print("Circumference: " + str(newCircle.circumference()))