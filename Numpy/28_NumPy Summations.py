import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2])
print(newarr)

#Summation Over an Axis
newarr = np.sum([arr1, arr2], axis=0)
print(newarr)

#Cummulative Sum
arr = np.array([1, 2, 3])

newarr = np.cumsum(arr)
print('Cummulative sum of arr is : ', newarr)










