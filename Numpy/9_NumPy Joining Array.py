import numpy as np

#Join two 1-D arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
print(arr)

#Join two 2-D arrays along rows (axis=1):
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

#Joining Arrays Using Stack Functions
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6]) #Two input must have same shape

arr = np.stack((arr1, arr2), axis=1)    #Basic Concatatenate without axis
print(arr)

#Stacking Along Rows
arr = np.hstack((arr1, arr2))
print('Stacking Along Rows: \n', arr)

#Stacking Along Columns
arr = np.vstack((arr1, arr2))
print('Stacking Along Columns: \n', arr)

#Stacking Along Height (depth)
arr = np.dstack((arr1, arr2))
print('Stacking Along Height (depth): \n', arr)
print('Dimention of dstack: ', arr.ndim)






