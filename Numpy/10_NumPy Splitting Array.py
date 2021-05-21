import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

#Split the array in 3 parts/ 2-D Arrays
newarr = np.array_split(arr, 4) #array_split can adjust the array size in the last
newarr2 = np.split(arr, 3) #Split can only create equal size arrays
print(newarr)
print(newarr2)

#Access the splitted arrays
print('\nAccess the splitted array:')
print(newarr[0])
print(newarr[1])
print(newarr[2])

#Split the 2-D array into three 2-D arrays
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)
print('2-D array split:')
for i in newarr:
    print(i)

print('\nSplit the 2-D array into three 2-D arrays along rows.')
newarr = np.array_split(arr, 3, axis=1)
for i in newarr:
 print(newarr)

#hsplit() method to split the 2-D array into three 2-D arrays along rows.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(arr, 3)
print(newarr)
print(' Similar alternates to vstack() and dstack() are available as vsplit() and dsplit()')




