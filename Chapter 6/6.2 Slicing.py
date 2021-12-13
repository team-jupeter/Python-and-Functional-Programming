import numpy as np

a = np.array([2, 3, 8])
a[2] # 8
a[1:] # np.array([3, 8])

b = np.array([
    [2, 3, 8],
    [4, 5, 6],
    ])
b[1] # array([4, 5, 6])
b[1][2] # 6
b[1, 2] # 6
b[:, 1] # array([3, 5])