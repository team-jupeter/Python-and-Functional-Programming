import copy
class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

def same_coordinates(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)

p1 = Point(3, 4)
p2 = copy.copy(p1)
p1 is p2 # False
same_coordinates(p1, p2) # True


class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, position, w, h):
        """ Initialize rectangle at position, with width w, height h """
        self.corner = position
        self.width = w
        self.height = h

b1 = Rectangle(Point(0, 0), 100, 200)
b2 = copy.deepcopy(b1)

