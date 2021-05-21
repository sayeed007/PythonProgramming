import numpy as np

arr = np.array([3, 2, 0, 1])
#Sort the array:
print('Sorted arra:\n', np.sort(arr)) #sort neumerically
#This method returns a copy of the array, leaving the original array unchanged.

arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))     #sort string alphabetically

arr = np.array([True, False, True])
print(np.sort(arr))     #sort boolean alphabetically

#Sorting a 2-D Array
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))











