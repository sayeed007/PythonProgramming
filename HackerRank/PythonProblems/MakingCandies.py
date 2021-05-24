
import math
import os
import random
import re
import sys

# Complete the minimumPasses function below.
def minimumPasses(m, w, p, n):
                # 3/4  1/2/3/4  2  12
    candies = 0
    count = 1
    while(candies<= n):
        print("Count= ",count)
        print("m = ",m ,"w= ",w)
        candies += m * w
        print("Candies= ", candies,"\n")
        if candies >= n:
            return count
        if candies * 2 >= n:
            count += 1
            continue
        else:
            while(candies >= p ):
                if (w+1)*m > (m+1)*w:
                    candies = candies - p
                    w += 1
                else:
                    candies = candies - p
                    m += 1 
        count += 1


        

if __name__ == '__main__':
    m = 1#int(mwpn[0])

    w = 1#int(mwpn[1])

    p = 6#int(mwpn[2])

    n = 45#int(mwpn[3])

    result = minimumPasses(m, w, p, n)

    print (result)
