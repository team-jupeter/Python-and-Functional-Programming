# Conditional execution
x = 1

if x % 2 == 0:
    print(x, " is even.")
    print("Did you know that 2 is the only even number that is prime?")
else:
    print(x, " is odd.")
    print("Did you know that multiplying two odd numbers " +
    "always gives an odd result?")

# The indented statements that follow are called a block.
# The first unindented statement marks the end of the block.

# if <BOOLEAN EXPRESSION>:
#     <STATEMENTS_1> # Executed if condition evaluates to True
# else:
#     <STATEMENTS_2> # Executed if condition evaluates to False

# pass statement
# if True: # This is always True,
#     pass # so this is always executed, but it does nothing
# else:
#     pass # And this is never executed

