from itertools import product

A = list(map(int,input().strip().split()))
B = list(map(int,input().strip().split()))

for i in product(A, B):
    print(i, end = " ")