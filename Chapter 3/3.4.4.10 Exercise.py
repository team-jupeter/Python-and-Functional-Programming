import math
a = math.sqrt(2.0)
print(a, a*a)
print(a*a == 2.0)

# 1
for _ in range(1000):
    print("like Python's turtles!")

# 2
months = ['Janaury', 'Februray', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
'October', 'November', 'December']

for x in months:
    print(f'One of the months of the year is {x}')

# 3
# tess.left(3645) == tess.left(3645//360)

# 4
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# a
for _ in numbers:
    print(_)

# b
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

def print_num(numbers):
    for _ in numbers:
        print(_, "\t", _**2)

print_num(numbers)


# c
total = 0
for _ in numbers:
    total += _

#
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
print(sum(numbers))

# Functional 1
import functools
functools.reduce(lambda acc, x : acc + x, numbers, 0)

# Functional 2
from functools import reduce
sum = lambda numbers : reduce(lambda acc, x : acc + x, numbers, 0)
print(sum(numbers))



# d
import functools
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
sum = functools.reduce(lambda acc, x : acc * x, numbers, 1)
print(sum)

#
sum = lambda numbers : functools.reduce(lambda acc, x : acc * x, numbers, 1)
sum(numbers)

# Use for loops to make a turtle draw these regular polygons
# (regular means all sides the same lengths, all angles the same):
# • An equilateral triangle
# • A square
# • A hexagon (six sides)
# • An octagon (eight sides)

import turtle
window = turtle.Screen()
tess = turtle.Turtle()
tess.pendown()

# A equilateral triangle
for _ in range(3):
    tess.forward(10)
    tess.left(120)

# A square
for _ in range(4):
    tess.forward(10)
    tess.left(90)

# A hexagon
for _ in range(6):
    tess.forward(10)
    tess.left(60)

# An octagon
for _ in range(8):
    tess.forward(10)
    tess.left(45)

# 6, 7
turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for _ in turns:
    tess.forward(100)
    tess.left(_)

# 8
for _ in range(18):
    tess.forward(100)
    tess.left(360/18)

# 9
tess.right(90)
tess.left(3600)
tess.right(-90)
tess.speed(10)
tess.left(3600)
tess.speed(0)
tess.left(3645)
tess.forward(-100)

# 10
for _ in range(5):
    tess.forward(100)
    tess.left(72) # 360/5

# 11
tess.penup()
tess.stamp()
for _ in range(12):
    tess.forward(100)
    tess.stamp()
    tess.backward(100)
    tess.left(30) # 360/12

# 12
type(tess) # Turtle Class