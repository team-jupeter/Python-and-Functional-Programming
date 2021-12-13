class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

p = Point(3, 4)
p.x # 3
p.y # 4
p.distance_from_origin() # 5.0
q = Point(5, 12)
q.x # 5
q.y # 12
q.distance_from_origin() # 13.0
r = Point() #
r.x # 0
r.y # 0
r.distance_from_origin() # 0.0