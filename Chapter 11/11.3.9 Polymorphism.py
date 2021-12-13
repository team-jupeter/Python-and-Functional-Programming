class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __rmul__(self, other): # scalar multiplication
        return Point(other * self.x, other * self.y)

def multadd (x, y, z):
    return x * y + z

multadd (3, 2, 1) # 7
p1 = Point(3, 4)
p2 = Point(5, 7)
print(multadd (2, p1, p2)) # (11, 15)
print(multadd (p1, p2, 1)) # 44

