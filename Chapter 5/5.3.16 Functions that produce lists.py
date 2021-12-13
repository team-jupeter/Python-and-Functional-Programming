# initialize a result variable to be an empty list
# loop
#     create a new element
#     append it to result
# return the result
import sympy
def primes_lessthan(n):
    """ Return a list of all prime numbers less than n. """
    result = []
    for i in range(2, n):
        if sympy.is_prime(i): # condition
            result.append(i)
    return result

##### Functional
primes_lessthan = lambda n : filter(sympy.is_prime, range(2, n))

xs = primes_lessthan(30)
print(xs)