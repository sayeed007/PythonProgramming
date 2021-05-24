import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    if n == 0:
        return 1
    else:
        x = 1
        for i in range(n):
            if i % 2 == 0:
                x += 1
            else:
                x = x*2
        return x


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
