# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int,input().split()))
t = {}

n = int(input())
for i in range(n):
    s = set(map(int,input().split()))
    
    t = s.union(t)
    
if t.intersection(A) == t:    
    print("True")
else:
    print("False")