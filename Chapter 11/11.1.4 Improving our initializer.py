class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

p = Point()
p.x = 7
p.y = 6

###
class Point:
    """ Point class represents and manipulates x,y coords. """
    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    # Other statements outside the class continue below here.

p = Point(4, 2)
q = Point(6, 3)
r = Point() # r represents the origin (0, 0)
print(p.x, q.y, r.x) # 4 3 0