import math
import cmath
"""Calculate all vlaues for right triangles when the sides are no greater than 20"""

#sides
a=int(raw_input("Input side -a-. Value must be under 20"))
b=int(raw_input("Input side -b-. Value must be under 20"))
c=None

#angles
A=None
B=None
C=90

def findHypo():
    """Return the hypotenuse of a triangle."""
    x=(a*a)+(b*b)
    c=math.sqrt(x)
    return c

def findAngleA():
    """Return the angle -A- given all sides known."""
    A=math.asin(a/c)
    return A

def findAngleB():
    """Return the angle -B- given all sides known."""
    B=math.asin(b/c)
    return B


c = findHypo()
A = findAngleA()
B = findAngleB()


def printFunction():
    """Print all sides and angles."""
    print("sides")
    print(a)
    print(b)
    print(c)
    print()
    print("angles")
    print(round(math.degrees(A),2))
    print(round(math.degrees(B),2))
    print(C)



printFunction()
