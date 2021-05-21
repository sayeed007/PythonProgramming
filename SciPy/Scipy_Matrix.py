import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
print(csr_matrix(arr))
#returns non zero value's position

print(csr_matrix(arr).data)
#Returns only non zero values

print(csr_matrix(arr).count_nonzero())
#REturns total number of non zero values

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
mat = csr_matrix(arr)
mat.eliminate_zeros()
#Element all zero values
print("matrix = \n",mat)

#Eliminating duplicates by adding them:
mat = csr_matrix(arr)
mat.sum_duplicates()

print(mat)

#onverting from csr to csc with the tocsc() method
newarr = csr_matrix(arr).tocsc()
print(newarr)


