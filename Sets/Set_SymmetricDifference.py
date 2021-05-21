# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
a = list(map(int,input().split()))
set_A = set(a)
N = int(input())
b = list(map(int,input().split()))
set_B = set(b)

x = []
y = []
x = set_A.difference(set_B)
y = set_B.difference(set_A)
z = x.union(y)
z = sorted(z)

#print(x,y,z)
for i in z:
    print(i)