# 5.2.3 Tuples as return values
import math

def circle_stats(r):
    """ Return (circumference, area) of a circle of radius r """
    circumference = 2 * math.pi * r
    area = math.pi * r * r
    return (circumference, area)