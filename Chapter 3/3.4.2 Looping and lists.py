# # 3.4.2 Looping and lists
import random
ran = random.Random()

# Version 1
# Build a list of random numbers, then sum them
numbers = [] # integers are stored in memory.
for _ in range(10000000): # 16*10,000,000
    num = ran.randrange(1000) # Generate one random number
    numbers.append(num) # Save it in our list, see the next chapter

total = sum(numbers)
print(total)

# Version 2
# Sum the random numbers as we generate them
total = 0
for _ in range(10000000):
    num = ran.randrange(1000)
    total += num # 32
print(total) # integer

# LC return a list. Error
# [total += num or _ in range(10000000)]

# Functional_1
from functools import reduce
sum = reduce(lambda acc, x : acc + x, range(10000000), 0)
print(sum)

# Functional_2
print(sum(range(10000000)))



