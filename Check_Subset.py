# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
lis = []

for i in range(T):
    na = int(input())
    A = set(map(int,input().split()))
    
    nb = int(input())
    B = set(map(int,input().split()))
    
    X = A.intersection(B)
    
    if A == X:
        lis.append("True")
    else:
        lis.append("False")

for i in lis:
    print(i)
    
    
