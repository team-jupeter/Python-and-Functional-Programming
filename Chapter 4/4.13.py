# 4.13 Composition
import math

def distance(x1, y1, x2, y2):
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
def area(radius):
    return 3.14*radius**2

def area_of_circle(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result

def area_of_circle(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

# ##### Be functional
# # Currying
# def change(b, c):
#     def a(*x):
#         return b(c(*x))
#     return a

# area_of_circle = change(area, distance)
# print(area_of_circle(1, 2, 4, 6))