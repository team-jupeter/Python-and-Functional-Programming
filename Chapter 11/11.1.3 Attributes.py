class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

p = Point() # Instantiate an object of type Point
q = Point() # Make a second point

p.x = 3
p.y = 4

print(p.y) # 4
x = p.x
print(x) # 3

print(f"(x={p.x}, y={p.y})")
distance_squared_from_origin = p.x * p.x + p.y * p.y