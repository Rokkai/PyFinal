
print("We will be determining the characteristics of a rectangle.\n")
userInputType = str(raw_input("Will your inputs be (c)oordinates or (m)easurements?\nInput c or m"))

if (userInputType == "m"):
    print("You chose to enter measurements\n")
    l=float(raw_input("Please enter the length\n"))
    w=float(raw_input("Please enter the width\n"))
elif (userInputType == "c"):
    print("You chose to enter coordinates\n")
    x1=float(raw_input("x1="))
    y1=float(raw_input("y1="))
    x2=float(raw_input("x2="))
    y2=float(raw_input("y2="))

    p1=(x1,y1)
    p2=(x2,y2)





class Rectangle():
    """Takes input types determine by initial user choice and calculates the characteristics of a rectangle"""
    if (userInputType == "m"):

        def __init__(self,l,w):
            """if the user chose to input measurements, the class accepts length and width inputs"""
            self.length=l
            self.width=w

        def area(self):
            """returns the area of a rectangle given the user input length and width"""
            return self.length*self.width

        def perimeter(self):
            """returns the perimeter of the perimeter give the user input length and width"""
            return self.length*2+self.width*2

    elif(userInputType == "c"):
        def __init__(self,p1,p2):
            self.TopLeft=p1
            self.BottomRight=p2

        def length(self):
            """returns the length of the rectangle"""
            return self.BottomRight[0]-self.TopLeft[0]

        def width(self):
            """returns the width of the rectangle"""
            return self.TopLeft[1]-self.BottomRight[1]

        def area(self):
            """returns the perimeter of the area give the calculated length and width"""
            return self.length()*self.width()

        def perimeter(self):
            """returns the perimeter of the perimeter give the calculated length and width"""
            return self.length()*2+self.width()*2

if (userInputType=="c"):
    rpLength=Rectangle(p1,p2).length()
    rpWidth=Rectangle(p1,p2).width()
    rpArea=Rectangle(p1,p2).area()
    rpPerimeter=Rectangle(p1,p2).perimeter()
    print("Perimeter: " + str(rpPerimeter))
    print("Area: " + str(rpArea))
if (userInputType=="m"):
    rArea = Rectangle(l,w).area()
    rPerimeter = Rectangle(l,w).perimeter()
    print("Area: " + str(rArea))
    print("Perimeter: " + str(rPerimeter))


