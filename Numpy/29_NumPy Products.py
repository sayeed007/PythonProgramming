import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

x = np.prod([arr1, arr2])
print(x)

#Product Over an Axis
newarr = np.prod([arr1, arr2], axis=1)
print(newarr)

#Cummulative Product
newarr = np.cumprod(arr1)
print(newarr)









