class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y



p1 = Point(3, 4)
p2 = Point(3, 4)
p1 is p2 # False

def same_coordinates(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)

same_coordinates(p1, p2) # True

p = Point(4, 2)
s = Point(4, 2)
print("== on Points returns", p == s) # False
# By default, == on Point objects does a shallow equality test

a = [2, 3]
b = [2, 3]
print("== on lists returns", a == b) #  True
# But by default, == does a deep equality test on lists

print(id(p))
print(id(s))
print(id(a))
print(id(b))
