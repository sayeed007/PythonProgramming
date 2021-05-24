import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    n = len(a)
    ans = []
    for q in queries:
        ans.append(a[(n-k+q)%n])
    return ans
    

if __name__ == '__main__':
    n = 3

    k = 2

    q = 3

    a = [1, 2, 3]
    
    queries = [0, 1, 2]

    result = circularArrayRotation(a, k, queries)

    print(result)
