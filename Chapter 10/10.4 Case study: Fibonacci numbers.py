def fib(n):
    if n <= 1:
        return n
    t = fib(n-1) + fib(n-2)
    return t

# fib(0) = 0
# fib(1) = 1
# fib(n) = fib(n-1) + fib(n-2) for n >= 2

import time
time.process_time
t0 = time.process_time()
n = 35
result = fib(n)
t1 = time.process_time()

print(f"fib({n}) = {result}, ({t1-t0} secs)")


#### Functional
# Code 1 - By using lambda and reduce method
from functools import reduce
fib = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0, 1])
print(fib(15))

# Code 2 - By using lambda and map function
def fibonacci(count):
    fib_list = [0, 1]
    any(map(lambda _: fib_list.append(sum(fib_list[-2:])), range(2, count)))
    return fib_list[:count]

print(fibonacci(10))


