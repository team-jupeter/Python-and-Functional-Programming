import random
joe = random.Random()

def sum1():
    """ Build a list of random numbers, then sum them """
    xs = []
    for i in range(10000000):
        num = joe.randrange(1000) # Generate one random number
        xs.append(num) # Save it in our list

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

# ####### Functional
# # using reduce to compute sum of list
# import functools

# sum3 = functools.reduce(lambda a, b: a+b, range(10000000))
# print(sum3)

# # using reduce to compute maximum element from list
# xs = [1, 3, 5, 6, 2, ]

# print("The maximum element of the list is : ", end="")
# print(functools.reduce(lambda a, b: a if a > b else b, xs))