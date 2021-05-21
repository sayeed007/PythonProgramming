x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z)

#print('ufuncs stands for "Universal Functions" ')
print('ufuncs stands for "Universal Functions" ')

import numpy as np

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)

print('using numpy.add function adding 2 arrays: ',z)





