# 5.3.3 List length
horsemens = ["war", "famine", "pestilence", "death"]

# Code 1
for i in range(len(horsemens)):
    print(horsemens[i])

# Code 2
for horseman in horsemens:
    print(horseman)

# Code 3
len(["car makers", 1, ["Ford", "Toyota", "BMW"], [1, 2, 3]])

#### Functional
# ##### Iterating With Python Lambdas
# # 1
# x = [2, 3, 4, 5, 6]
# y = []
# for v in x :
#     y += [v * 5]
# assert x == [ 2,  3,  4,  5,  6]
# assert y == [10, 15, 20, 25, 30]

# # 2
# x = [2, 3, 4, 5, 6]
# y = [v * 5 for v in x]

# # 3
# x = [2, 3, 4, 5, 6]
# y = map(lambda v : v * 5, x)

# # example 2
# # 1
# x = [2, 3, 4, 5, 6]
# y = []
# for v in x :
#     if v % 2 : # condition
#         y += [v * 5]
# assert x == [2, 3, 4, 5, 6]
# assert y == [15, 25]

# # 2
# x = [2, 3, 4, 5, 6]
# y = [v * 5 for v in x if v % 2] # condition

# # 3 - map(fun, iter)
# x = [2, 3, 4, 5, 6]
# y = map(lambda v : v * 5, filter(lambda u : u % 2, x))
# print(list(y))

# # filter(function, iterable) --> [item for item in iterable if function(item)]
# [v * 5 for v in x if v % 2]  #list comprehension
# # map(lambda for v: v * 5, for filter(lambda for v: if v % 2, in x)) #"pseudo" lambda and list comprehension
# map(lambda v : v * 5, filter(lambda u : u % 2, x)) #lambda, just a 'rearrangement' of what we had before

# ### another example
# x = [2, 3, 4]
# y = [4, 5]
# z = []
# for v in x :
#     for w in y :
#         z += [v + w]
# assert x == [2, 3, 4]
# assert y == [4, 5]
# assert z == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]
# assert z == [6, 7, 7, 8, 8, 9]

# # Now with a list comprehension...
# x = [2, 3, 4]
# y = [4, 5]
# z = [v + w for v in x for w in y]

# # And finally with lamdas....
# x = [2, 3, 4]
# y = [4, 5]
# t = map(lambda v : map(lambda w : v + w, y), x)

# result = list(map(list, t))
# print(result)

# # z = sum(t, [])
# # print(z)

# # another example - List of strings
# l = ['sat', 'bat', 'cat', 'mat']

# # map() can listify the list of strings individually
# test = list(map(list, l))
# print(test)


# [v + w for v in x for w in y]                              #list comprehension
# # map(lambda for v: in map(lambda for w: v + w, in y), in x) #"pseudo" lambda
# map(lambda v : map(lambda w : v + w, y), x)                #lambda

# assert t == [[6, 7], [7, 8], [8, 9]]
# z = sum(t, [])
# assert z == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]
# assert z == [6, 7, 7, 8, 8, 9]