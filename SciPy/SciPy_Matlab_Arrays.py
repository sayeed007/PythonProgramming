from scipy import io
import numpy as np

#Export the following array as variable name "vec" to a mat file
arr = np.arange(100) #arange => 0 to specific range
print(arr)
#io.savemat('file_name.mat', {"Variable_Name": arr})
io.savemat('arr.mat', {"vec": arr})

#Import Data from Matlab Format
mydata = io.loadmat('arr.mat')
print(mydata)
print("Only Mat_Values\n", mydata['vec'])


#In order to remain the same dimension, we can pass an additional argument squeeze_me=True
mydata = io.loadmat('arr.mat', squeeze_me=True)
print(mydata['vec'])












