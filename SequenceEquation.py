import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    arr = []
    
    for i in range(1,len(p)+1):
        z = p.index(i)
        y = p.index(z+1)
        arr.append(y+1)
        
    return arr    
        #z = p[y]
        #p[z] == i

if __name__ == '__main__':
    n = 3#int(input())

    p = [2, 3, 1]#list(map(int, input().rstrip().split()))

    result = permutationEquation(p)
    for i in result:
        print(i)
        #2 3 1