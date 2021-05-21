from numpy import random
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

#Shuffling Arrays
print('Original Array: \n', arr)
random.shuffle(arr)
print('Shuffeled Array: \n', arr)       #Original Array Changed

#Generating Permutation of Arrays
print('Permutation of Array: \n', random.permutation(arr))  #Original array unchanged




















