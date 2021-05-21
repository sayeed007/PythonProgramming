import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr)
print(newarr)

#We can perform this operation repeatedly by giving parameter n.
newarr = np.diff(arr, n=2) #Do the same work n time
print(newarr)










