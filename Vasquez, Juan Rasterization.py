
import graphics
import math
win = graphics.GraphWin("Canvas", 500, 500)

def fillPixel(x, y, color):
    """
    This function colors a single pixel on the screen.  You will call this function,
    as you fill in your shapes one pixel at a time.
    See rasterize function in Square class for an example of how to call.
    Do not change this method!
    Parameters:
        1. x - x-coordinate of screen to shade
        2.  y - y coordinate of screen to shade
        3.  color - color pixel will be shaded; typical colors like 'red', 'blue', 'purple', etc. should be supported
    Return: None 
    """
    win.plotPixel(x, y, color)


#superclassShape, which stores the z depth value of a shape
#shapes with smaller z values are in front of shapes with larger z values
class Shape(object):
    """
    Superclass that stores the depth value z of a shape.
    A shape with a smaller z value is in front of (and should appear on top of) a shape with larger z value.
    """
    def __init__(self, z):
        """
        Shape constructor.
        Paramters:
        1. z - depth value of shape
        Return: None 
        """
        self.z = float(z) 


    def getZ(self):
        """
        Accessor method for z value of a shape.
        Parameters: None
        Return:  None 
        """
        return self.z


    def rasterize(self):
        """
        Superclass rasterize method will raise an exception if it is ever called.
        An "exception" is a special name for an error in programming.
        It will cause the program to crash, unless you do special processing.
        Your subclasses should override this method, so this method in the superclass should never be called. 
        """
        raise AttributeException("Subclasses should override this method.")
        



class Square(Shape):
    """
    Subclass of Shape that represents a square. 
    """
    def __init__(self, cornerX, cornerY, width, z, color):
        """
        Square constructor.
        Parameters:
        1.  cornerX - x-coordinate of top left corner
        2.  cornerY - y-coordinate of top left corner
        3.  width - side length of the square in pixels
        4.  z - depth value of square
        5.  color - fill color of the square 
        """
        self.cornerX = int(cornerX)
        self.cornerY = int(cornerY)
        self.width = int(width)
        self.color = color 
        Shape.__init__(self, z)  #call the constructor of the superclass

    def __str__(self):
        """
        String representation of a square
        Parameters: None
        Return:  Screen attributes of the square
        """
        return 'Square with corner (' + str(self.cornerX) + ',' + str(self.cornerY)  + '), width ' + str(self.width) + " and depth " + str(self.z)

    def rasterize(self):
        """
        Draw a square to the screen one pixel at a time.
        Parameters: None
        Return:  None 
        """
        #two for loops can be used to go through all the pixels inside the square
        for x in range(self.cornerX, self.cornerX+self.width):
            for y in range(self.cornerY, self.cornerY + self.width):
                #each pixel inside the square gets "turned on" with a call to fillPixel
                fillPixel(x, y, self.color)

class Circle(Shape):
    """
    Subclass of Shape that represents a circle. 
    """
    def __init__(self, centerX, centerY, radius, z, color):
        """
        Circle constructor.
        Parameters:
        1.  centerX - x-coordinate of circle center
        2.  centerY - y-coordinate of circle center
        3.  radius - radius length of the circle in pixels
        4.  z - depth value of circle
        5.  color - fill color of the circle
        """
        self.centerX = int(centerX)
        self.centerY = int(centerY)
        self.radius = int(radius)
        self.color = color 
        Shape.__init__(self, z)  #call the constructor of the superclass

    def __str__(self):
        """
        String representation of a circle
        Parameters: None
        Return:  Screen attributes of the circle
        """
        return 'Circle with center (' + str(self.centerX) + ',' + str(self.centerY)  + '), radius ' + str(self.radius) + " and depth " + str(self.z)

    def rasterize(self):
        """
        Draw a circle to the screen one pixel at a time.
        Parameters: None
        Return:  None 
        """
        #two for loops can be used to go through all the pixels inside the circle
        for x in range(self.centerX-self.radius, self.centerX+self.radius):
            for y in range(self.centerY-self.radius, self.centerY + self.radius):
                distance = math.sqrt(((x - self.centerX)**2) + ((y - self.centerY)**2))
                #checks to see if the pixels are within range of the center
                if distance <= self.radius:
                    #each pixel inside the circle gets "turned on" with a call to fillPixel
                    fillPixel(x, y, self.color)

