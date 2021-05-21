import numpy as np

arr = [-3.1666, 3.6667]

#Truncation : Remove the decimals, and return the float number closest to zero
print('Truncation of arr is:', np.trunc(arr))

#Fix do just like trunc
print('Fix of arr is:', np.fix(arr))

#Rounding :  increments preceding digit or decimal by 1 if >=5 else do nothing.
print('Round of 3.1666 in 3 degit is:', np.around(3.1666, 3))

#The floor() function rounds off decimal to nearest lower integer.
print('Floor of arr is:', np.floor(arr))

#The ceil() function rounds off decimal to nearest upper integer.
print('Ceiling of arr is:', np.ceil(arr))




