import numpy as np

a = np.array([230, 10, 284, 39, 76])
cutoff = 200
a > cutoff # np.array([True, False, True, False, False])

a = np.array([230, 10, 284, 39, 76])
cutoff = 200
a[a > cutoff] = 0
a # np.array([0, 10, 0, 39, 76])

a = np.array([230, 10, 284, 39, 76])
cutoff = 200
new_a = []
for x in a:
    if x > cutoff:
        new_a.append(0)
    else:
        new_a.append(x)
a = np.array(new_a)

##### Functional
a = np.array([230, 10, 284, 39, 76])
cutoff = 200

[a[i] if v <= cutoff else 0 for i, v in enumerate(a)]

