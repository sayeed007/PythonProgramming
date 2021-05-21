import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    if(c[0] == 0):
        count = 0
        current = 0
    else:
        current = 1
        count = 1
    
    i = current
    while(i < len(c)-2):
        if c[i+1] == 1 and c[i+2] == 0:
            i = i+2
            count += 1
        else:#(c[i+1] == 0 and c[i+2] == 1):
            i = i+1
            count += 1
    return count

if __name__ == '__main__':

    n = 6#int(input())

    c = [0, 0, 0, 0, 1, 0]  #list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    print(result)