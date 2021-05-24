import math
import random

from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    time_format = '%a %d %b %Y %H:%M:%S %z'
    """
        %a = weekday
        %d = Day of month 01-31
        %b = Month name, short version
        %Y = Year, full version
        %H:= Hour 00-23
        %M:= Minute 00-59
        %S = Second 00-59
        %z = UTC offset    +0100
    """
    t1 = datetime.strptime(t1, time_format)
    t2 = datetime.strptime(t2, time_format)
    return str(int(abs((t1-t2).total_seconds())))   

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print(delta + '\n')
