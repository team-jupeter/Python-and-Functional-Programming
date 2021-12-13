# The while statement

# while <CONDITION> Expression:
#     <STATEMENT>

n = 6
current_sum = 0
i = 0
while i <= n:
    current_sum += i
    i += 1
print(current_sum)

n = 6
current_sum = 0
for i in range(n+1): # [0, ... , 6]
    current_sum += i
print(current_sum)

# functional
# Code 1
from functools import reduce
reduce(lambda acc, x : acc + x, range(7), 0)

# Code 2
sum(range(7))

