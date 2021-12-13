# 4.14 Boolean functions
def is_divisible(x, y):
    """ Test if x is exactly divisible by y """
    if x % y == 0:
        return True
    else:
        return False

def is_divisible(x, y):
    return x % y == 0

is_divisible(6, 4)

