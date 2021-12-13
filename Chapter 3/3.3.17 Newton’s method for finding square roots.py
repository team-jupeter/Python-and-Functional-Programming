# Newton's method for finding square roots

# better = (approximation + n/approximation)/2
n = 888
threshold = 0.00001
approximation = n/2 # Start with some or other guess at the answer

while True:
    better = (approximation + n/approximation)/2
    print(better)
    if abs(approximation - better) < threshold:
        print(better)
        break
    approximation = better


# the square root of 4 is 2.
# the square root of 10 is ?.

