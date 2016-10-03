#! /usr/bin/python

'''
Information Technology (1DT051) 2016

Programming assignment 3.

'''


# Import all the necessary functions and classes for creating graphics.
from graphics import *

# To calculate the distance between two points, math.sqrt() might be useful.
import math

# You will need to use random.choice() and random.randint().
import random


# ===========================================================================
#
#        You don't need to add or modify any of the functions below.
#
# ===========================================================================

def randomPoint(p1, p2):
    '''
    Arguments:

    p1 :: Point
    p2 :: Point

    Returns :: Point

    Returns a random point inside the rectangle defined by the upper
    left corner p1 and lower right corner p2.
    '''

    x = random.randint(p1.getX(), p2.getX())
    y = random.randint(p1.getY(), p2.getY())

    return Point(x, y)

def randomGrayFill(c):
    '''
    Arguments:

    c :: Circle

    Returns :: None

    Side effects:

    Set the color of c to a random gray color.

    '''

    # Pick a random gray color.
    gray = random.choice(["gray5", "gray10","gray20", "gray30", "gray40", "gray50", "gray60", "gray70"])

    c.setFill(gray)

def randomColorFill(shape):
    '''
    Arguments:

    shape :: Circle or Rectangle

    Returns :: None

    Side effects:

    Set the color of shgape to a random color.

    '''
    # Pick a random color.
    color = random.choice(["red", "blue", "green", "pink", "orange", "RoyalBlue1", "green3"])

    shape.setFill(color)

def randomGrayCircle(p1, p2):
    '''
    Arguments:

    p1 :: Point
    p2 :: Point


    Returns :: Circle

    Returns a circle with a random radius between 10 and 40 units with
    a random center point inside the bounding box defined by the upper
    left corner p1 and the lower right corner p2 such that the whole circle fits inside the bounding box.
    '''

    r = random.randint(10, 40)
    c = Circle(randomPoint(Point(p1.getX() + r, p1.getY() + r), Point(p2.getX() - r, p2.getY() - r)), r)

    randomGrayFill(c)

    return c


def inRectangle(p, r):
    '''
    Arguments:

    p :: Point
    r :: Rectangle

    Returns :: Bool

    Returns True if p is inside r and otherwise returns False.
    '''

    p1 = r.getP1()
    p2 = r.getP2()

    smallx = min(p1.getX(), p2.getX())
    bigx   = max(p1.getX(), p2.getX())

    smally = min(p1.getY(), p2.getY())
    bigy   = max(p1.getY(), p2.getY())

    return p.getX() > smallx and p.getX() < bigx and p.getY() > smally and p.getY() < bigy


# ===========================================================================
#
#        You must add or change code in the following functions.
#
# ===========================================================================


def main():
    '''
    The start-up main function. Creates a window with some graphics in
    it. Wait for mouse click inside the window.
    '''

    # Create a graphical window.
    w = GraphWin("Programmering 3", 300, 300)

    # Make a randomized background with 50 random gray circles.
    randomBackground(w, 50)


    # A red square centered in the window.

    r = Rectangle(Point(100, 100), Point(200, 200))
    # TODO: Make the rectangle red.
    r.draw(w)

    # A yellow circle centered inside the square. Use a random radius
    # between 25 and 40.

    radius = random.randint(25, 40)
    c = Circle(r.getCenter(), radius)
    # TODO: Make the circle yellow
    c.draw(w)

    while True:
        # Wait for mouse click
        p = w.getMouse()

        # Handle mouse click on Point p inside window w.
        handleClick(p, c, r)


def randomBackground(w, n):
    '''Arguments:

    w :: GraphWin object

    n :: int

    Returns :: None

    Side effects:

    Draws n random sized circles, each with a random gray color in
    window w.
    '''

    p1 = Point(0, 0)
    p2 = Point(w.getWidth(), w.getHeight())

    # TODO: You must add code here.

    # TIP: Use randomGrayCircle(p1, p2) inside a for-in loop.

def inCircle(p, c):
    '''
    Arguments:

    p :: Point
    c :: Circle

    Returns :: Bool

    Returns True if p is inside c and othterwise returns False.
    '''

    # TODO: You must add code here.


    return False # You must change this.


def handleClick(p, c, r):
    '''
    Arguments:

    p :: Point
    c :: Circle
    r :: Rectangle

    Side effects:

    If p is inside c, change the color of c randonly. If p is inside r
    but outsicde c, change the color of r randomly.

    '''

    print "Click on:"
    print "    x = ", p.getX()
    print "    y = ", p.getY()

    # TODO: You must add code here.

    # TIP: Use inCircle() and inRectangle().

    # TIP: Use randomColorFill() and move().


    return None


def move(p, shapes):
    '''
    Arguments:

    p :: Point

    shapes :: list of shapes (Circle, Rectangle etc).

    Returns :: None

    Side effects:

    Move the center point of each shape in shapes to p.
    '''

    dx = p.getX() - shapes[0].getCenter().getX()
    dy = p.getY() - shapes[0].getCenter().getY()

    print "    dx =", dx
    print "    dy =", dy

    for shape in shapes:
        # TODO: You must add code here.

        print "Shape moved"

    return None




'''
The code block below allow you to run the main() function directly
from the Linu-terminal simply by doing:

    linux> python assignment.py

Note that main() will not be run if you do import assignment from within a running python
process.  Then you need to do:

>>> import assignment
>>> assignment.main()

'''

if __name__ == "__main__":
    main()
