
import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, arr):
    count = 0

    for i in range(n):
        print("i= ",i)
        for j in range(i, n):
            if(i != j):
                sum = arr[i]+arr[j]
                print("sum= " ,sum)
                if(sum == k or sum%k == 0):
                    count += 1
                    print("count= ",count, arr[i],arr[j])

    return count




n = 6  #total element

k = 3  #total sum

arr = [1,3, 2, 6, 1, 2]

result = divisibleSumPairs(n, k, arr)

print(result)
