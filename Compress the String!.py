from itertools import *

s = input()
li = list(s)

#print(list(groupby(map(int,li))))

for i,j in groupby(map(int,li)):
    print(tuple([len(list(j)), i]) ,end = " ")