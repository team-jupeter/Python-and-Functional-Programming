# Omitting the else clause
# else is not a statement. The if statement has two clauses,
# one of which is the (optional) else clause.
import math
x = 1
if x < 0:
    print("The negative number ", x, " is not valid here.")
    x = 42
    print("I've decided to use the number 42 instead.")

print("The square root of ", x, "is", math.sqrt(x))