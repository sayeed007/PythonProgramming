import numpy as np

#Checking the Data Type of an Array
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

#Creating Arrays With a Defined Data Type
#String
arr = np.array([1, 2, 3, 4], dtype='S')
print("array =", arr)
print("Array Data Type : ", arr.dtype)

#4-Byte Integer
arr = np.array([1, 2, 3, 4], dtype='i4')
print("array =", arr)
print("Array Data Type : ", arr.dtype)

#Converting Data Type on Existing Arrays || astype()
arr = np.array([1.1, -4, 3.1])

newarr = arr.astype(bool)   #Also use[int/float/str]
print(newarr)
print(newarr.dtype)













