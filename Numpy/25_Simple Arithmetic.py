import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

print('Sum of Array1 & Array2:')
newarr = np.add(arr1, arr2)
print(newarr)

print('Subtraction of Array1 & Array2:')
newarr = np.subtract(arr1, arr2)
print(newarr)

print('Multiplicatin of Array1 & Array2:')
newarr = np.multiply(arr1, arr2)
print(newarr)

print('Division of Array1 & Array2:')
newarr = np.divide(arr1, arr2)
print(newarr)

print('REminder of Array2 & Array1:')
newarr = np.mod(arr2, arr1)     # "np.reminder" do the same
print(newarr)

#Quotient and Mod
print('Quotient and Mod')
newarr = np.divmod(arr1, arr2)
print(newarr)

print('Power of Array1 & Array2:')
newarr = np.power(arr1, arr2)
print(newarr)

print('Absolute Values')
arr = np.array([-1, -2, 1, 2, 3, -4])

newarr = np.absolute(arr)
print(newarr)

