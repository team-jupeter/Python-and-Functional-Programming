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

p = Point(3, 4)
print(p.to_string()) # (3, 4)

str(p) # '<__main__.Point object at 0x01F9AA10>'
print(p) # '<__main__.Point object at 0x01F9AA10>'

# Code 2
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

str(p) # Python now uses the __str__ method that we wrote.
# (3, 4)
print(p) # (3, 4)

