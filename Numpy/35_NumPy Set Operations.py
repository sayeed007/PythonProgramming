import numpy as np

#Create Sets in NumPy
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])

x = np.unique(arr)
print(x)

#Finding Union
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)
print('Union arr1 & arr2 is:\n', newarr)

#Finding Intersection
newarr = np.intersect1d(arr1, arr2, assume_unique=True)
print('Intersection arr1 & arr2 is:\n', newarr)

#Finding Difference
newarr = np.setdiff1d(arr1, arr2, assume_unique=True)
print('Difference arr1 & arr2 is:\n',newarr)

#Finding Symmetric Difference
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr = np.setxor1d(set1, set2, assume_unique=True)
print('Finding Symmetric Difference: \n', newarr)









