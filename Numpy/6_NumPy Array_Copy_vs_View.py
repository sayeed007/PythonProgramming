import numpy as np

print('the copy is a new array, \nThe view is just a view of the original array.')
arr = np.array([1, 2, 3, 4, 5])

#COPY
print('\nCOPY:')
x = arr.copy()
arr[0] = 42

print('After Changing Original array value:')
print("Original Array arr = ", arr)
print('Copied Array X = ', x)

#Changing into the view
x[0] = 11

print('After Changing Copy array value:')
print("Original Array arr = ", arr)
print('Viewed Array x = ', x)

#VIEW
print('\n\nVIEW:')
y = arr.view()
arr[0] = 42

print('After Changing Original array value:')
print("Original Array arr = ", arr)
print('Viewed Array Y = ', y)

#Changing into the view
y = arr.view()
y[0] = 22

print('After Changing View array value:')
print("Original Array arr = ", arr)
print('Viewed Array Y = ', y)

#Check if Array Owns it's Data
print(x.base)   # None => the array owns the data.
print(y.base)   #the base  attribute refers to the original object.












