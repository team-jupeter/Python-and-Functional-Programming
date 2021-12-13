### Code 1
def koch(tortoise, order, size):
    """
    Make turtle tortoise draw a Koch fractal of 'order' and 'size'.
    Leave the turtle facing the same direction.
    """

    if order == 0: # The base case is just a straight line
        tortoise.forward(size)
    else:
        koch(tortoise, order-1, size/3) # Go 1/3 of the way
        tortoise.left(60)
        koch(tortoise, order-1, size/3)
        tortoise.right(120)
        koch(tortoise, order-1, size/3)
        tortoise.left(60)
        koch(tortoise, order-1, size/3)

#### Code 2
def koch(tortoise, order, size):
    if order == 0:
        tortoise.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(tortoise, order-1, size/3) # Recursion
            tortoise.left(angle)

##### Code 3
def koch_0(tortoise, size):
    tortoise.forward(size)

def koch_1(tortoise, size):
    for angle in [60, -120, 60, 0]:
        koch_0(tortoise, size/3)
        tortoise.left(angle)

def koch_2(tortoise, size):
    for angle in [60, -120, 60, 0]:
        koch_1(tortoise, size/3)
        tortoise.left(angle)

def koch_3(tortoise, size):
    for angle in [60, -120, 60, 0]:
        koch_2(tortoise, size/3)
        tortoise.left(angle)