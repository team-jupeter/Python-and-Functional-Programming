import numpy as np
a = np.array([200], dtype='uint8')
a + a # array([144], dtype=uint8)

a = np.array([200], dtype='uint16')
a + a # array([400], dtype=uint16)

a = np.array([200], dtype='uint8')
a.astype('uint64')