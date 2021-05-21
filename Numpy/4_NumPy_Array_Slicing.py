import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5]) #sHOWING 2ND TO 5TH ELEMENTS
print(arr[4:])  #5th to Last
print(arr[:4]) #1st to 3rd, not including 5th

#Negative Slicing
print(arr[-3:-1])   #3rd last index to 2nd last index || not including the last element


#STEP
print(arr[1:5:2])   #2nd to 5th position whis stem 2
print(arr[::2])     #all element with step 2


#Slicing 2-D Arrays
print('\nSlicing 2-D Arrays')
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])  #from 1st array
print(arr[0:2, 2])  #from 2nd array

print(arr[0:2, 1:4])    #From both array









