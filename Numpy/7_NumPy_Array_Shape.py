import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print('The shape of an array is the number of elements in each dimension.')

#Print the shape of a 2-D array
print(arr.shape)

#Print the shape of a 5-D array
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)

#Reshaping arrays
print('\n\nReshape From 1-D to 2-D')
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)
print(newarr)

print('\n\nReshape From 1-D to 3-D')
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)
print(newarr)

#Returns Copy or View?
print('Base/Return Type of reshape:', newarr)

#Unknown Dimension

newarr = arr.reshape(2, 2, -1)  #Numpy calculate the dimension
print(newarr)






