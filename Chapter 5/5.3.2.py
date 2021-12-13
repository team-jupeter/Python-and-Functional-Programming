# 5.3.2 Accessing elements
numbers = [17, 123]
numbers[0] #17
numbers[9-8] # 123
numbers[1.0]
# Traceback (most recent call last):
# File "<interactive input>", line 1, in <module>
# TypeError: list indices must be integers, not float

numbers[2]
# Traceback (most recent call last):
# File "<interactive input>", line 1, in <module>
# IndexError: list index out of range


horsemen = ["war", "famine", "pestilence", "death"]

# 1
for i in [0, 1, 2, 3]:
    print(horsemen[i])

# 2
for h in horsemen:
    print(h)

# 3
[print(i) for i in horsemen]

# ##### Functional - Python map() function
# map(fun, iter)
# map(lambda i: print(i), horsemen)

# CODE 1
# Return double of n
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# CODE 2
# Double all numbers using map and lambda
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

# CODE 3
# Add two lists using map and lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# CODE 4
# List of strings
l = ['sat', 'bat', 'cat', 'mat']

l_1 = list('sat')
print(l_1)

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)


