# 3.3.9 Tables
for x in range(13): # Generate numbers 0 to 12
    print(x, "\t", 2**x)

# list comprehension
[print(x, "\t", 2**x) for x in range(13)]

# functional
any(map(lambda x : print(x, "\t", 2**x), range(13)))