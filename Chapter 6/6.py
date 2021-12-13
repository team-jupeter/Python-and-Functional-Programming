# a = [2, 3, 8]
# 2 * a # [2, 3, 8, 2, 3, 8]

# a = [2, 3, 8]
# 2 * a
# # 2.1 * a # TypeError: can't multiply sequence by non-int of type 'float'

# values = [2, 3, 8]
# result = []
# for x in values:
#     result.append(2.1 * x)

import numpy as np
a = np.array([2, 3, 8])

print(a)
print(2.1 * a) # array([ 4.2, 6.3, 16.8])
print(np.dot(a,a))