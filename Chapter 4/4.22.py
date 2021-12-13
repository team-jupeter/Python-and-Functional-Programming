# 4.22 Looping and lists

import random
joe = random.Random()

def sum1():
    """ Build a list of random numbers, then sum them """
    xs = []
    for i in range(10000000):
        num = joe.randrange(1000) # Generate one random number
        xs.append(num) # Save it in our list
    print(xs)
    tot = sum(xs)
    return tot


def sum2():
    """ Sum the random numbers as we generate them """
    tot = 0
    for i in range(10000000):
        num = joe.randrange(1000)
        tot += num
    return tot

print(sum1())
print(sum2())

# ##### Be functional
# from functools import reduce
# lst = [joe.randrange(1000) for _ in range(10000000)]
# result = reduce(lambda a, b: a+b, lst)
# print(result)