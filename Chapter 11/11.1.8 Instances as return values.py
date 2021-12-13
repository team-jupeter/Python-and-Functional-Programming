class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def to_string(self):
        return "({0}, {1})".format(self.x, self.y)

    def __str__(self): # All we have done is renamed the method
        return "({0}, {1})".format(self.x, self.y)

def midpoint(p1, p2):
    """ Return the midpoint of points p1 and p2 """
    mx = (p1.x + p2.x)/2
    my = (p1.y + p2.y)/2

    return Point(mx, my)

p = Point(3, 4)
q = Point(5, 12)
r = midpoint(p, q)
r # (4.0, 8.0)


def halfway(self, target):
    """ Return the halfway point between myself and the target """
    mx = (self.x + target.x)/2
    my = (self.y + target.y)/2
    return Point(mx, my)

p = Point(3, 4)
q = Point(5, 12)
r = p.halfway(q)
r # (4.0, 8.0)

print(Point(3, 4).halfway(Point(5, 12))) # (4.0, 8.0)