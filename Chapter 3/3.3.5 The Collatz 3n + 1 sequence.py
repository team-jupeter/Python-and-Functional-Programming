# The Collatz 3n + 1 sequence by  a German mathematician called Lothar Collatz.
n = 27371

# Code 1
while n != 1:
    print(n, end=", ")

    if n % 2 == 0: # n is even
        n = n // 2
    else: # n is odd
        n = n * 3 + 1

print(n, end=".\n")

# Code 2
def collatz(n: int) -> int:
    if n == 1:
        print(n)
        return 1
    elif n % 2 == 0:
        print(n)
        return 1 + collatz(n // 2)
    else:  # n % 2 == 1:
        print(n)
        return 1 + collatz(3 * n + 1)

collatz(435345)


