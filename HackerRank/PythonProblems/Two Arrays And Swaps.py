import os
import sys


def timeConversion(s):
    temp = s[-2]
    if temp == "P":
        print("x")
        return 1



if __name__ == '__main__':

    s = "07:05:45PM"
    arr = list(s.split(":"))

    print(arr)

    result = timeConversion(s)

    if result == 1:
        x = int(arr[0]) + 12
        print(x)
        arr[0] = str(x)
    
    result = ":".join(arr)
    print(result)
