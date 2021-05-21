import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

#Find the indexes where the value is 4:
x = np.where(arr == 4)
print('value 4 found in array position: \n', x)

#Find the indexes where the values are even
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0) #Find the values whose index is even
print('Given condition matched values are: \n', x)

#Find the indexes where the value 7 should be inserted
arr = np.array([7, 8, 7, 5, 7, 5, 8, 9])

#Default Left to right search 
x = np.searchsorted(arr, 7)     #searchsorted() method is assumed to be used on sorted arrays.
print('Ledt to right ', x)
#Right to left search
x = np.searchsorted(arr, 7, side='right')
print('right to left ', x)

#Find the indexes where the values 2, 4, and 6 should be inserted
arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])
print('Index for 2,4,6  is : ', x)







