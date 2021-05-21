import numpy as np

#Accessing 1-D Array
arr = np.array([1, 2, 3, 4])
print('\n2nd element of the array: ',arr[1])

#Accessing 2-D Array
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('\n2nd element on 1st dim: ', arr[0, 1])
print('\n5th element on 2nd dim: ', arr[1, 4])

#Access 3-D Arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("\nSecond Row Third Column value of First Entity: ",arr[0, 1, 2])

#Negative Indexing
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])








