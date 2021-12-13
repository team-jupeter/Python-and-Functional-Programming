import numpy as np
a = np.array([
    [0, 1],
    [2, 3],
    [4, 5],
    ])
b = np.array([10, 100])
print(b.shape )
print(a * b)

c = np.array([[1, 2]])
c.shape # (1, 2)

d = np.array([
    [0, 1, 2],
    [3, 4, 5],
    ])
b = np.array([10, 100])
# d * b # ValueError: operands could not be broadcast together with shapes (2,3) (2,)

c = np.array([
    [0, 1, 2],
    [3, 4, 5],
    ])
b = np.array([10, 100])
c * b[:, None]
