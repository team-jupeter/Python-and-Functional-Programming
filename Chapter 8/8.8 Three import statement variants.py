import math
x = math.sqrt(10)

from math import cos, sin, sqrt
x = sqrt(10)

from math import * # Import all the identifiers from math,
# adding them to the current namespace.
x = sqrt(10) # Use them without qualification.

import math as m
m.pi # 3.141592653589793


######## Error
def area(radius):
    import math
    return math.pi * radius * radius

x = math.sqrt(10) # This gives an error