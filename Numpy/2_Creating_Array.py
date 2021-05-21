import numpy as np

arr = np.array([1, 2, 3, 4, 5])
#(1, 2, 3, 4, 5) => tupple also converted into ndarray

print(arr)
print("Type of Numpy defined array", type(arr))

#0-D Array
a = np.array(42)
print("\nExample of 0-D Arrays", a)
print("Number of Dimensions =",a.ndim)

#1-D Array
b = np.array([1, 2, 3, 4, 5])
print("\nExample of 1-D Arrays", b)
print("Number of Dimensions =",b.ndim)

#2-D Array [Array of Array]
c = np.array([[1, 2, 3], [4, 5, 6]])
print("\nExample of 2-D Arrays\n", c)
print("Number of Dimensions =",c.ndim)

#3-D Array [Array of matrix or 2-D arrays]
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("\nExample of 3-D Arrays\n", d)
print("Number of Dimensions =",d.ndim)

#PreDefining Array Dimensions
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('\nnumber of dimensions :', arr.ndim)
'''
    []          => innermost dimension elements
   [[]]        => vector with element
  [[[]]]      => matrix with vector
 [[[[]]]]    => 4th dimension has 3-D Array
[[[[[]]]]]  => 5th dimension has 4-D Array
'''











