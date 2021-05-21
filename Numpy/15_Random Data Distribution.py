from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
'''
    p => probability distribution function
    3 => 10%
    5 => 30%
    7 => 60%
    9 =>  0%
'''
print(x)