import numpy as np

#Iterating 2-D Arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

print('Iterate on each scalar element of the 2-D array:')
for x in arr:
  for y in x:
    print(y)

#Iterating 3-D Arrays
print('Iterating 3-D Arrays')
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)
print('Iterate down to the scalars of 3-D Array:')
for x in arr:
  for y in x:
    for z in y:
      print(z)

#Iterating Arrays Using nditer()
print('Iterating on Each Element using nditer() ')
for x in np.nditer(arr):
  print(x)

#Iterating Array With Different Data Types with op_dtypes=['']
arr = np.array([1, 2, 3])
print('Iterate through the array as a string:')
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

#Iterating With Different Step Size
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print('Iterate through every scalar element of the 2D array skipping 1 element:')
for x in np.nditer(arr[:, ::2]):
  print(x)

#Enumerated Iteration Using ndenumerate()
arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)     #idx store position number