class Rectangle(Shape):
    """
    Subclass of Shape that represents a rectangle. 
    """
    def __init__(self, cornerX, cornerY, width, length, z, color):
        """
        Rectangle constructor
        Parameters:
        1.  cornerX - x-coordinate of top left corner
        2.  cornerY - y-coordinate of top left corner
        3.  width - side width of the rectangle in pixels
        4.  length - side length of the rectangle in pixels
        5.  z - depth value of rectangle
        6.  color - fill color of the rectangle 
        """
        self.cornerX = int(cornerX)
        self.cornerY = int(cornerY)
        self.width = int(width)
        self.length = int(length)
        self.color = color 
        Shape.__init__(self, z)  #call the constructor of the superclass

    def __str__(self):
        """
        String representation of a rectangle
        Parameters: None
        Return:  Screen attributes of the rectangle
        """
        return 'Rectangle with corner (' + str(self.cornerX) + ',' + str(self.cornerY)  + '), width ' + str(self.width) + '), length ' + str(self.length) + " and depth " + str(self.z)

    def rasterize(self):
        """
        Draw a rectangle to the screen one pixel at a time.
        Parameters: None
        Return:  None 
        """
        #two for loops can be used to go through all the pixels inside the rectangle
        for x in range(self.cornerX, self.cornerX+self.width):
            for y in range(self.cornerY, self.cornerY + self.length):
                #each pixel inside the rectangle gets "turned on" with a call to fillPixel
                fillPixel(x, y, self.color)

class Triangle(Shape):
    """
    Subclass of Shape that represents a triangle. 
    """
    def __init__(self, v1x, v1y, v2x, v2y, v3x, v3y, z, color):
        """
        Triangle constructor
        Parameters:
        1.  v1x - x-coordinate of vertex 1
        2.  v1y - y-coordinate of vertex 1
        3.  v2x - x-coordinate of vertex 2
        4.  v2y - y-coordinate of vertex 2
        5.  v3x - x-coordinate of vertex 3
        6.  v3y - y-coordinate of vertex 3
        7.  z - depth value of triangle
        8.  color - fill color of the triangle 
        """
        self.v1x = int(v1x)
        self.v1y = int(v1y)
        self.v2x = int(v2x)
        self.v2y = int(v2y)
        self.v3x = int(v3x)
        self.v3y = int(v3y)
        self.color = color 
        Shape.__init__(self, z)  #call the constructor of the superclass

    def __str__(self):
        """
        String representation of a triangle
        Parameters: None
        Return:  Screen attributes of the triangle
        """
        return 'Triangle with vertex 1 at (' + str(self.v1x) + ',' + str(self.v1y)  + '), vertex 2 at (' + str(self.v2x) + ',' + str(self.v2y)  + '), vertex 3 at (' + str(self.v3x) + ',' + str(self.v3y) + '),' + " and depth " + str(self.z)

    def rasterize(self):
        """
        Draw a triangle to the screen one pixel at a time.
        Parameters: None
        Return:  None 
        """
        #two for loops can be used to go through all the pixels in the triangle, but first we have to get the maximum and minimum possible x and y coordinates
        vxList = [self.v1x, self.v2x, self.v3x]
        vyList = [self.v1y, self.v2y, self.v3y]
        vxList.sort()
        vyList.sort()
        for x in range(vxList[0],vxList[2]):
            for y in range(vyList[0],vyList[2]):
                v12 = (self.v2x - self.v1x)*(y - self.v1y) - (x - self.v1x)*(self.v2y - self.v1y)
                v23 = (self.v3x - self.v2x)*(y - self.v2y) - (x - self.v2x)*(self.v3y - self.v2y)
                v31 = (self.v1x - self.v3x)*(y - self.v3y) - (x - self.v3x)*(self.v1y - self.v3y)
                #checks to see if pixel is within the boundaries set by the three possible pairs of verteces
                if(v12>=0 and v23>=0 and v31>=0) or (v12<0 and v23<0 and v31<0):
                    #each pixel inside the rectangle gets "turned on" with a call to fillPixel
                    fillPixel(x, y, self.color)

class World(object):
    """
    World class that rasterizes and keeps track of all shapes on the screen. 
    """
    def __init__(self):
        """
        World constructor
        Parameters: None
        Return: None
        """
        self.shapes = []

    def addShape(self, shape):
        """
        Populates the world list
        Parameters:
        1. shape - takes the shape input and inserts it correctly into the list
        Return:  None
        """
        self.shapes.append(shape)
        k = 0
        while shape.getZ() < self.shapes[k].getZ():
            k+=1
        else:
            self.shapes.remove(shape)
            self.shapes.insert(k, shape)
        
    def rasterizeWorld(self):
        """
        Goes through the shapes in the list and rasterizes them one at a time, then prints
        Parameters: None
        Return:  None 
        """
        for i in range(len(self.shapes)):
            self.shapes[i].rasterize()
            print(self.shapes[i])

def main():
    #Defining a "main" method is a convention from the Java programming language.
    #All test-code should be defined in here. 
    w = World()
    w.addShape(Square(100, 100, 50, 150, 'red'))
    w.addShape(Rectangle(100, 100, 20, 100, 100, 'yellow'))
    w.addShape(Circle(100, 100, 30, 200, 'green'))
    w.addShape(Triangle(10, 10, 390, 390, 10, 390, 300, 'blue'))
    w.rasterizeWorld()
    win.getMouse()
    win.close()

main()  #execute the main method 




