import time

def do_my_sum(xs):
    sum = 0
    for v in xs:
        sum += v
    return sum

sz = 10000000 # Lets have 10 million elements in the list
testdata = range(sz)
t0 = time.process_time()
my_result = do_my_sum(testdata)
t1 = time.process_time()
print(f"my_result = {my_result} (time taken = {t1-t0} seconds)")
t2 = time.process_time()
their_result = sum(testdata)
t3 = time.process_time()
print(f"their_result = {their_result} (time taken = {t3-t2} seconds)")

####### Functional
import functools
sz = 10000000 # Lets have 10 million elements in the list
testdata = range(sz)
t4 = time.process_time()
func_result = functools.reduce(lambda x, acc : acc + x, testdata, 0)
t5 = time.process_time()

print(f"functional_result = {func_result} (time taken = {t5-t4} seconds)")

