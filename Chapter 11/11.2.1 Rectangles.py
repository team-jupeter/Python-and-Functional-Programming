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

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, position, w, h):
        """ Initialize rectangle at position, with width w, height h """
        self.corner = position
        self.width = w
        self.height = h

    def __str__(self):
        return f"({self.corner}, {self.width}, {self.height})"

box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10) # In my video game
print("box: ", box) # box: ((0, 0), 100, 200)
print("bomb: ", bomb) # bomb: ((100, 80), 5, 10)
