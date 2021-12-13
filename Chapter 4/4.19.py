# 4.19 Problems with logic and flow of control
def any_odd(xs): # Buggy version
    """ Return True if there is an odd number in xs, a list of integers. """
    for v in xs:
        if v % 2 == 1:
            return True
        else:
            return False

def any_odd(xs): # Still buggy
    """ Return True if there is an odd number in xs, a list of integers. """
    count = 0
    for v in xs:
        if v % 2 == 1:
            count += 1 # Count the odd numbers
        if count > 0:
            return True
        else:
            return False

def any_odd(xs): # Still buggy
    """ Return True if there is an odd number in xs, a list of integers. """
    count = 0
    for v in xs:
        if v % 2 == 1:
            count += 1 # Count the odd numbers
    return count > 0 # Aha! a programmer who understands that Boolean
                     # expressions are not just used in if statements!


def any_odd(xs): # Rather concise version
    for v in xs:
        if v % 2 == 1:
            return True
    else:
        return False

# ##### Be functional
# xs = [2, 4, 5, 8]
# result = [x % 2 == 1 for x in xs]
# print(result)

# result = [x for x in xs if x % 2 == 1 ]
# print(result)

# result = any(x % 2 == 1 for x in xs)
# print(result)
