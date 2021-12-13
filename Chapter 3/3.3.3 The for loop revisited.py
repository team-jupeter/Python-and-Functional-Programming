# The for loop revisited
for friend in ["Joe", "Zoe", "Zuki", "Thandi", "Paris"]:
    invite = f"Hi {friend} Please come to my party!"
    print(invite)

numbers = [5, 6, 32, 21, 9]
running_total = 0
for number in numbers:
    running_total = running_total + number
print(running_total)

for number in numbers:
    running_total += number
print(running_total)

# functional
# import functools
from functools import reduce
reduce(lambda acc, x : acc + x, numbers, 0) # accumulator



