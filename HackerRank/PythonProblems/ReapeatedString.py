import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    number=s.count('a')
    if number==0:
        return 0
    elif number==1 and len(s)==1:
        return n
    else:
        repeats = n//len(s) 

        remainders= n%len(s)

        count = str(number*repeats+s[:remainders].count('a')) 

    return count


if __name__ == '__main__':
    s = "a"     #input()

    n = 100000  # int(input())

    result = repeatedString(s, n)

    print(result)
