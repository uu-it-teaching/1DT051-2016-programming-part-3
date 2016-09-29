'''This module demonstrates the checkKey() and checkMouse() methods
and the autoflush property of graphics.py version 4.3.

Using checkKey() and checkMouse() allows you to check for key presses
and mouse clicks without blocking the program.

getKey()
   Wait (blocks) for user to press a key and return it as a string.

checkKey()
   Return last key pressed or None if no key pressed since
   last call.

getMouse()
   Wait (block) for mouse click and return Point object representing
   the click.

checkMouse()
   Return last mouse click or None if mouse has
   not been clicked since last call.

The program will start to execute in the main() function. Have a look
at the code in the main() function to see examples of how to use the
non-blocking checkKey() and checkMouse() functions. In main() you will
also see how to change the autoflush property of a GraphWin object.

To run this program from the Linux or Unix shell:

  prompt> python demo.py

You will now see a blue circle in the middle of the window.

Press space to randomly change the color of the circle.

Press mouse inside window to create a new rectangle with a random
color. All created rectangles will start to move (shake) randomly.

Press the c key to center all rectangles at the center of the blue
circle.

Press the f key to flip the autoflush property of the graphic
window.

  * The default is to autoflush to be turned on (True). Now updates on
    the window are done after each action (update of a drawn
    object). This may cause graphics intensive programs to appear
    sluggish.

  * Turning off autoflush (False) causes updates to happen during idle
    periods or when flush() is called explicitly. This will make
    graphics intensive programs to run more smoothly.

Keep adding new rectangles. Flip autoflush by pressing the f key. Look
at the Linux/Unix shell for status messages.  As the number of
rectangles increases the difference between turning autoflush on
(True) and off (False) will radically change.

'''

__author__  = "Karl Marklund"
__email__   = "karl.marklund@it.uu.se"
__version__ = 0.1
__date__    = "2014-10-14"

from graphics import *
import random
import time

def randomColorFill(shape):
    '''Set the fill color of shape to a random color.

    Arguments:

    shape :: Circle or Rectangle

    Returns :: None

    Side effects:

    Set the color of shape to a random color.

    '''
    # Pick a random color.
    color = random.choice(["red", "blue", "green", "pink", "orange", "RoyalBlue1", "green3"])

    shape.setFill(color)

def randomColoredRectangle(p):
    '''Creates and returns a rectangle 20 units wide and 20 units
    high centered at the point p.

    Arguments:

    p :: Point

    Returns :: Rectangle
    '''

    r = Rectangle(Point(0,0), Point(20, 20))
    r.setWidth(4)
    randomColorFill(r)
    r.move(p.getX() - 10, p.getY() - 10)

    return r

def randomMove(w, rs):
    '''Randomly moves each of the rectangles in rs.

    Arguments:

    w :: GraphWin

    rs :: list of Rectangle
    '''

    for r in rs:
        center = r.getCenter()
        x = center.getX()
        y = center.getY()

        dx = random.randint(-5, 5)
        dy = random.randint(-5, 5)

        # Only move r if new center point is within the bounds of w.

        if 0 < x + dx < w.getWidth() and 0 < y + dy < w.getHeight():
            r.move(dx, dy)

def moveAll(rs, p):
    '''Move all rectangles in rs such that they are centered at the point p.

    Arguments:

    rs :: list of Rectangle

    p :: Point

    Side effects:

    Changes the center point of all rectangles in rs to p.
    '''

    for r in rs:
        rc = r.getCenter()

        rx = rc.getX()
        ry = rc.getY()

        px = p.getX()
        py = p.getY()

        dx = px - rx
        dy = py - ry

        r.move(dx, dy)

def flipFlush(w):
    '''Flips the autoflush property of w.

    Arguments:

    w :: GraphWin

    Side effects:

    Flips the auotflush property of w.
    '''

    if w.autoflush:
        w.autoflush = False
    else:
        w.autoflush = True

    print "Autoflush = ", w.autoflush

def main():
    '''
    The main function. This is where the program starts to execute.
    '''

    # Create a window with a circle at the center.

    w = GraphWin("Graphics 4.3", 300, 300)

    c = Circle(Point(150, 150), 30)
    c.setFill("blue")
    c.setWidth(10)
    c.draw(w)

    # This list will store all rectangles.

    rs = []

    while True:

        # Randomly move all rectangles.
        randomMove(w, rs)

        # Check if user pressed a key or clicked the mouse. Note, both
        # checkKey() and checkMouse() will return None if no key or
        # mouse click has been detected since last check.

        k = w.checkKey()
        p = w.checkMouse()

        if k:
            # If key pressed print "value" of key and its type.
            print k, type(k)

        if k == "space":
            # If user pressed the space key, randomly change the color of c.
            randomColorFill(c)
        elif k == "f":
            # If the user pressed the f key, flip the autoflush property of w.
            flipFlush(w)
        elif k == "c":
            moveAll(rs, c.getCenter())

        if p:
            # If the user clicked the mouse, print the x- and y-value
            # of the point clicked.
            print "Mouse clicked at x = ", p.getX(), " y = ", p.getY()

            # Create and draw a random colored rectangle centered at point p.
            r = randomColoredRectangle(p)
            r.draw(w)

            # Append the new rectangle to the list of rectangles.
            rs.append(r)


        if not w.autoflush:
            # If no autoflush, manually flush to re-draw all objects.
            w.flush()


# Call the main() function if you do unix> python demo.py
if __name__ == "__main__":
    main()
