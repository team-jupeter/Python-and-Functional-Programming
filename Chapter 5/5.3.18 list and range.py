letters = list("Crunchy Frog")
letters # ["C", "r", "u", "n", "c", "h", "y", " ", "F", "r", "o", "g"]
"".join(letters) # 'Crunchy Frog'

# lazy
def f(n):
    """ Find the first positive integer between 101 and less
    than n that is divisible by 21
    """
    for i in range(101, n):
        if (i % 21 == 0):
            return i

print(f(110) == 105)
print(f(1000000000) == 105)

range(10) # Create a lazy promise - range(0, 10)
list(range(10)) # Call in the promise, to produce a list. - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]