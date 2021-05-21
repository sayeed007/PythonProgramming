import numpy as np
from math import log

arr = np.arange(1, 10)
print(arr)

#Log at Base 2
print("Log of base 2")
for i in arr:
    print("log2(",i,')', np.log2(i))

#Log at Base 10
print("Log of base 10")
for i in arr:
    print("log10(",i,')', np.log10(i))

#Natural Log, or Log at Base e
print("Log of base e")
for i in arr:
    print("loge(",i,')', np.log(i))

#Log at Any Base
print("Log of any base")
nplog = np.frompyfunc(log, 2, 1)
#Creat your own function with log which has 2 input and 1 output || named of the function is nplog
print(nplog(100, 15))

